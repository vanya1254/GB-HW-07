from model import *
from view import *


def input_handler(inp: int):
    match inp:
        case 1:
            read_db('database.txt')
            db_success(get_db())
        case 2:
            save_db('database.txt')
        case 3:
            show_all(get_db())
        case 4:
            set_db(create_contact())
        case 5:
            change_contact(get_db())
        case 6:
            remove_contact(get_db())
        case 7:
            exit_program()
            

def start():
    while True:
        user_choice = main_menu()
        input_handler(user_choice)