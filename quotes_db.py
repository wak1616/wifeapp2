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
            category TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def populate_initial_quotes():
    quotes_data = [
        ("The greatest glory in living lies not in never falling, but in rising every time we fall.", "Nelson Mandela", 1994, "resilience"),
        ("Balance is not something you find, it's something you create.", "Jana Kingsford", 2015, "balance"),
        ("The power of finding beauty in the humblest things makes home happy and life lovely.", "Louisa May Alcott", 1868, "family"),
    ]
    
    conn = sqlite3.connect(get_db_path())
    c = conn.cursor()
    
    c.executemany('''
        INSERT OR IGNORE INTO quotes (quote, author, year, category)
        VALUES (?, ?, ?, ?)
    ''', quotes_data)
    
    conn.commit()
    conn.close()

def get_random_quote():
    conn = sqlite3.connect(get_db_path())
    c = conn.cursor()
    
    c.execute('''
        SELECT quote, author, year
        FROM quotes 
        ORDER BY RANDOM() 
        LIMIT 1
    ''')
    
    result = c.fetchone()
    conn.close()
    
    if result:
        return {
            'quote': result[0],
            'author': result[1],
            'year': result[2]
        }
    else:
        return {
            'quote': "Every day is a new beginning.",
            'author': "Unknown",
            'year': None
        }

if __name__ == '__main__':
    init_db()
    populate_initial_quotes() 