import sqlite3
import os

def get_db_path():
    return 'instance/tips.db'

def init_db():
    os.makedirs('instance', exist_ok=True)
    conn = sqlite3.connect(get_db_path())
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS tips (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tip TEXT NOT NULL,
            category TEXT NOT NULL,
            last_shown DATE
        )
    ''')
    
    conn.commit()
    conn.close()

def get_random_tip(category):
    conn = sqlite3.connect(get_db_path())
    c = conn.cursor()
    
    # Get a random tip that hasn't been shown recently
    c.execute('''
        SELECT tip FROM tips 
        WHERE category = ? 
        AND last_shown IS NULL
        ORDER BY RANDOM() 
        LIMIT 1
    ''', (category,))
    
    result = c.fetchone()
    
    if result:
        # Update last_shown date
        c.execute('''
            UPDATE tips 
            SET last_shown = date('now')
            WHERE tip = ?
        ''', (result[0],))
        conn.commit()
        tip = result[0]
    else:
        # If all tips have been shown, reset last_shown dates and try again
        c.execute('''
            UPDATE tips 
            SET last_shown = NULL 
            WHERE category = ?
        ''', (category,))
        conn.commit()
        
        # Get a random tip
        c.execute('''
            SELECT tip FROM tips 
            WHERE category = ? 
            ORDER BY RANDOM() 
            LIMIT 1
        ''', (category,))
        result = c.fetchone()
        if result:
            tip = result[0]
        else:
            # Default tips if nothing is found in the database
            defaults = {
                'parenting': "Remember to spend quality time with your children every day. One day you will miss it.",
                'nutrition': "Try to eat a balanced diet with plenty of protein, fiber, and limited simple sugars and carbohydrates."
            }
            tip = defaults.get(category, f"Default {category} tip")
    
    conn.close()
    return tip

if __name__ == '__main__':
    init_db() 