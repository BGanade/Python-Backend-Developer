import os #import the os module to use the system command
restaurant = ['Pizza', 'Burger', 'Sushi'] #List of restaurants

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
    os.system('cls')
    print('Ending the application\n')  

def invalid_option(): #Show an invalid option message
    print('Invalid option!\n')
    input('Press enter to continue...')
    main()

def register_restaurant(): #Register a restaurant
    os.system('cls')
    print('Registration of new restaurants\n')
    restaurant_name = input('Enter the restaurant name you want to register: ')
    restaurant.append(restaurant_name)
    print(f'The restaurant {restaurant_name} was registered successfully!\n')
    input('Press enter to go back to the main menu...')
    main()

def list_restaurants(): #List the restaurants
    os.system('cls')
    print('List of registered restaurants\n')
    for i, restaurant_name in enumerate(restaurant, start=1):
        print(f'{i}. {restaurant_name}')
    input('Press enter to go back to the main menu...')
    main()

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
                active_restaurants()
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
    