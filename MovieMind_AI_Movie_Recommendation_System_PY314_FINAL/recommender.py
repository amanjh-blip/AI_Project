from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Self-contained movie dataset. No external download or pandas is required.
MOVIES = [
    {"title":"Inception","genre":"Sci-Fi Thriller","description":"A skilled thief enters dreams and steals secrets while facing a difficult mission involving layered dreams."},
    {"title":"Interstellar","genre":"Sci-Fi Adventure Drama","description":"Explorers travel through space and time to search for a new home for humanity and save Earth."},
    {"title":"The Matrix","genre":"Sci-Fi Action","description":"A hacker discovers that reality is an artificial simulation and joins a rebellion against intelligent machines."},
    {"title":"Avatar","genre":"Sci-Fi Adventure Fantasy","description":"A former marine enters an alien world and becomes involved in a conflict between humans and the native people."},
    {"title":"The Martian","genre":"Sci-Fi Adventure Drama","description":"An astronaut stranded on Mars uses science, engineering and determination to survive until rescue."},
    {"title":"Gravity","genre":"Sci-Fi Thriller Drama","description":"Two astronauts struggle to survive after an accident leaves them stranded in space."},
    {"title":"Jurassic Park","genre":"Sci-Fi Adventure Thriller","description":"Visitors at a dinosaur theme park face chaos when genetically engineered dinosaurs escape."},
    {"title":"Avengers: Endgame","genre":"Action Adventure Sci-Fi","description":"Superheroes unite for a final mission to undo a devastating event and restore the universe."},
    {"title":"The Dark Knight","genre":"Action Crime Drama","description":"Batman faces a dangerous criminal mastermind who creates chaos across Gotham City."},
    {"title":"Iron Man","genre":"Action Adventure Sci-Fi","description":"A billionaire inventor builds advanced armor and becomes a superhero while confronting dangerous enemies."},
    {"title":"Spider-Man: Into the Spider-Verse","genre":"Animation Action Adventure","description":"A young hero discovers other versions of Spider-Man and learns to become a superhero."},
    {"title":"Guardians of the Galaxy","genre":"Action Adventure Comedy Sci-Fi","description":"A group of unlikely heroes joins together to protect the galaxy from a powerful threat."},
    {"title":"Titanic","genre":"Romance Drama","description":"A young couple from different social backgrounds fall in love aboard a famous ocean liner."},
    {"title":"The Notebook","genre":"Romance Drama","description":"A timeless love story follows two people whose relationship survives separation and changing circumstances."},
    {"title":"La La Land","genre":"Romance Musical Drama","description":"An aspiring actress and a jazz musician pursue their dreams while falling in love in Los Angeles."},
    {"title":"Forrest Gump","genre":"Drama Romance Comedy","description":"A kind-hearted man experiences major moments in American history while holding onto his love and optimism."},
    {"title":"The Shawshank Redemption","genre":"Drama","description":"A wrongly imprisoned man develops hope and friendship while finding a way to reclaim his freedom."},
    {"title":"The Pursuit of Happyness","genre":"Drama Biography","description":"A struggling father works tirelessly to build a better life for himself and his young son."},
    {"title":"3 Idiots","genre":"Comedy Drama","description":"Three engineering students navigate friendship, pressure, education and the search for their true passions."},
    {"title":"Zindagi Na Milegi Dobara","genre":"Adventure Comedy Drama","description":"Three friends take a road trip through Spain and rediscover friendship, courage and life."},
    {"title":"Dangal","genre":"Biography Drama Sport","description":"A determined father trains his daughters to become successful wrestlers despite social obstacles."},
    {"title":"Taare Zameen Par","genre":"Drama Family","description":"A teacher helps a misunderstood child discover his creativity and overcome difficulties at school."},
    {"title":"PK","genre":"Comedy Drama Sci-Fi","description":"An innocent alien stranded on Earth questions social customs and searches for a way home."},
    {"title":"Drishyam","genre":"Crime Drama Thriller","description":"A family man uses careful planning to protect his family after a dangerous incident."},
]

FEATURE_TEXT = [
    movie["genre"] + " " + movie["description"]
    for movie in MOVIES
]

VECTORIZER = TfidfVectorizer(stop_words="english")
FEATURE_MATRIX = VECTORIZER.fit_transform(FEATURE_TEXT)
SIMILARITY_MATRIX = cosine_similarity(FEATURE_MATRIX)

def get_movie_titles():
    return [movie["title"] for movie in MOVIES]

def get_recommendations(title, n=6):
    if not title:
        return []

    idx = next(
        (i for i, movie in enumerate(MOVIES)
         if movie["title"].lower() == title.lower()),
        None
    )

    if idx is None:
        return []

    scores = sorted(
        enumerate(SIMILARITY_MATRIX[idx]),
        key=lambda x: x[1],
        reverse=True
    )

    results = []
    for movie_idx, score in scores[1:n + 1]:
        movie = MOVIES[movie_idx]
        results.append({
            "title": movie["title"],
            "genre": movie["genre"],
            "description": movie["description"],
            "score": round(float(score) * 100, 1)
        })

    return results
