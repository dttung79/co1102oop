from random import randint


def get_random_index(items):
    return randint(0, len(items) - 1)

def init_pizzas():
    pizza_types = ["margherita", "napoletana", "marinara"]
    pizza_prices = [6.0, 7.0, 7.5]
    extra_types = ["mushrooms", "cheese", "anchovies", "sausage"]
    extra_prices = [0.5, 1.0, 1.5, 1.8]
    print('Pizza types:')
    for i in range(len(pizza_types)):
        print(f"{i+1}. {pizza_types[i]} (${pizza_prices[i]:.2f})")
    print('Extras:')
    for i in range(len(extra_types)):
        print(f"{i+1}. {extra_types[i]} (${extra_prices[i]:.2f})")

    return pizza_types, pizza_prices, extra_types, extra_prices

def get_pizza(pizza_types, pizza_prices):
    pizza_choice = int(input('Choose a pizza type: '))
    while pizza_choice < 1 or pizza_choice > len(pizza_types):
        print('Invalid choice')
        pizza_choice = int(input('Choose a pizza type: '))
    pizza_type = pizza_types[pizza_choice-1]
    pizza_price = pizza_prices[pizza_choice-1]
    
    return pizza_type, pizza_price

def add_extras(pizza_type, pizza_price, extra_types, extra_prices):
    pizza_description = pizza_type
    
    n_extras = int(input('Enter number of extras (1-3): '))
    while n_extras < 1 or n_extras > 3:
        print('Invalid number of extras')
        n_extras = int(input('Enter number of extras (1-3): '))

    for e in range(n_extras):
        extra_choice = int(input('Choose an extra: '))
        while extra_choice < 1 or extra_choice > len(extra_types):
            print('Invalid choice')
            extra_choice = int(input('Choose an extra: '))
        extra_type = extra_types[extra_choice-1]
        if e == 0:
            pizza_description += f" with extra {extra_type}"
        else:
            pizza_description += f", {extra_type}"
        extra_price = extra_prices[extra_choice-1]
        pizza_price += extra_price
    
    return pizza_description, pizza_price


# MAIN PROGRAM
pizza_types, pizza_prices, extra_types, extra_prices = init_pizzas()
pizza_type, pizza_price = get_pizza(pizza_types, pizza_prices)
pizza_description, pizza_price = add_extras(pizza_type, pizza_price, 
                                                                extra_types, extra_prices)

print(f"You have chosen a {pizza_description} worth ${pizza_price:.2f}")