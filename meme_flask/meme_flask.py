from flask import Flask, render_template, url_for, request, session
import sqlite3
import random

app = Flask(__name__)

# Secret key for session management
app.secret_key = 'your_secret_key_here'

# Function to get a random meme from the database
def get_random_meme(category=None):
    conn = sqlite3.connect("meme_database.db")
    cursor = conn.cursor()

    # Modify query to filter memes by category if provided
    if category:
        cursor.execute("SELECT path FROM memes WHERE category=?", (category,))
    else:
        cursor.execute("SELECT path FROM memes")  # If no category, get memes from all categories

    memes = cursor.fetchall()
    conn.close()

    return memes

@app.route("/", methods=["GET", "POST"])
def index():
    # Get category from query parameters, if any
    category = request.args.get("category", None)

    # Get all memes from the database
    memes = get_random_meme(category)

    # If there are no memes, show a placeholder
    if not memes:
        meme_pic = "placeholder.png"
    else:
        # If there's a previous meme stored in session, exclude it from the options
        last_meme = session.get('last_meme', None)

        # Filter out the last meme to avoid showing it again
        available_memes = [meme for meme in memes if meme[0] != last_meme]

        if available_memes:
            # Choose a random meme from the remaining options
            meme_pic = random.choice(available_memes)[0]
        else:
            # If all memes are the same, fall back to choosing one (though this shouldn't happen often)
            meme_pic = random.choice(memes)[0]

        # Store the current meme in session to avoid showing it again
        session['last_meme'] = meme_pic

    # Check if meme_pic already contains 'static/' and avoid repeating it
    if meme_pic.startswith('static/'):
        full_image_url = request.host_url + meme_pic  # Only append the full URL without adding 'static/' again
    else:
        full_image_url = request.host_url + "static/" + meme_pic  # Add 'static/' if it isn't present

    print(f"DEBUG: meme_pic: {meme_pic}")
    print(f"DEBUG: full_image_url: {full_image_url}")

    return render_template("index.html", meme_pic=meme_pic, full_image_url=full_image_url, subreddit="Amit's Supreme Database", category=category)

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host="0.0.0.0", port=5000, debug=True)


