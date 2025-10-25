"""
Question: Movie Watchlist Manager

Create a Python program that:

Starts with a list of movies: ["Inception", "Avatar", "Titanic"].

Has a function to add a new movie to the list.

Has a function to remove the last movie from the list.

Uses a lambda function to print each movie in the format "Movie: <name>".

Includes a recursive function that counts the total number of letters in all movie titles combined.
"""

movies = ["Inception", "Avatar", "Titanic"]
def add_new_movie(x):
    movies.append(x)

def remove_last_movie():
    movies.pop()

show_movie = lambda name : print(f"Movie: {name}")

def count_characters(x):
    if not x:
        return 0
    else:
       return len(x[0]) + count_characters(x[1:])
    
print("movie list: ")
for x in movies:
    show_movie(x)

add_new_movie("Harry potter")
print("After adding:")
for x in movies:
    show_movie(x)

remove_last_movie()
print("After removing last element:")
for x in movies:
    show_movie(x)

count = count_characters(movies)
print("Count of characters: ", count)