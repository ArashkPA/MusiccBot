import sqlite3
conn = sqlite3.connect('songs.db')
 

c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS songs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT UNIQUE,
        file_id TEXT,
        text TEXT
    )
''')

conn.commit()
conn.close()

print("دیتابیس ساخته شد و جدول songs آماده است.")
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

