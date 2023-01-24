def main_menu() -> int:   
    print('Main menu:')     
    menu_list = ['Show all contacts',
                 'Open file',
                 'Save file',
                 'Create contact',
                 'Change contact',
                 'Remove contact',
                 'Close'
                ]
    
    for i in range(len(menu_list)):
        print(f'\t{i + 1}. {menu_list[i]}')
    user_input = int(input('Enter command => '))
    
    return user_input
        

def show_all(db: list):
    if db_success(db):
        for i in range(len(db)):
            user_id = i + 1
            print(f'\t{user_id}', end='. ')
            for v in db[i].values():
                print(f'{v}', end=' ')
            print()
    

def db_success(db: list):
    if db:
        print('Book opened')
        return True
    else:
        print('Book empty or not open')
        return False


def exit_program():
    print('The end of program')
    exit()
    
    
def create_contact():
    print('Create new contact.')
    new_contact =  dict()
    
    new_contact['lastname'] = input(f'\tEnter lastname => ')
    new_contact['firstname'] = input(f'\tEnter name => ')
    new_contact['phone'] = input(f'\tEnter phone => ')
    new_contact['comment'] = input(f'\tEnter comment => ')

    return new_contact

# def input_data():
#   while True:
#   try:
#       num = float(input('Введите число: '))
#       if type(num) == float:
#           return num
#   except:
#       print('Вы ввели не число.')