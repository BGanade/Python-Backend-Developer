from models.restaurant import Restaurant
from models.menu.drinks import Drinks
from models.menu.dish import Dish

restaurant_square = Restaurant('square', 'gourmet')
juice_drink = Drinks('Watermelon', 5.0, '500ml')
juice_drink.apply_discount()
bread_dish = Dish('Bread', 2.00, 'The best Bread of the city')
bread_dish.apply_discount()
restaurant_square.add_to_menu(juice_drink)
restaurant_square.add_to_menu(bread_dish)


def main():
    restaurant_square.show_menu


if __name__ == '__main__':
    main()
