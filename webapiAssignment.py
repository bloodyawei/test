import requests

def fetch_object(film_url):
    return requests.get(film_url).json()

def search_film_species_sum(films, title):
    for film in films:
        if film['title'] == title:
            return len(film['species'])
    return title + ' is not found'

def list_film_title_sorted(films):
    sorted_films = sorted(films, key = lambda films : films['episode_id'])
    return [sorted_films[i]['title'] for i in range(len(sorted_films))]

def list_vehicle_condition(vehicles):
    return [vehicles[i] for i in range(len(vehicles)) if int(vehicles[i]['max_atmosphering_speed']) > 1000]

if __name__ == '__main__':

    # Goal 1 : How many different species appears in film-6 (Revenge of the Sith)
    response_films = fetch_object("https://swapi.dev/api/films/")
    films = response_films['results']
    print(search_film_species_sum(films, 'Revenge of the Sith'))

    # Goal 2 : Please list all the film names and sort the name by episode_id
    print(list_film_title_sorted(films))

    # Goal 3 : Please find out all vehicles which max_atmosphering_speed is over 1000
    response_vehicles = fetch_object("https://swapi.dev/api/vehicles/")
    vehicles = response_vehicles['results']
    print(list_vehicle_condition(vehicles))