from flask import Flask, render_template
import requests
import json

app = Flask(__name__)  # Initialize Flask app

# Function to fetch memes
def get_meme():
    try:
        url = "https://meme-api.com/gimme"
        response = json.loads(requests.get(url).text)
        meme_large = response["preview"][-2]  # Get the second largest preview image
        subreddit = response["subreddit"]

        return meme_large, subreddit
    except (KeyError, json.JSONDecodeError, requests.RequestException) as e:
        return "https://via.placeholder.com/600", "Error"

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



