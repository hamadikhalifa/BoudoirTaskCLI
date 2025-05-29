# BoudoirTaskCLI

**BoudoirTaskCLI** is a Python command-line task management application that allows users to manage tasks, categories, and user profiles using SQLAlchemy ORM and SQLite. It provides full CRUD operations and an interactive CLI for organizing tasks under user-specific categories.

---

## 💡 Features

- 👤 User management (create, read, update, delete)
- 🗂️ Category management assigned to users
- ✅ Task management assigned to categories and users
- 💾 Persistent storage using SQLite + SQLAlchemy ORM
- 🔄 Schema migrations using Alembic
- 🖥️ Interactive command-line interface

---

## 🛠 Technologies Used

- Python 3.11+
- SQLAlchemy
- Alembic
- Pipenv
- SQLite
- Rich (optional, for CLI output formatting)

---

## 📁 Project Structure
BoudoirTaskCLI/
│
├── alembic/ # Migration scripts
├── alembic.ini # Alembic configuration
├── cli.py # Main CLI application
├── models.py # SQLAlchemy ORM models
├── Pipfile # Pipenv dependency file
├── Pipfile.lock # Pipenv lock file
├── app.db # SQLite database (generated)
└── README.md # Project documentation


---

## 🚀 Getting Started

Follow these steps to run the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/hamadikhalifa/BoudoirTaskCLI.git
cd BoudoirTaskCLI

##  Install dependencies
pipenv install


##  Run database migrations
alembic upgrade head

## Start the CLI application
pipenv run python cli.py

## CLI Functionality Overview
Once running, you'll see a menu like:
--- BoudoirTaskCLI ---
1. Create User
2. List Users
3. Update User
4. Delete User
5. Create Category
6. List Categories
7. Update Category
8. Delete Category
9. Create Task
10. List Tasks
11. Update Task
12. Delete Task
13. Exit

## 🔧 Maintenance Commands
rm app.db                  
alembic downgrade base     
alembic upgrade 

## 👤 Author
Ekidor Evans
📍 Lodwar, Kenya
📧 ekidorevans719@gmail.com
📞 0743704815
🌐 @Boudoir Antidote Village









