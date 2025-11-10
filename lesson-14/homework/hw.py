import json

with open('students.json', 'r') as file:
    students = json.load(file)

for student in students:
    print(f"Name: {student.get('name')}")
    print(f"Age: {student.get('age')}")
    print(f"Grade: {student.get('grade')}")
    print("-" * 20)




import requests

api_key = "a524239cf31131acf7b030252d74d687"
city = "London"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
elif response.status_code == 401:
    print("Unauthorized: API key is invalid or not yet activated.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")







import json

with open("books.json", "r") as f:
    books = json.load(f)

new_book = {"name": "Fahrenhvyh", "pages": 5000, 'genre': 'Triller'}
books.append(new_book)

with open("books.json", "w") as f:
    json.dump(books, f, indent=4) 

print("New book added successfully!")




import requests
import random

api_key = "945d2e72"

def recommend_movie_by_genre():
    genre = input("Enter a movie genre (e.g., Action, Comedy, Drama): ").strip()
    
    search_terms = ["love", "war", "hero", "life", "death", "adventure", "fun"]
    movies_list = []

    for term in search_terms:
        url = f"http://www.omdbapi.com/?apikey={api_key}&s={term}&type=movie"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data.get("Search"):
                for movie in data["Search"]:
                    # Get full movie details
                    movie_id = movie["imdbID"]
                    details_url = f"http://www.omdbapi.com/?apikey={api_key}&i={movie_id}"
                    details_response = requests.get(details_url)
                    if details_response.status_code == 200:
                        details = details_response.json()
                        movie_genres = details.get("Genre", "")
                        if genre.lower() in movie_genres.lower():
                            movies_list.append(details)
    
    if movies_list:
        recommendation = random.choice(movies_list)
        print("\n🎬 Movie Recommendation:")
        print(f"Title: {recommendation['Title']}")
        print(f"Year: {recommendation['Year']}")
        print(f"Genre: {recommendation['Genre']}")
        print(f"IMDb Rating: {recommendation['imdbRating']}")
        print(f"Plot: {recommendation['Plot']}")
    else:
        print(f"No movies found for genre '{genre}'.")

recommend_movie_by_genre()
