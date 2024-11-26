from flask import Flask, render_template
import requests
import json
from pymongo import MongoClient
import os

app = Flask(__name__)  # Initialize Flask app

# MongoDB configuration
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/meme_db")  # Use environment variable or default
client = MongoClient(mongo_uri)  # Connect to MongoDB
db = client.get_database()  # Get the database (e.g., meme_db)
memes_collection = db["memes"]  # Use or create a collection called 'memes'

# Function to fetch memes
def get_meme():
    try:
        url = "https://meme-api.com/gimme"
        response = json.loads(requests.get(url).text)
        meme_large = response["preview"][-2]  # Get the second largest preview image
        subreddit = response["subreddit"]

        # Save meme to MongoDB
        memes_collection.insert_one({
            "meme_url": meme_large,
            "subreddit": subreddit
        })

        return meme_large, subreddit
    except (KeyError, json.JSONDecodeError, requests.RequestException) as e:
        return "https://via.placeholder.com/600", "Error"

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


