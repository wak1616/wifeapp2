import sqlite3
import os

def get_db_path():
    return 'instance/quotes.db'

def init_db():
    # Create instance directory if it doesn't exist
    os.makedirs('instance', exist_ok=True)
    conn = sqlite3.connect(get_db_path())
    c = conn.cursor()
    
    # Create quotes table only
    c.execute('''
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quote TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER,
            category TEXT,
            last_shown DATE
        )
    ''')
    
    conn.commit()
    conn.close()

def get_random_quote():
    conn = sqlite3.connect(get_db_path())
    c = conn.cursor()
    
    # Get a random quote that hasn't been shown recently
    c.execute('''
        SELECT quote, author, year 
        FROM quotes 
        WHERE last_shown IS NULL
        ORDER BY RANDOM() 
        LIMIT 1
    ''')
    
    result = c.fetchone()
    
    if result:
        # Update last_shown date
        c.execute('''
            UPDATE quotes 
            SET last_shown = date('now')
            WHERE quote = ?
        ''', (result[0],))
        conn.commit()
        quote_data = {
            'quote': result[0],
            'author': result[1],
            'year': result[2]
        }
    else:
        # If all quotes have been shown, reset last_shown dates and try again
        c.execute('UPDATE quotes SET last_shown = NULL')
        conn.commit()
        
        # Get a random quote
        c.execute('SELECT quote, author, year FROM quotes ORDER BY RANDOM() LIMIT 1')
        result = c.fetchone()
        if result:
            quote_data = {
                'quote': result[0],
                'author': result[1],
                'year': result[2]
            }
        else:
            quote_data = {
                'quote': "Every day is a new beginning.",
                'author': "Unknown",
                'year': None
            }
    
    conn.close()
    return quote_data

if __name__ == '__main__':
    init_db() 