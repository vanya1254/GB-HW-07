def main_menu() -> int:   
    print('\nMain menu:')     
    menu_list = ['Open file',
                 'Save file',
                 'Show all contacts',
                 'Create contact',
                 'Change contact',
                 'Remove contact',
                 'Close'
                ]
    
    for i in range(len(menu_list)):
        print(f'\t{i + 1}. {menu_list[i]}')
    user_input = int(input('\nEnter command => '))
    
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
        print('\nBook opened')
        return True
    else:
        print('\nBook empty or not open')
        return False


def exit_program():
    print('\nThe end of program')
    exit()
    
    
def create_contact():
    print('\nCreate new contact.')
    new_contact =  dict()
    
    new_contact['lastname'] = input(f'\tEnter lastname => ')
    new_contact['firstname'] = input(f'\tEnter name => ')
    new_contact['phone'] = input(f'\tEnter phone => ')
    new_contact['comment'] = input(f'\tEnter comment => ')
    
    print('\nDo not forget to save!')

    return new_contact


def change_contact(db: list):
    print('\nChange contact.')
    
    user_choice = int(input('\nEnter number of contact => ')) - 1
    db[user_choice]['lastname'] = input(f'\tEnter new lastname => ')
    db[user_choice]['firstname'] = input(f'\tEnter new name => ')
    db[user_choice]['phone'] = input(f'\tEnter new phone => ')
    db[user_choice]['comment'] = input(f'\tEnter new comment => ')
    
    print('\nDo not forget to save!')


def remove_contact(db: list):
    user_choice = int(input('\nEnter number of contact => ')) - 1
    check = input('Are you sure? (yes="y", no="n") => ')
    if check == 'y':
        del db[user_choice]
        print('\nDo not forget to save!')
    elif check == 'n':
        pass


# def input_data():
#   while True:
#   try:
#       num = float(input('Введите число: '))
#       if type(num) == float:
#           return num
#   except:
#       print('Вы ввели не число.')