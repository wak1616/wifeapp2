document.addEventListener('DOMContentLoaded', function() {
    // Chat elements
    const chatContainer = document.querySelector('.chat-container');
    const chatMessages = document.querySelector('.chat-messages');
    const chatInput = document.getElementById('chat-input');
    const sendButton = document.getElementById('send-message');
    const closeChat = document.querySelector('.close-chat');

    // Only initialize chat functionality if we're on a page with chat elements
    if (chatContainer && chatMessages && chatInput && sendButton && closeChat) {
        let currentTip = '';
        let chatType = '';
        let processedTips = new Set();
        let isProcessing = false;

        // Remove any existing event listeners first
        document.querySelectorAll('.tip-card').forEach(card => {
            card.replaceWith(card.cloneNode(true));
        });

        // Handle tip card clicks - with single event binding
        const tipCards = document.querySelectorAll('.tip-card');
        tipCards.forEach(card => {
            const handler = async function(e) {
                e.stopPropagation();
                e.preventDefault();
                
                // Prevent multiple clicks while processing
                if (isProcessing) return;

                chatType = this.dataset.type;
                currentTip = this.querySelector('.tip-content p').textContent;
                const tipId = `${chatType}:${currentTip}`;
                
                if (!processedTips.has(tipId)) {
                    try {
                        isProcessing = true;
                        
                        // Remove event listener to prevent multiple triggers
                        card.removeEventListener('click', handler);
                        
                        // Show chat container
                        chatContainer.style.display = 'flex';
                        
                        // Clear any existing thinking messages first
                        const existingThinking = document.getElementById('thinking-message');
                        if (existingThinking) {
                            existingThinking.remove();
                        }
                        
                        // Add thinking message
                        const thinkingDiv = document.createElement('div');
                        thinkingDiv.classList.add('thinking');
                        thinkingDiv.textContent = 'Thinking...';
                        thinkingDiv.id = 'thinking-message';
                        chatMessages.appendChild(thinkingDiv);

                        // Make API call
                        const response = await fetch('/chat', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify({
                                message: '',
                                tip: currentTip,
                                type: chatType
                            })
                        });

                        const data = await response.json();
                        
                        // Remove thinking message
                        const thinkingMessage = document.getElementById('thinking-message');
                        if (thinkingMessage) {
                            thinkingMessage.remove();
                        }

                        // Add response
                        const messageDiv = document.createElement('div');
                        messageDiv.classList.add('message', 'bot-message');
                        messageDiv.innerHTML = convertMarkdownToHtml(data.response);
                        chatMessages.appendChild(messageDiv);
                        chatMessages.scrollTop = chatMessages.scrollHeight;

                        processedTips.add(tipId);
                    } catch (error) {
                        console.error('Error:', error);
                        const errorDiv = document.createElement('div');
                        errorDiv.classList.add('message', 'bot-message');
                        errorDiv.textContent = 'Sorry, there was an error processing your request.';
                        chatMessages.appendChild(errorDiv);
                    } finally {
                        isProcessing = false;
                    }
                }
            };

            card.addEventListener('click', handler);
        });

        // Handle follow-up questions
        async function sendMessage(message) {
            if (!message.trim() || isProcessing) return;

            try {
                isProcessing = true;
                
                // Add user message
                const userDiv = document.createElement('div');
                userDiv.classList.add('message', 'user-message');
                userDiv.textContent = message;
                chatMessages.appendChild(userDiv);

                // Create bot message div
                const botDiv = document.createElement('div');
                botDiv.classList.add('message', 'bot-message');
                chatMessages.appendChild(botDiv);

                // Set up EventSource for streaming
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        message: message,
                        tip: currentTip,
                        type: chatType
                    })
                });

                const reader = response.body.getReader();
                const decoder = new TextDecoder();
                let accumulatedResponse = '';

                while (true) {
                    const {value, done} = await reader.read();
                    if (done) break;
                    
                    const chunk = decoder.decode(value);
                    const lines = chunk.split('\n');
                    
                    for (const line of lines) {
                        if (line.startsWith('data: ')) {
                            try {
                                const data = JSON.parse(line.slice(6));
                                accumulatedResponse += data.chunk;
                                botDiv.innerHTML = convertMarkdownToHtml(accumulatedResponse);
                                chatMessages.scrollTop = chatMessages.scrollHeight;
                            } catch (e) {
                                console.error('Error parsing SSE data:', e);
                            }
                        }
                    }
                }

                if (accumulatedResponse.includes("cannot respond to any more comments")) {
                    chatInput.disabled = true;
                    sendButton.disabled = true;
                }

            } catch (error) {
                console.error('Error:', error);
                const errorDiv = document.createElement('div');
                errorDiv.classList.add('message', 'bot-message');
                errorDiv.textContent = 'Sorry, there was an error processing your request.';
                chatMessages.appendChild(errorDiv);
            } finally {
                isProcessing = false;
            }
        }

        // Close chat
        closeChat.addEventListener('click', () => {
            chatContainer.style.display = 'none';
        });

        // Send message handlers
        sendButton.addEventListener('click', () => {
            const message = chatInput.value;
            if (message) {
                sendMessage(message);
                chatInput.value = '';
            }
        });

        chatInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                const message = chatInput.value;
                if (message) {
                    sendMessage(message);
                    chatInput.value = '';
                }
            }
        });
    }

    // Add image checking functionality if we're on the home page
    const dailyImage = document.getElementById('daily-image');
    if (dailyImage) {
        console.log('Initializing image generation process...');
        
        // First, trigger image generation
        fetch('/generate_image')
            .then(response => response.json())
            .then(data => {
                console.log('Image generation response:', data);
                if (data.image_url && !data.image_url.includes('placeholder.com')) {
                    dailyImage.src = data.image_url;
                }
            })
            .catch(error => console.error('Error generating image:', error));

        function checkImage() {
            console.log('Checking for image update...');
            fetch('/check_image')
                .then(response => response.json())
                .then(data => {
                    console.log('Image check response:', data);
                    if (data.image_url && 
                        !data.image_url.includes('placeholder.com') && 
                        data.image_url !== dailyImage.src) {
                        console.log('Updating image to:', data.image_url);
                        dailyImage.src = data.image_url;
                        return true;
                    }
                    return false;
                })
                .catch(error => console.error('Error checking image:', error));
        }

        // Check more frequently initially
        let checkCount = 0;
        const imageCheck = setInterval(() => {
            if (checkCount < 12) { // First minute: every 5 seconds
                checkImage();
            } else {
                console.log('Stopping image checks');
                clearInterval(imageCheck);
            }
            checkCount++;
        }, 5000);
    }

    // Add this function to handle basic Markdown conversion
    function convertMarkdownToHtml(text) {
        // Convert headers (### and ####)
        text = text.replace(/### (.*?)(\n|$)/g, '<h3>$1</h3>');
        text = text.replace(/#### (.*?)(\n|$)/g, '<h4>$1</h4>');
        
        // Convert bold text
        text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
        
        // Convert numbered lists with bold numbers when followed by bold text
        text = text.replace(/(\d+)\. \*\*(.*?)(\n|$)/g, '<div class="list-item"><strong>$1.</strong> <strong>$2</strong></div>');
        text = text.replace(/(\d+)\. (.*?)(\n|$)/g, '<div class="list-item">$1. $2</div>');
        
        // Convert line breaks
        text = text.replace(/\n\n/g, '<br>');
        
        return text;
    }

    // Then modify how we add messages to use innerHTML instead of textContent
    function addMessage(message, type) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', `${type}-message`);
        messageDiv.innerHTML = convertMarkdownToHtml(message);
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});
