import sqlite3
import os

# Path to the memes folder
memes_folder = "meme_flask/static/memes"
# Connect to SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect("meme_database.db")
cursor = conn.cursor()

# Create a table to store memes (if it doesn't exist)
cursor.execute("""
CREATE TABLE IF NOT EXISTS memes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL,
    path TEXT NOT NULL
)
""")

# Clear existing meme data (optional, useful for testing)
cursor.execute("DELETE FROM memes")

# Insert memes into the database
if os.path.exists(memes_folder):
    meme_files = [f for f in os.listdir(memes_folder) if f.endswith(('.jpg', '.png', '.jpeg', '.gif'))]
    for meme in meme_files:
        path = f"/static/memes/{meme}"  # Relative path for Flask
        cursor.execute("INSERT INTO memes (filename, path) VALUES (?, ?)", (meme, path))
        print(f"Inserted: {meme} -> {path}")
else:
    print("Memes folder not found!")

# Commit the changes and close the connection
conn.commit()
conn.close()
print("Database and memes setup completed!")
