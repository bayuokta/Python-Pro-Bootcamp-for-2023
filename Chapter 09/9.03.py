from rich.console import Console
console = Console()
# Nesting Dictionary in a dictionary

travel_log_dict = {
    "France": {
        "cities_visited":["Paris", "Lille", "Dijon"],
        "total_visit": 12
    },
    "Germanry": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}

# Nesting Dictionary in a List 
travel_log_list = [
    {
        "country":"France",
        "cities_visited":["Paris", "Lille", "Dijon"],
        "total_visit": 12
    },
    {
        "country":"Germanry",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
]

console.print(travel_log_dict)
console.print(travel_log_dict)