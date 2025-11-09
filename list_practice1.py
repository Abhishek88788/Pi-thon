size = None
list_of_movies = []
print("number of movies you watched this year")
size = int(input("enter size: "))

for i in range(size):
    list_of_movies.append(input(f"enter {1+i}movie name :"))

print("you watched these movies this year:")

print(list_of_movies)

