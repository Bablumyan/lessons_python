"""Выводит описание пиццы."""
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")    
    for topping in toppings:
        print(f"- {topping}")

make_pizza(15,'pepperoni')
make_pizza(10,'mushrooms', 'green peppers', 'extra cheese')

"""Строит словарь с информацией о пользователе."""
def build_profile(a,b,c, **user_info):
    user_info["First"] = a
    user_info["Second"] = b
    user_info["Third"] = c
    return user_info

user_profile = build_profile(1, 2, 3, location ='princeton',fields = 'physics')
print(user_profile)

user_profile = build_profile(1, 2, 3, fish=["Larry", "Curly", "Moe"])
print(user_profile)
