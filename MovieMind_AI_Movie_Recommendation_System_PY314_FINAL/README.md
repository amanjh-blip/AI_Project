# MovieMind AI - Movie Recommendation System

A complete Flask-based AI/ML movie recommendation website.

## Features
- Modern responsive website
- Movie selection form
- TF-IDF text feature extraction
- Cosine similarity recommendation engine
- AI match percentage
- Self-contained sample movie dataset
- No external API or database required

## How to run

### 1. Install Python
Python 3.14 is supported. The project dependencies are pinned to versions with Python 3.14 wheels.

### 2. Open the project folder in VS Code

### 3. Create a virtual environment (recommended)

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Start the website
```bash
python app.py
```

### 6. Open in browser
Go to:
http://127.0.0.1:5000

## How the AI works

The recommendation engine combines each movie's genre and description into text.
TF-IDF converts this text into numerical vectors. Cosine similarity then measures
how similar the selected movie is to other movies. The top six most similar movies
are displayed as recommendations.

## Project structure

```text
movie_recommendation_system/
├── app.py
├── recommender.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Academic note

This is a mini-project prototype using a small built-in dataset. For a production
system, the dataset should be expanded and validated, and user ratings, posters,
authentication, databases, and/or external movie APIs can be added.
