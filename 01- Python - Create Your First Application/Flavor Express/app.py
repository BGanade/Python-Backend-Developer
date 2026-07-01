import os  # import the os module to use the system command
restaurants = [{'name': 'Praça', 'category': 'Japonesa', 'active': False},
               {'name': 'Pizza Suprema', 'category': 'Pizza', 'active': True},
               # List of restaurants
               {'name': 'Cantina', 'category': 'Italiana', 'active': False}]


def show_program_name():
    """Display the application's name as ASCII art.

    Prints the program's banner in the terminal when the application
    starts.
    """
    print("""
███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗  ███████╗██╗░░░░░░█████╗░██╗░░░██╗░█████╗░██████╗░
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝  ██╔════╝██║░░░░░██╔══██╗██║░░░██║██╔══██╗██╔══██╗
█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░  █████╗░░██║░░░░░███████║╚██╗░██╔╝██║░░██║██████╔╝
██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗  ██╔══╝░░██║░░░░░██╔══██║░╚████╔╝░██║░░██║██╔══██╗
███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝  ██║░░░░░███████╗██║░░██║░░╚██╔╝░░╚█████╔╝██║░░██║
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
""")


def show_options():
    """Display the main menu options.

    Prints the available options that the user can choose from
    to interact with the application.
    """
    print('1. Register a restaurant')
    print('2. List restaurants')
    print('3. Toggle restaurant status')
    print('4. Exit')


def ending_application():
    """Display the application shutdown message.

    Shows a subtitle indicating that the application is being closed.
    """
    show_subtitle('Ending the application...')


def back_to_main_menu():
    """Return to the main menu.

    Waits for the user to press Enter before calling the main
    function to display the application's main menu.
    """
    input('Press Enter to go back to the main menu...')
    main()


def invalid_option():
    """Display an invalid option message.

    Informs the user that the selected option is invalid and
    returns to the application's main menu.
    """
    print('Invalid option!\n')
    back_to_main_menu()


def show_subtitle(subtitle):
    """Display a formatted subtitle in the terminal.

    Clears the terminal screen and prints the provided subtitle
    surrounded by lines of asterisks for better visual formatting.

    Args:
        subtitle: The text to be displayed as the subtitle.
    """
    os.system('cls')
    line = '*' * len(subtitle)
    print(f'{line}\n{subtitle}\n{line}\n')


def register_restaurant():  # Register a restaurant
    """Register a new restaurant in the system.

    Prompts the user to enter the restaurant's name and category,
    creates a new restaurant with the status set to inactive,
    adds it to the restaurant list, displays a success message,
    and returns to the main menu.
    """
    show_subtitle('Registration of new restaurants')
    restaurant_name = input('Enter the restaurant name you want to register: ')
    category = input(
        f'Enter the category of the restaurant {restaurant_name}: ')
    restaurant_data = {'name': restaurant_name,
                       'category': category, 'active': False}
    restaurants.append(restaurant_data)

    print(f'The restaurant {restaurant_name} was registered successfully!\n')
    back_to_main_menu()


def list_restaurants():
    """Display all registered restaurants.

    Shows a formatted list containing each restaurant's name,
    category, and activation status. After displaying the list,
    returns to the application's main menu.
    """
    show_subtitle('List of registered restaurants')

    print(f'{'Restaurant name'.ljust(22)} | {'Category'.ljust(20)} | {'Active'}')
    for i, restaurant in enumerate(restaurants, start=1):
        restaurant_name = restaurant['name']
        category = restaurant['category']
        active = 'activated' if restaurant['active'] else 'disabled'
        print(
            f'{i}.{restaurant_name.ljust(20)} | {category.ljust(20)} | {active.ljust(20)}')

    back_to_main_menu()


def toggle_restaurant_status():
    """Toggle the activation status of a restaurant.

    Prompts the user to enter a restaurant's name, searches for the restaurant in the 
    registered list, switches its activation status, displays a confirmation message, 
    and returns to the main menu. If the restaurant is not found, an error message
    is displayed instead.
    """
    show_subtitle('Toggling restaurant status')
    name_restaurant = input(
        'Enter the name of the restaurant for which you want to toggle the status: '
    )
    restaurant_found = False

    for restaurant in restaurants:
        if name_restaurant == restaurant['name']:
            restaurant_found = True
            restaurant['active'] = not restaurant['active']
            message = (
                f'The restaurant {name_restaurant} was activated successfully.'
                if restaurant['active']
                else f'The restaurant {name_restaurant} was deactivated successfully.'
            )
            print(message)

    if not restaurant_found:
        print('Restaurant not found.')

    back_to_main_menu()


def chose_option():
    """Read and process the user's menu selection.

    Prompts the user to choose an option from the main menu,
    converts the input to an integer, and calls the corresponding
    function. If the input is not a valid number or does not match
    any available option, the invalid option handler is executed.
    """
    try:
        chosed_option = int(input('Choose an option: '))
        print(f'You chose option: {chosed_option}!')

        match chosed_option:
            case 1:
                register_restaurant()
            case 2:
                list_restaurants()
            case 3:
                toggle_restaurant_status()
            case 4:
                ending_application()
            case _:
                invalid_option()
    except ValueError:
        invalid_option()
        return


def main():
    """Start the restaurant management application.

    Clears the terminal screen, displays the program banner,
    shows the main menu options, and prompts the user to
    choose an action.
    """
    os.system('cls')
    show_program_name()
    show_options()
    chose_option()


if __name__ == '__main__':
    main()
