"""
multi-line string
"""

movies = []


def menu():
    user_input = input("a: add movie, l: list movies, f: find movie:  ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies()
        elif user_input == 'f':
            find_movie()
        else:
            print('Unknown command')

        user_input = input("a: add movie, l: list movies, f: find movie:  ")


def add_movie():
    name = input('Title: ')
    year = int(input('Year: '))
    movies.append({
        'name': name,
        'year': year
    })
    print(f"\nAdded movie: '{name}' from {year}")


def show_movies():
    for movie in movies:
        show_movie_details(movie)


def show_movie_details(movie):
    print(f"Title: '{movie['name']}', Year: {movie['year']}")


def find_movie():
    search_criteria = input("Search for Title - name, Year - year: ")
    search_value = input("What value you are looking for: ")

    if search_criteria == 'year':
        search_value = int(search_value)

    search_result = find_by_attribute(search_value, lambda m: m[search_criteria])

    print(f"Found {len(search_result)} movies matching search criteria")
    for movie in search_result:
        show_movie_details(movie)


def find_by_attribute(expected_value, finder):
    search_result = []

    for movie in movies:
        if finder(movie) == expected_value:
            search_result.append(movie)

    return search_result


menu()
