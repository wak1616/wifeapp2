 #!/bin/bash
echo "Removing old databases..."
rm -f instance/quotes.db instance/tips.db

echo "Initializing quotes database..."
python3 quotes_data.py

echo "Initializing tips database..."
python3 tips_data.py

echo "Databases have been reset successfully!"