import os #import the os module to use the system command
restaurants = [{'name' : 'Praça', 'category' : 'Japonesa', 'active': False},
              {'name' : 'Pizza Suprema', 'category' : 'Pizza', 'active': True},
              {'name' : 'Cantina', 'category' : 'Italiana', 'active': False}] #List of restaurants

def show_program_name(): #show the program name
    print("""
███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗  ███████╗██╗░░░░░░█████╗░██╗░░░██╗░█████╗░██████╗░
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝  ██╔════╝██║░░░░░██╔══██╗██║░░░██║██╔══██╗██╔══██╗
█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░  █████╗░░██║░░░░░███████║╚██╗░██╔╝██║░░██║██████╔╝
██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗  ██╔══╝░░██║░░░░░██╔══██║░╚████╔╝░██║░░██║██╔══██╗
███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝  ██║░░░░░███████╗██║░░██║░░╚██╔╝░░╚█████╔╝██║░░██║
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝\n""")

def show_options(): #show the options
    print('1. Register a restaurant')
    print('2. List restaurants')
    print('3. Active restaurants')
    print('4. exit  ')

def ending_application(): #End the application
    show_subtitle('Ending the application...')

def back_to_main_menu(): #Back to the main menu
    input('Press enter to go back to the main menu...')
    main()

def invalid_option(): #Show an invalid option message
    print('Invalid option!\n')
    back_to_main_menu()

def show_subtitle(subtitle): #Show a subtitle
    os.system('cls')
    print(f'{subtitle}\n')

def register_restaurant(): #Register a restaurant
    show_subtitle('Registration of new restaurants')
    restaurant_name = input('Enter the restaurant name you want to register: ')
    category = input(f'Enter the category of the restaurant {restaurant_name}: ')
    restaurant_data = {'name':restaurant_name, 'category': category,'active' :False }
    restaurants.append(restaurant_data)

    print(f'The restaurant {restaurant_name} was registered successfully!\n')
    back_to_main_menu()

def list_restaurants():
    show_subtitle('List of registered restaurants')

    for i, restaurant in enumerate(restaurants, start=1): #
        restaurant_name = restaurant['name']
        category = restaurant['category']
        active = restaurant['active']
        print(f'{i}. {restaurant_name} | {category} | {active}')

    back_to_main_menu()

def chose_option(): #Choose an option
    try:
        chosed_option = int(input('Chose an option: '))
        print(f'You chose option: {chosed_option}!')  

        match chosed_option:
            case 1:
                register_restaurant()
            case 2:
                list_restaurants()
            case 3:
                print('active_restaurants')
            case 4:
                ending_application()
            case _:
                invalid_option()
    except ValueError:
        invalid_option()
        return 

def main():
    os.system('cls')
    show_program_name()
    show_options()
    chose_option()

if __name__ == '__main__':
    main()
    