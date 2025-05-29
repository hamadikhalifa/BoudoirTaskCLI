from models import SessionLocal, User, Category, Task


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def prompt_int(prompt_text):
    while True:
        val = input(f"{Colors.BOLD}{prompt_text}{Colors.ENDC}").strip()
        if val.isdigit():
            return int(val)
        print(f"{Colors.WARNING}Please enter a valid number.{Colors.ENDC}")



def create_user():
    session = SessionLocal()
    try:
        username = input(f"{Colors.BOLD}Enter username: {Colors.ENDC}").strip()
        email = input(f"{Colors.BOLD}Enter email: {Colors.ENDC}").strip()

        existing_user = session.query(User).filter(
            (User.username == username) | (User.email == email)
        ).first()
        if existing_user:
            print(f"{Colors.FAIL}User with that username or email already exists.{Colors.ENDC}")
            return

        new_user = User(username=username, email=email)
        session.add(new_user)
        session.commit()
        print(f"{Colors.OKGREEN}User '{username}' created successfully with ID {new_user.id}.{Colors.ENDC}")

    except Exception as e:
        print(f"{Colors.FAIL}Error creating user: {e}{Colors.ENDC}")
        session.rollback()
    finally:
        session.close()

def list_users():
    session = SessionLocal()
    try:
        users = session.query(User).all()
        if not users:
            print(f"{Colors.WARNING}No users found.{Colors.ENDC}")
            return
        print(f"{Colors.HEADER}All Users:{Colors.ENDC}")
        for user in users:
            print(f"ID: {user.id} | Username: {user.username} | Email: {user.email}")
    except Exception as e:
        print(f"{Colors.FAIL}Error fetching users: {e}{Colors.ENDC}")
    finally:
        session.close()

def update_user():
    session = SessionLocal()
    try:
        user_id = prompt_int("Enter the user ID to update: ")
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            print(f"{Colors.FAIL}User not found.{Colors.ENDC}")
            return

        print(f"Current username: {user.username}")
        new_username = input(f"{Colors.BOLD}Enter new username (leave blank to keep current): {Colors.ENDC}").strip()
        if new_username:
            user.username = new_username

        print(f"Current email: {user.email}")
        new_email = input(f"{Colors.BOLD}Enter new email (leave blank to keep current): {Colors.ENDC}").strip()
        if new_email:
            user.email = new_email

        session.commit()
        print(f"{Colors.OKGREEN}User ID {user_id} updated successfully.{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Error updating user: {e}{Colors.ENDC}")
        session.rollback()
    finally:
        session.close()

def delete_user():
    session = SessionLocal()
    try:
        user_id = prompt_int("Enter the user ID to delete: ")
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            print(f"{Colors.FAIL}User not found.{Colors.ENDC}")
            return

        confirm = input(f"{Colors.WARNING}Are you sure you want to delete user '{user.username}'? (y/n): {Colors.ENDC}").strip().lower()
        if confirm == "y":
            session.delete(user)
            session.commit()
            print(f"{Colors.OKGREEN}User ID {user_id} deleted successfully.{Colors.ENDC}")
        else:
            print(f"{Colors.OKBLUE}Deletion cancelled.{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Error deleting user: {e}{Colors.ENDC}")
        session.rollback()
    finally:
        session.close()




def create_category():
    session = SessionLocal()
    try:
        name = input(f"{Colors.BOLD}Enter category name: {Colors.ENDC}").strip()
        user_id = prompt_int("Enter user ID for this category: ")

        user = session.query(User).get(user_id)
        if not user:
            print(f"{Colors.FAIL}User not found.{Colors.ENDC}")
            return

        category = Category(name=name, user=user)
        session.add(category)
        session.commit()
        print(f"{Colors.OKGREEN}Category '{name}' created with ID {category.id}.{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Error creating category: {e}{Colors.ENDC}")
        session.rollback()
    finally:
        session.close()

def list_categories():
    session = SessionLocal()
    try:
        categories = session.query(Category).all()
        if not categories:
            print(f"{Colors.WARNING}No categories found.{Colors.ENDC}")
            return
        print(f"{Colors.HEADER}Categories:{Colors.ENDC}")
        for c in categories:
            print(f"ID: {c.id} | Name: {c.name} | User ID: {c.user_id}")
    except Exception as e:
        print(f"{Colors.FAIL}Error listing categories: {e}{Colors.ENDC}")
    finally:
        session.close()

def update_category():
    session = SessionLocal()
    try:
        category_id = prompt_int("Enter the category ID to update: ")
        category = session.query(Category).filter(Category.id == category_id).first()
        if not category:
            print(f"{Colors.FAIL}Category not found.{Colors.ENDC}")
            return

        print(f"Current name: {category.name}")
        new_name = input(f"{Colors.BOLD}Enter new category name (leave blank to keep current): {Colors.ENDC}").strip()
        if new_name:
            category.name = new_name

        session.commit()
        print(f"{Colors.OKGREEN}Category ID {category_id} updated successfully.{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Error updating category: {e}{Colors.ENDC}")
        session.rollback()
    finally:
        session.close()

def delete_category():
    session = SessionLocal()
    try:
        category_id = prompt_int("Enter the category ID to delete: ")
        category = session.query(Category).filter(Category.id == category_id).first()
        if not category:
            print(f"{Colors.FAIL}Category not found.{Colors.ENDC}")
            return

        confirm = input(f"{Colors.WARNING}Are you sure you want to delete category '{category.name}'? (y/n): {Colors.ENDC}").strip().lower()
        if confirm == "y":
            session.delete(category)
            session.commit()
            print(f"{Colors.OKGREEN}Category ID {category_id} deleted successfully.{Colors.ENDC}")
        else:
            print(f"{Colors.OKBLUE}Deletion cancelled.{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Error deleting category: {e}{Colors.ENDC}")
        session.rollback()
    finally:
        session.close()



def create_task():
    session = SessionLocal()
    try:
        title = input(f"{Colors.BOLD}Enter task title: {Colors.ENDC}").strip()
        description = input(f"{Colors.BOLD}Enter task description: {Colors.ENDC}").strip()
        user_id = prompt_int("Enter user ID for this task: ")
        category_id = prompt_int("Enter category ID for this task: ")

        user = session.query(User).get(user_id)
        category = session.query(Category).get(category_id)

        if not user:
            print(f"{Colors.FAIL}User not found.{Colors.ENDC}")
            return
        if not category:
            print(f"{Colors.FAIL}Category not found.{Colors.ENDC}")
            return

        task = Task(title=title, description=description, user=user, category=category)
        session.add(task)
        session.commit()
        print(f"{Colors.OKGREEN}Task '{title}' created with ID {task.id}.{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Error creating task: {e}{Colors.ENDC}")
        session.rollback()
    finally:
        session.close()

def list_tasks():
    session = SessionLocal()
    try:
        tasks = session.query(Task).all()
        if not tasks:
            print(f"{Colors.WARNING}No tasks found.{Colors.ENDC}")
            return
        print(f"{Colors.HEADER}Tasks:{Colors.ENDC}")
        for t in tasks:
            print(f"ID: {t.id} | Title: {t.title} | User ID: {t.user_id} | Category ID: {t.category_id}")
    except Exception as e:
        print(f"{Colors.FAIL}Error listing tasks: {e}{Colors.ENDC}")
    finally:
        session.close()

def update_task():
    session = SessionLocal()
    try:
        task_id = prompt_int("Enter the task ID to update: ")
        task = session.query(Task).filter(Task.id == task_id).first()
        if not task:
            print(f"{Colors.FAIL}Task not found.{Colors.ENDC}")
            return

        print(f"Current title: {task.title}")
        new_title = input(f"{Colors.BOLD}Enter new task title (leave blank to keep current): {Colors.ENDC}").strip()
        if new_title:
            task.title = new_title

        print(f"Current description: {task.description}")
        new_description = input(f"{Colors.BOLD}Enter new description (leave blank to keep current): {Colors.ENDC}").strip()
        if new_description:
            task.description = new_description

        session.commit()
        print(f"{Colors.OKGREEN}Task ID {task_id} updated successfully.{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Error updating task: {e}{Colors.ENDC}")
        session.rollback()
    finally:
        session.close()

def delete_task():
    session = SessionLocal()
    try:
        task_id = prompt_int("Enter the task ID to delete: ")
        task = session.query(Task).filter(Task.id == task_id).first()
        if not task:
            print(f"{Colors.FAIL}Task not found.{Colors.ENDC}")
            return

        confirm = input(f"{Colors.WARNING}Are you sure you want to delete task '{task.title}'? (y/n): {Colors.ENDC}").strip().lower()
        if confirm == "y":
            session.delete(task)
            session.commit()
            print(f"{Colors.OKGREEN}Task ID {task_id} deleted successfully.{Colors.ENDC}")
        else:
            print(f"{Colors.OKBLUE}Deletion cancelled.{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Error deleting task: {e}{Colors.ENDC}")
        session.rollback()
    finally:
        session.close()



def exit_program():
    print(f"{Colors.OKGREEN}Goodbye!{Colors.ENDC}")
    exit()
