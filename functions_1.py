"""Возвращает аккуратно отформатированное полное имя."""
def get_formatted_name_2(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
    
musician = get_formatted_name_2('jimi', 'hendrix')
print(musician)

musician = get_formatted_name_2('john', 'hooker', 'lee')
print(musician)

""" Returning dictionary """