# Meme Generator 🎨😂

A Flask-based web app that allows users to generate and view memes. It also supports automated deployment using Docker, Docker Compose, and Jenkins CI/CD.

## 📁 Project Structure

```
.
├── meme_flask/              # Main Flask app directory
├── Dockerfile               # Docker image for the app
├── Jenkinsfile              # Jenkins pipeline for CI/CD
├── docker-compose.yml       # Docker Compose setup
├── init_db.py               # Script to initialize the SQLite database
├── meme_database.db         # Pre-existing SQLite database
├── requirements.txt         # Python dependencies
└── web.py                   # Entrypoint for running the Flask app
```

## 🚀 Features

- 🖼️ Meme generation and display  
- 🧠 Simple SQLite backend to store meme info  
- 🔥 Flask-based web server  
- 🐳 Docker and Docker Compose support  
- ⚙️ Jenkins pipeline for automated deployment  

## 🛠️ Setup & Usage

### Option 1: Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Meme_Generator.git
   cd Meme_Generator
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Initialize the database (optional if already exists):
   ```bash
   python init_db.py
   ```

4. Run the app:
   ```bash
   python web.py
   ```

5. Visit `http://localhost:5000` in your browser.

---

### Option 2: Run with Docker Compose

```bash
docker-compose up --build
```

The app will be available at `http://localhost:5000`.

---

### Option 3: Deploy with Jenkins

Ensure Jenkins is installed and has Docker and Git plugins enabled. Use the `Jenkinsfile` in this repo to set up a pipeline that:

- Pulls the latest code  
- Builds the Docker image  
- Deploys the updated container  

## 🧠 Tech Stack

- Python 3  
- Flask  
- SQLite  
- Docker  
- Docker Compose  
- Jenkins  


