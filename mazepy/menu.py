from maps import get_map_names, get_map

def display_menu():
    """Display the map selection menu."""
    print("=== Maze Game Menu ===")
    map_names = get_map_names()
    for idx, name in enumerate(map_names):
        print(f"{idx + 1}. {name}")
    print("0. Exit")

def select_map():
    """Prompt the user to select a map."""
    display_menu()
    choice = input("Enter map number: ")
    if choice == "0":
        print("Exiting game...")
        return None
    try:
        index = int(choice) - 1
        return get_map(index)
    except (ValueError, IndexError):
        print("Invalid selection. Please try again.")
        return select_map()