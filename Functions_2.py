"""Using function in while loop"""
""" Input arguments should have the same name in case of calling """
"""Возвращает аккуратно отформатированное полное имя."""

def get_formatted_name(f_name, l_name):
    full_name = f"{f_name} {l_name}"
    return full_name.title()

"""
# Бесконечный цикл
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    break


formatted_name = get_formatted_name(f_name, l_name)
print(f"\nHello, {formatted_name}!")

"""
""""""
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break
"""
    first_name = f_name
    last_name = l_name
"""    
formatted_name = get_formatted_name(f_name, l_name)
print(f"\nHello, {formatted_name}!")