movie = input("Enter your favourite movie: ")
with open("movie.txt", "w") as file:
    file.write(movie)
