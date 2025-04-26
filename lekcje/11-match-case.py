light = input("Jakie widzisz światło na sygnalizatorze? ")

match light:
    case 'zielone':
        print("Możesz jechać")
    case 'żółte':
        print("przygotuj się")
    case 'czerwone':
        print("stój")
    case _:
        print("nie ściemniaj")