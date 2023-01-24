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
            show_contact(get_db())
        case 4:
            show_all(get_db())
        case 5:
            set_db(create_contact())
        case 6:
            change_contact(get_db())
        case 7:
            remove_contact(get_db())
        case 8:
            exit_program()
            

def start():
    while True:
        user_choice = main_menu()
        input_handler(user_choice)