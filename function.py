from functions_1 import get_formatted_name_2

def greet_user():
    """Output simple greeting."""
    print("Good Morning")

greet_user()

def greet_user_2(username):
    print(f"hello , {username.title()}" )

greet_user_2('Nelson')    
greet_user_2('Bob') 

def describe_pat(animal_type, animal_name):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}s Name is {animal_name.title()}")

describe_pat("Dog","bob")

"""Default argument"""
def describe_pat_2(animal_type1 , last_name = "Mimi"):
    print(last_name)

describe_pat_2("Cow")

"""Возвращает аккуратно отформатированное полное имя."""
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('Luba', 'Lubava')
print(musician)

x = get_formatted_name_2('jimi1', 'hendrix1')
print(x)


