from datetime import datetime, date

QUOTES = [
    {
        "quote": "The greatest wealth is health.",
        "author": "Virgil",
        "year": -19,
        "category": "health"
    },
    {
        "quote": "To keep the body in good health is a duty... otherwise we shall not be able to keep our mind strong and clear.",
        "author": "Buddha",
        "year": -500,
        "category": "health"
    },
    {
        "quote": "It is health that is real wealth and not pieces of gold and silver.",
        "author": "Mahatma Gandhi",
        "year": 1930,
        "category": "health"
    },
    {
        "quote": "A good laugh and a long sleep are the best cures in the doctor’s book.",
        "author": "Irish Proverb",
        "year": None,
        "category": "health"
    },
    {
        "quote": "Exercise is a celebration of what your body can do. Not a punishment for what you ate.",
        "author": "Anonymous",
        "year": None,
        "category": "fitness"
    },
    {
        "quote": "Take care of your body. It’s the only place you have to live.",
        "author": "Jim Rohn",
        "year": 1980,
        "category": "fitness"
    },
    {
        "quote": "Walking is man's best medicine.",
        "author": "Hippocrates",
        "year": -400,
        "category": "fitness"
    },
    {
        "quote": "What we achieve inwardly will change outer reality.",
        "author": "Plutarch",
        "year": 100,
        "category": "mindfulness"
    },
    {
        "quote": "Yoga is the journey of the self, through the self, to the self.",
        "author": "Bhagavad Gita",
        "year": -200,
        "category": "yoga"
    },
    {
        "quote": "In the middle of difficulty lies opportunity.",
        "author": "Albert Einstein",
        "year": 1940,
        "category": "inspiration"
    },
    {
        "quote": "Children are not things to be molded, but are people to be unfolded.",
        "author": "Jess Lair",
        "year": 1970,
        "category": "parenting"
    },
    {
        "quote": "The way we talk to our children becomes their inner voice.",
        "author": "Peggy O'Mara",
        "year": 1986,
        "category": "parenting"
    },
    {
        "quote": "It takes a village to raise a child.",
        "author": "African Proverb",
        "year": None,
        "category": "parenting"
    },
    {
        "quote": "Your children will see what you're all about by what you live rather than what you say.",
        "author": "Wayne Dyer",
        "year": 2000,
        "category": "parenting"
    },
    {
        "quote": "Health is the greatest possession. Contentment is the greatest treasure. Confidence is the greatest friend.",
        "author": "Lao Tzu",
        "year": -500,
        "category": "health"
    },
    {
        "quote": "An early-morning walk is a blessing for the whole day.",
        "author": "Henry David Thoreau",
        "year": 1854,
        "category": "fitness"
    },
    {
        "quote": "The groundwork for all happiness is good health.",
        "author": "Leigh Hunt",
        "year": 1820,
        "category": "health"
    },
    {
        "quote": "He who has health has hope, and he who has hope has everything.",
        "author": "Arabian Proverb",
        "year": None,
        "category": "health"
    },
    {
        "quote": "A fit body, a calm mind, a house full of love. These things cannot be bought – they must be earned.",
        "author": "Naval Ravikant",
        "year": 2018,
        "category": "fitness"
    },
    {
        "quote": "You don’t have to be extreme, just consistent.",
        "author": "Anonymous",
        "year": None,
        "category": "fitness"
    },
    {
        "quote": "Yoga does not just change the way we see things, it transforms the person who sees.",
        "author": "B.K.S. Iyengar",
        "year": 1975,
        "category": "yoga"
    },
    {
        "quote": "Calm mind brings inner strength and self-confidence, so that's very important for good health.",
        "author": "Dalai Lama",
        "year": 2000,
        "category": "mindfulness"
    },
    {
        "quote": "Nature does not hurry, yet everything is accomplished.",
        "author": "Lao Tzu",
        "year": -500,
        "category": "mindfulness"
    },
    {
        "quote": "Hiking is not for the body, but for the soul.",
        "author": "Anonymous",
        "year": None,
        "category": "hiking"
    },
    {
        "quote": "In every walk with nature, one receives far more than he seeks.",
        "author": "John Muir",
        "year": 1901,
        "category": "hiking"
    },
    {
        "quote": "Parenting is not about perfect behavior. It’s about perfect love.",
        "author": "Anonymous",
        "year": None,
        "category": "parenting"
    },
    {
        "quote": "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
        "author": "Benjamin Franklin",
        "year": 1750,
        "category": "parenting"
    },
    {
        "quote": "The best way to make children good is to make them happy.",
        "author": "Oscar Wilde",
        "year": 1880,
        "category": "parenting"
    },
    {
        "quote": "Friendship is born at that moment when one person says to another, ‘What! You too? I thought I was the only one.’",
        "author": "C.S. Lewis",
        "year": 1960,
        "category": "relationships"
    },
    {
        "quote": "Happiness is only real when shared.",
        "author": "Christopher McCandless",
        "year": 1992,
        "category": "relationships"
    },
    {
        "quote": "In the sweetness of friendship let there be laughter, and sharing of pleasures.",
        "author": "Khalil Gibran",
        "year": 1923,
        "category": "relationships"
    },
    {
        "quote": "Alone we can do so little; together we can do so much.",
        "author": "Helen Keller",
        "year": 1921,
        "category": "relationships"
    },
    {
        "quote": "Medicine is a science of uncertainty and an art of probability.",
        "author": "William Osler",
        "year": 1906,
        "category": "medicine"
    },
    {
        "quote": "Wherever the art of medicine is loved, there is also a love of humanity.",
        "author": "Hippocrates",
        "year": -400,
        "category": "medicine"
    },
    {
        "quote": "Prevention is better than cure.",
        "author": "Desiderius Erasmus",
        "year": 1500,
        "category": "medicine"
    },
    {
        "quote": "Doctors put a wall up between themselves and their patients; nurses broke it down.",
        "author": "Jodi Picoult",
        "year": 1999,
        "category": "medicine"
    },
    {
        "quote": "You must be the change you wish to see in the world.",
        "author": "Mahatma Gandhi",
        "year": 1913,
        "category": "global health"
    },
    {
        "quote": "The health of the people is really the foundation upon which all their happiness and all their powers as a state depend.",
        "author": "Benjamin Disraeli",
        "year": 1877,
        "category": "global health"
    },
    {
        "quote": "The true meaning of life is to plant trees, under whose shade you do not expect to sit.",
        "author": "Nelson Henderson",
        "year": 1950,
        "category": "global health"
    },
    {
        "quote": "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.",
        "author": "Buddha",
        "year": -500,
        "category": "mindfulness"
    },
    {
        "quote": "It always seems impossible until it’s done.",
        "author": "Nelson Mandela",
        "year": 2001,
        "category": "inspiration"
    },
    {
        "quote": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs",
        "year": 2005,
        "category": "inspiration"
    },
    {
        "quote": "Not all those who wander are lost.",
        "author": "J.R.R. Tolkien",
        "year": 1954,
        "category": "inspiration"
    },
    {
        "quote": "Happiness depends upon ourselves.",
        "author": "Aristotle",
        "year": -350,
        "category": "mindfulness"
    },
    {
        "quote": "In the middle of every difficulty lies opportunity.",
        "author": "Albert Einstein",
        "year": 1940,
        "category": "inspiration"
    },
    {
        "quote": "Happiness is not something ready-made. It comes from your own actions.",
        "author": "Dalai Lama",
        "year": 2000,
        "category": "mindfulness"
    },
    {
        "quote": "Life is what happens when you’re busy making other plans.",
        "author": "John Lennon",
        "year": 1980,
        "category": "inspiration"
    },
    {
        "quote": "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "author": "Winston Churchill",
        "year": 1941,
        "category": "inspiration"
    },
    {
        "quote": "Don’t count the days, make the days count.",
        "author": "Muhammad Ali",
        "year": 1974,
        "category": "inspiration"
    },
    {
        "quote": "You miss 100% of the shots you don’t take.",
        "author": "Wayne Gretzky",
        "year": 1983,
        "category": "inspiration"
    },
    {
        "quote": "It is not how much we have, but how much we enjoy, that makes happiness.",
        "author": "Charles Spurgeon",
        "year": 1860,
        "category": "mindfulness"
    },
    {
        "quote": "Spread love everywhere you go. Let no one ever come to you without leaving happier.",
        "author": "Mother Teresa",
        "year": 1979,
        "category": "relationships"
    },
    {
        "quote": "The best way to find yourself is to lose yourself in the service of others.",
        "author": "Mahatma Gandhi",
        "year": 1914,
        "category": "global health"
    },
    {
        "quote": "A journey of a thousand miles begins with a single step.",
        "author": "Lao Tzu",
        "year": -500,
        "category": "inspiration"
    },
    {
        "quote": "You can’t go back and change the beginning, but you can start where you are and change the ending.",
        "author": "C.S. Lewis",
        "year": 1940,
        "category": "inspiration"
    },
    {
        "quote": "Do what you can, with what you have, where you are.",
        "author": "Theodore Roosevelt",
        "year": 1901,
        "category": "inspiration"
    },
    {
        "quote": "Education is the most powerful weapon which you can use to change the world.",
        "author": "Nelson Mandela",
        "year": 1994,
        "category": "global health"
    },
    {
        "quote": "It takes a long time to grow an old friend.",
        "author": "John Leonard",
        "year": 1960,
        "category": "relationships"
    },
    {
        "quote": "The best way out is always through.",
        "author": "Robert Frost",
        "year": 1915,
        "category": "inspiration"
    },
    {
        "quote": "Happiness is when what you think, what you say, and what you do are in harmony.",
        "author": "Mahatma Gandhi",
        "year": 1925,
        "category": "mindfulness"
    },
    {
        "quote": "Life isn’t about waiting for the storm to pass. It’s about learning to dance in the rain.",
        "author": "Vivian Greene",
        "year": 2006,
        "category": "inspiration"
    },
    {
        "quote": "Act as if what you do makes a difference. It does.",
        "author": "William James",
        "year": 1890,
        "category": "inspiration"
    },
    {
        "quote": "Keep your face always toward the sunshine—and shadows will fall behind you.",
        "author": "Walt Whitman",
        "year": 1855,
        "category": "inspiration"
    },
    {
        "quote": "Health is the soul that animates all the enjoyments of life, which fade and are tasteless without it.",
        "author": "Lucius Annaeus Seneca",
        "year": 50,
        "category": "health"
    },
    {
        "quote": "The future depends on what you do today.",
        "author": "Mahatma Gandhi",
        "year": 1947,
        "category": "inspiration"
    },
    {
        "quote": "If you want to go fast, go alone. If you want to go far, go together.",
        "author": "African Proverb",
        "year": None,
        "category": "relationships"
    },
    {
        "quote": "Do not go where the path may lead, go instead where there is no path and leave a trail.",
        "author": "Ralph Waldo Emerson",
        "year": 1841,
        "category": "inspiration"
    },
    {
        "quote": "To love and be loved is to feel the sun from both sides.",
        "author": "David Viscott",
        "year": 1989,
        "category": "relationships"
    },
    {
        "quote": "The purpose of our lives is to be happy.",
        "author": "Dalai Lama",
        "year": 2000,
        "category": "mindfulness"
    },
    {
        "quote": "Knowing yourself is the beginning of all wisdom.",
        "author": "Aristotle",
        "year": -350,
        "category": "mindfulness"
    },
    {
        "quote": "The secret of getting ahead is getting started.",
        "author": "Mark Twain",
        "year": 1890,
        "category": "inspiration"
    },
    {
        "quote": "We are what we repeatedly do. Excellence, then, is not an act, but a habit.",
        "author": "Aristotle",
        "year": -350,
        "category": "inspiration"
    },
    {
        "quote": "The best preparation for tomorrow is doing your best today.",
        "author": "H. Jackson Brown Jr.",
        "year": 1993,
        "category": "inspiration"
    },
    {
        "quote": "No one can make you feel inferior without your consent.",
        "author": "Eleanor Roosevelt",
        "year": 1935,
        "category": "inspiration"
    },
    {
        "quote": "What lies behind us and what lies before us are tiny matters compared to what lies within us.",
        "author": "Ralph Waldo Emerson",
        "year": 1841,
        "category": "inspiration"
    },
    {
        "quote": "Kind words can be short and easy to speak, but their echoes are truly endless.",
        "author": "Mother Teresa",
        "year": 1975,
        "category": "relationships"
    },
    {
        "quote": "The greatest gift of life is friendship, and I have received it.",
        "author": "Hubert H. Humphrey",
        "year": 1965,
        "category": "relationships"
    },
    {
        "quote": "Happiness is a direction, not a place.",
        "author": "Sydney J. Harris",
        "year": 1951,
        "category": "mindfulness"
    },
    {
        "quote": "Do small things with great love.",
        "author": "Mother Teresa",
        "year": 1950,
        "category": "relationships"
    },
    {
        "quote": "Every child is an artist. The problem is how to remain an artist once we grow up.",
        "author": "Pablo Picasso",
        "year": 1954,
        "category": "parenting"
    },
    {
        "quote": "A mother’s love for her child is like nothing else in the world.",
        "author": "Agatha Christie",
        "year": 1930,
        "category": "parenting"
    },
    {
        "quote": "It’s not what we have in life but who we have in our life that matters.",
        "author": "Unknown",
        "year": None,
        "category": "relationships"
    },
    {
        "quote": "The good physician treats the disease; the great physician treats the patient who has the disease.",
        "author": "William Osler",
        "year": 1910,
        "category": "medicine"
    },
    {
        "quote": "A good laugh is sunshine in the house.",
        "author": "William Makepeace Thackeray",
        "year": 1847,
        "category": "mindfulness"
    },
    {
        "quote": "We don’t inherit the earth from our ancestors, we borrow it from our children.",
        "author": "Native American Proverb",
        "year": None,
        "category": "global health"
    },
    {
        "quote": "You are never too old to set another goal or to dream a new dream.",
        "author": "C.S. Lewis",
        "year": 1940,
        "category": "inspiration"
    },
    {
        "quote": "Success usually comes to those who are too busy to be looking for it.",
        "author": "Henry David Thoreau",
        "year": 1854,
        "category": "inspiration"
    },
    {
        "quote": "If you want to lift yourself up, lift up someone else.",
        "author": "Booker T. Washington",
        "year": 1901,
        "category": "relationships"
    },
    {
        "quote": "He who opens a school door, closes a prison.",
        "author": "Victor Hugo",
        "year": 1862,
        "category": "global health"
    },
    {
        "quote": "Everything has beauty, but not everyone sees it.",
        "author": "Confucius",
        "year": -500,
        "category": "mindfulness"
    },
    {
        "quote": "Do what you feel in your heart to be right – for you’ll be criticized anyway.",
        "author": "Eleanor Roosevelt",
        "year": 1935,
        "category": "inspiration"
    },
    {
        "quote": "The most beautiful things in the world cannot be seen or even touched. They must be felt with the heart.",
        "author": "Helen Keller",
        "year": 1921,
        "category": "relationships"
    },
    {
        "quote": "There is no charm equal to tenderness of heart.",
        "author": "Jane Austen",
        "year": 1813,
        "category": "relationships"
    },
    {
        "quote": "You don’t have to control your thoughts. You just have to stop letting them control you.",
        "author": "Dan Millman",
        "year": 1980,
        "category": "mindfulness"
    },
    {
        "quote": "Your time is limited, so don’t waste it living someone else’s life.",
        "author": "Steve Jobs",
        "year": 2005,
        "category": "inspiration"
    },
    {
        "quote": "The most wasted of days is one without laughter.",
        "author": "E.E. Cummings",
        "year": 1950,
        "category": "mindfulness"
    },
    {
        "quote": "Love and compassion are necessities, not luxuries. Without them humanity cannot survive.",
        "author": "Dalai Lama",
        "year": 1989,
        "category": "relationships"
    },
    {
        "quote": "A doctor should be a father to the poor and mother to the rich.",
        "author": "Charaka",
        "year": -200,
        "category": "medicine"
    },
    {
        "quote": "Start where you are. Use what you have. Do what you can.",
        "author": "Arthur Ashe",
        "year": 1975,
        "category": "inspiration"
    },
    {
        "quote": "What you get by achieving your goals is not as important as what you become by achieving your goals.",
        "author": "Zig Ziglar",
        "year": 1970,
        "category": "inspiration"
    },
    {
        "quote": "The mind is everything. What you think you become.",
        "author": "Buddha",
        "year": -500,
        "category": "mindfulness"
    },
    {
        "quote": "The difference between a successful person and others is not a lack of strength, not a lack of knowledge, but rather a lack in will.",
        "author": "Vince Lombardi",
        "year": 1960,
        "category": "inspiration"
    },
    {
        "quote": "Believe you can and you’re halfway there.",
        "author": "Theodore Roosevelt",
        "year": 1903,
        "category": "inspiration"
    },
    {
        "quote": "The only limit to our realization of tomorrow will be our doubts of today.",
        "author": "Franklin D. Roosevelt",
        "year": 1939,
        "category": "inspiration"
    },
    {
        "quote": "Do not go gentle into that good night. Rage, rage against the dying of the light.",
        "author": "Dylan Thomas",
        "year": 1951,
        "category": "inspiration"
    },
    {
        "quote": "Do what you love, and the money will follow.",
        "author": "Marsha Sinetar",
        "year": 1987,
        "category": "inspiration"
    },
    {
        "quote": "Turn your wounds into wisdom.",
        "author": "Oprah Winfrey",
        "year": 2000,
        "category": "inspiration"
    },
    {
        "quote": "He who has a why to live can bear almost any how.",
        "author": "Friedrich Nietzsche",
        "year": 1889,
        "category": "inspiration"
    },
    {
        "quote": "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work.",
        "author": "Steve Jobs",
        "year": 2005,
        "category": "inspiration"
    },
    {
        "quote": "Do not wait to strike till the iron is hot; but make it hot by striking.",
        "author": "William Butler Yeats",
        "year": 1921,
        "category": "inspiration"
    },
    {
        "quote": "Opportunity is missed by most people because it is dressed in overalls and looks like work.",
        "author": "Thomas Edison",
        "year": 1925,
        "category": "inspiration"
    },
    {
        "quote": "The best revenge is massive success.",
        "author": "Frank Sinatra",
        "year": 1955,
        "category": "inspiration"
    },
    {
        "quote": "I have not failed. I've just found 10,000 ways that won't work.",
        "author": "Thomas Edison",
        "year": 1925,
        "category": "inspiration"
    },
    {
        "quote": "Success is how high you bounce when you hit bottom.",
        "author": "George S. Patton",
        "year": 1944,
        "category": "inspiration"
    },
    {
        "quote": "Fall seven times and stand up eight.",
        "author": "Japanese Proverb",
        "year": None,
        "category": "inspiration"
    },
    {
        "quote": "Happiness is not by chance, but by choice.",
        "author": "Jim Rohn",
        "year": 1970,
        "category": "mindfulness"
    },
    {
        "quote": "Success is getting what you want. Happiness is wanting what you get.",
        "author": "Dale Carnegie",
        "year": 1936,
        "category": "mindfulness"
    },
    {
        "quote": "Courage doesn’t always roar. Sometimes courage is the quiet voice at the end of the day saying, ‘I will try again tomorrow.’",
        "author": "Mary Anne Radmacher",
        "year": 1995,
        "category": "inspiration"
    },
    {
        "quote": "Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart.",
        "author": "Roy T. Bennett",
        "year": 2016,
        "category": "inspiration"
    },
    {
        "quote": "Every moment is a fresh beginning.",
        "author": "T.S. Eliot",
        "year": 1920,
        "category": "mindfulness"
    },
    {
        "quote": "The road to success and the road to failure are almost exactly the same.",
        "author": "Colin R. Davis",
        "year": 1980,
        "category": "inspiration"
    },
    {
        "quote": "Don't spend time beating on a wall, hoping to transform it into a door.",
        "author": "Coco Chanel",
        "year": 1954,
        "category": "inspiration"
    },
    {
        "quote": "The future belongs to those who believe in the beauty of their dreams.",
        "author": "Eleanor Roosevelt",
        "year": 1935,
        "category": "inspiration"
    },
    {
        "quote": "It does not matter how slowly you go as long as you do not stop.",
        "author": "Confucius",
        "year": -500,
        "category": "inspiration"
    },
    {
        "quote": "Everything you’ve ever wanted is on the other side of fear.",
        "author": "George Addair",
        "year": 1971,
        "category": "inspiration"
    },
    {
        "quote": "Dream big and dare to fail.",
        "author": "Norman Vaughan",
        "year": 1991,
        "category": "inspiration"
    },
    {
        "quote": "Do one thing every day that scares you.",
        "author": "Eleanor Roosevelt",
        "year": 1940,
        "category": "inspiration"
    },
        {
        "quote": "Success is not how high you have climbed, but how you make a positive difference to the world.",
        "author": "Roy T. Bennett",
        "year": 2016,
        "category": "inspiration"
    },
    {
        "quote": "Go confidently in the direction of your dreams. Live the life you have imagined.",
        "author": "Henry David Thoreau",
        "year": 1854,
        "category": "inspiration"
    },
    {
        "quote": "What we think, we become.",
        "author": "Buddha",
        "year": -500,
        "category": "mindfulness"
    },
    {
        "quote": "The way to get started is to quit talking and begin doing.",
        "author": "Walt Disney",
        "year": 1950,
        "category": "inspiration"
    },
    {
        "quote": "You are never too old to set another goal or to dream a new dream.",
        "author": "C.S. Lewis",
        "year": 1940,
        "category": "inspiration"
    },
    {
        "quote": "It is never too late to be what you might have been.",
        "author": "George Eliot",
        "year": 1869,
        "category": "inspiration"
    },
    {
        "quote": "Don’t let the noise of others’ opinions drown out your own inner voice.",
        "author": "Steve Jobs",
        "year": 2005,
        "category": "inspiration"
    },
    {
        "quote": "Keep your face always toward the sunshine—and shadows will fall behind you.",
        "author": "Walt Whitman",
        "year": 1855,
        "category": "inspiration"
    },
    {
        "quote": "Happiness is not a goal... it's a by-product of a life well-lived.",
        "author": "Eleanor Roosevelt",
        "year": 1941,
        "category": "mindfulness"
    },
    {
        "quote": "Do not wait for the perfect moment, take the moment and make it perfect.",
        "author": "Zoey Sayward",
        "year": 2010,
        "category": "mindfulness"
    },
    {
        "quote": "Don’t let yesterday take up too much of today.",
        "author": "Will Rogers",
        "year": 1935,
        "category": "inspiration"
    },
    {
        "quote": "Your present circumstances don’t determine where you can go; they merely determine where you start.",
        "author": "Nido Qubein",
        "year": 1985,
        "category": "inspiration"
    },
    {
        "quote": "We may encounter many defeats but we must not be defeated.",
        "author": "Maya Angelou",
        "year": 1978,
        "category": "inspiration"
    },
    {
        "quote": "Happiness often sneaks in through a door you didn’t know you left open.",
        "author": "John Barrymore",
        "year": 1930,
        "category": "mindfulness"
    },
    {
        "quote": "Be yourself; everyone else is already taken.",
        "author": "Oscar Wilde",
        "year": 1890,
        "category": "inspiration"
    },
    {
        "quote": "In three words I can sum up everything I've learned about life: It goes on.",
        "author": "Robert Frost",
        "year": 1923,
        "category": "inspiration"
    },
    {
        "quote": "Change your thoughts and you change your world.",
        "author": "Norman Vincent Peale",
        "year": 1952,
        "category": "mindfulness"
    },
    {
        "quote": "Don’t gain the world and lose your soul; wisdom is better than silver or gold.",
        "author": "Bob Marley",
        "year": 1977,
        "category": "mindfulness"
    },
    {
        "quote": "Do not fear failure but rather fear not trying.",
        "author": "Roy T. Bennett",
        "year": 2016,
        "category": "inspiration"
    },
    {
        "quote": "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.",
        "author": "Albert Schweitzer",
        "year": 1952,
        "category": "inspiration"
    },
    {
        "quote": "Happiness is not something ready-made. It comes from your own actions.",
        "author": "Dalai Lama",
        "year": 2000,
        "category": "mindfulness"
    },
    {
        "quote": "Perfection is not attainable, but if we chase perfection we can catch excellence.",
        "author": "Vince Lombardi",
        "year": 1961,
        "category": "inspiration"
    },
    {
        "quote": "Start where you are. Use what you have. Do what you can.",
        "author": "Arthur Ashe",
        "year": 1975,
        "category": "inspiration"
    },
    {
        "quote": "Hardships often prepare ordinary people for an extraordinary destiny.",
        "author": "C.S. Lewis",
        "year": 1940,
        "category": "inspiration"
    },
    {
        "quote": "Do not anticipate trouble, or worry about what may never happen. Keep in the sunlight.",
        "author": "Benjamin Franklin",
        "year": 1750,
        "category": "mindfulness"
    },
    {
        "quote": "To succeed in life, you need two things: ignorance and confidence.",
        "author": "Mark Twain",
        "year": 1895,
        "category": "inspiration"
    },
    {
        "quote": "Happiness depends upon ourselves.",
        "author": "Aristotle",
        "year": -350,
        "category": "mindfulness"
    },
    {
        "quote": "Do not let what you cannot do interfere with what you can do.",
        "author": "John Wooden",
        "year": 1963,
        "category": "inspiration"
    },
    {
        "quote": "You only live once, but if you do it right, once is enough.",
        "author": "Mae West",
        "year": 1937,
        "category": "mindfulness"
    },
    {
        "quote": "Act as if what you do makes a difference. It does.",
        "author": "William James",
        "year": 1890,
        "category": "inspiration"
    },
     {
        "quote": "Perfection is not attainable, but if we chase perfection we can catch excellence.",
        "author": "Vince Lombardi",
        "year": 1960,
        "category": "inspiration"
    },
    {
        "quote": "Life is 10% what happens to us and 90% how we react to it.",
        "author": "Charles R. Swindoll",
        "year": 1982,
        "category": "mindfulness"
    },
    {
        "quote": "What you get by achieving your goals is not as important as what you become by achieving your goals.",
        "author": "Zig Ziglar",
        "year": 1970,
        "category": "inspiration"
    },
    {
        "quote": "Be yourself; everyone else is already taken.",
        "author": "Oscar Wilde",
        "year": 1888,
        "category": "inspiration"
    },
    {
        "quote": "Act as if what you do makes a difference. It does.",
        "author": "William James",
        "year": 1890,
        "category": "inspiration"
    },
    {
        "quote": "Success is not how high you have climbed, but how you make a positive difference to the world.",
        "author": "Roy T. Bennett",
        "year": 2015,
        "category": "inspiration"
    },
    {
        "quote": "Happiness is the highest form of health.",
        "author": "Dalai Lama",
        "year": 2000,
        "category": "health"
    },
    {
        "quote": "Keep your vitality. A life without health is like a river without water.",
        "author": "Maxime Lagacé",
        "year": 2016,
        "category": "health"
    },
    {
        "quote": "Your body hears everything your mind says.",
        "author": "Naomi Judd",
        "year": 1990,
        "category": "health"
    },
    {
        "quote": "Take care of your body, it’s the only place you have to live.",
        "author": "Jim Rohn",
        "year": 1970,
        "category": "health"
    },
    {
        "quote": "If you have good thoughts, they will shine out of your face like sunbeams and you will always look lovely.",
        "author": "Roald Dahl",
        "year": 1980,
        "category": "mindfulness"
    },
    {
        "quote": "To enjoy the glow of good health, you must exercise.",
        "author": "Gene Tunney",
        "year": 1925,
        "category": "fitness"
    },
    {
        "quote": "Reading is to the mind what exercise is to the body.",
        "author": "Joseph Addison",
        "year": 1712,
        "category": "mindfulness"
    },
    {
        "quote": "A year from now you may wish you had started today.",
        "author": "Karen Lamb",
        "year": 1977,
        "category": "inspiration"
    },
    {
        "quote": "Don’t wait. The time will never be just right.",
        "author": "Napoleon Hill",
        "year": 1937,
        "category": "inspiration"
    },
    {
        "quote": "The pain you feel today will be the strength you feel tomorrow.",
        "author": "Anonymous",
        "year": None,
        "category": "fitness"
    },
    {
        "quote": "Motivation is what gets you started. Habit is what keeps you going.",
        "author": "Jim Ryun",
        "year": 1970,
        "category": "fitness"
    },
    {
        "quote": "You have to expect things of yourself before you can do them.",
        "author": "Michael Jordan",
        "year": 1994,
        "category": "inspiration"
    },
    {
        "quote": "The difference between try and triumph is a little ‘umph.’",
        "author": "Marvin Phillips",
        "year": 1980,
        "category": "inspiration"
    },
    {
        "quote": "Don’t stop when you’re tired. Stop when you’re done.",
        "author": "Wesley Snipes",
        "year": 1997,
        "category": "fitness"
    },
    {
        "quote": "Strength doesn’t come from what you can do. It comes from overcoming the things you once thought you couldn’t.",
        "author": "Rikki Rogers",
        "year": 2010,
        "category": "fitness"
    },
    {
        "quote": "The greatest wealth is health.",
        "author": "Virgil",
        "year": -19,
        "category": "health"
    },
    {
        "quote": "A journey of a thousand miles begins with a single step.",
        "author": "Lao Tzu",
        "year": -500,
        "category": "inspiration"
    },
    {
        "quote": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs",
        "year": 2005,
        "category": "inspiration"
    },
    {
        "quote": "Fall seven times, stand up eight.",
        "author": "Japanese Proverb",
        "year": None,
        "category": "inspiration"
    },
    {
        "quote": "Our greatest glory is not in never falling, but in rising every time we fall.",
        "author": "Confucius",
        "year": -500,
        "category": "inspiration"
    },
    {
        "quote": "Do what you can with all you have, wherever you are.",
        "author": "Theodore Roosevelt",
        "year": 1901,
        "category": "inspiration"
    },
    {
        "quote": "The secret of getting ahead is getting started.",
        "author": "Mark Twain",
        "year": 1890,
        "category": "inspiration"
    },
    {
        "quote": "Life begins at the end of your comfort zone.",
        "author": "Neale Donald Walsch",
        "year": 2007,
        "category": "inspiration"
    }
]

def get_quote_for_date(target_date=None):
    """Get quote for a specific date, defaulting to today"""
    if target_date is None:
        target_date = date.today()
        
    # Use January 1, 2024 as the start date
    start_date = date(2024, 1, 1)
    days_elapsed = (target_date - start_date).days
    
    # Use modulo to cycle through the quotes list
    quote_index = days_elapsed % len(QUOTES)
    return QUOTES[quote_index]

def get_daily_quote():
    """Get today's quote"""
    return get_quote_for_date()

def preview_future_quotes(days=7):
    """Preview quotes for the next X days"""
    today = date.today()
    future_quotes = []
    for i in range(days):
        future_date = date.fromordinal(today.toordinal() + i)
        quote = get_quote_for_date(future_date)
        future_quotes.append({
            'date': future_date.strftime('%Y-%m-%d'),
            'quote': quote
        })
    return future_quotes

def get_quotes_by_category(category):
    """Get all quotes for a specific category"""
    return [q for q in QUOTES if q['category'].lower() == category.lower()]

# Example usage:
if __name__ == '__main__':
    # Get today's quote
    today_quote = get_daily_quote()
    print(f"Today's quote: {today_quote['quote']} - {today_quote['author']}")
    
    # Preview next week's quotes
    print("\nNext week's quotes:")
    for item in preview_future_quotes(7):
        print(f"{item['date']}: {item['quote']['quote']}") 