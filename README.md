Here's a `README.md` file for your project:

```markdown
# Flask To-Do List Application

This project is a simple To-Do list application built with Flask and SQLAlchemy, designed to help you manage tasks efficiently. The app uses a MySQL database to store and retrieve tasks, allowing you to add, view, and manage tasks with ease.

## Features

- Task Management: Add new tasks with a title and description.
- View Tasks: See a list of all your tasks, including their creation date.
- User-Friendly Interface: Designed with Bootstrap for a clean and intuitive user experience.
- Persistent Storage: Tasks are stored in a MySQL database, ensuring your data is saved and accessible anytime.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ShivamBaharwani/FlaskTaskManager.git
   cd FlaskTaskManager
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your MySQL database:**

   Update the `DATABASE_URI` in `flask_app.py` to match your MySQL credentials.

   ```python
   DATABASE_URI = "mysql+mysqldb://root:password@localhost/todo"
   ```

5. **Create the database tables:**

   ```bash
   python
   >>> from flask_app import db
   >>> db.create_all()
   >>> exit()
   ```

6. **Run the application:**

   ```bash
   python flask_app.py
   ```

7. **Access the application:**

   Open your browser and go to `http://localhost:7000`.

## Usage

- **Add Tasks:** Use the form on the homepage to add new tasks.
- **View Tasks:** All tasks will be displayed in a table with their creation date.
- **Manage Tasks:** Currently, tasks can be viewed. Additional features like editing and deleting can be added.

## Technologies Used

- **Flask:** A lightweight WSGI web application framework.
- **SQLAlchemy:** SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **MySQL:** An open-source relational database management system.
- **Bootstrap:** A popular CSS framework for responsive web design.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.

## License

This project is open-source and available under the [MIT License](LICENSE).
