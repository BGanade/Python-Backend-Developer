import os

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

def chose_option(): #Choose an option
    try:
        chosed_option = int(input('Chose an option: '))
        print(f'You chose option: {chosed_option}!')  

        match chosed_option:
            case 1:
                print('Register a restaurant')
            case 2:
                print('List restaurants')
            case 3:
                print('Active restaurants')
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
    