from models.restaurant import Restaurant

restaurant_square = Restaurant('square', 'gourmet')
restaurant_square.recive_review('Ganade', 10)
restaurant_square.recive_review('Jose', 8)
restaurant_square.recive_review('Joao', 8)
# restaurant_mexican = Restaurant('mexican food', 'mexican')
# restaurant_japan = Restaurant('japa', 'japan')

# restaurant_mexican.Alternate_status()


def main():
    Restaurant.list_restaurants()


if __name__ == '__main__':
    main()
