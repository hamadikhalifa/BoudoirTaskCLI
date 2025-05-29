from helpers import (
    create_user,
    list_users,
    update_user,
    delete_user,
    create_category,
    list_categories,
    update_category,
    delete_category,
    create_task,
    list_tasks,
    update_task,
    delete_task,
    exit_program
)

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_menu():
    print(f"""
{Colors.HEADER}{Colors.BOLD}📝 Boudoir Task CLI Menu{Colors.ENDC}
{Colors.OKBLUE}1.{Colors.ENDC} Create User
{Colors.OKBLUE}2.{Colors.ENDC} List Users
{Colors.OKBLUE}3.{Colors.ENDC} Update User
{Colors.OKBLUE}4.{Colors.ENDC} Delete User
{Colors.OKBLUE}5.{Colors.ENDC} Create Category
{Colors.OKBLUE}6.{Colors.ENDC} List Categories
{Colors.OKBLUE}7.{Colors.ENDC} Update Category
{Colors.OKBLUE}8.{Colors.ENDC} Delete Category
{Colors.OKBLUE}9.{Colors.ENDC} Create Task
{Colors.OKBLUE}10.{Colors.ENDC} List Tasks
{Colors.OKBLUE}11.{Colors.ENDC} Update Task
{Colors.OKBLUE}12.{Colors.ENDC} Delete Task
{Colors.FAIL}0.{Colors.ENDC} Exit
""")

def main():
    actions = {
        "1": create_user,
        "2": list_users,
        "3": update_user,
        "4": delete_user,
        "5": create_category,
        "6": list_categories,
        "7": update_category,
        "8": delete_category,
        "9": create_task,
        "10": list_tasks,
        "11": update_task,
        "12": delete_task,
        "0": exit_program,
    }

    while True:
        print_menu()
        choice = input(f"{Colors.BOLD}Enter your choice (0–12): {Colors.ENDC}").strip()
        action = actions.get(choice)

        if action:
            action()
        else:
            print(f"{Colors.WARNING}❌ Invalid choice. Please try again.{Colors.ENDC}")

if __name__ == "__main__":
    main()
