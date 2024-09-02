from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# MySQL Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldb://root:1234@localhost/todo"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todo_table1'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    desc_todo = db.Column(db.String(2000), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

# Ensure that create_all() is run within the app context
with app.app_context():
    db.create_all()

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        title = request.form.get('title')
        desc_todo = request.form.get('desc_todo')
        
        if not title or not desc_todo:
            return "Title and Description are required!", 400
        
        try:
            todo = Todo(title=title, desc_todo=desc_todo)
            db.session.add(todo)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return f"Error adding todo: {e}", 500

    try:
        allTodo = Todo.query.all()
    except Exception as e:
        return f"Error retrieving todos: {e}", 500

    return render_template('index.html', allTodo=allTodo)

@app.route('/show')
def products():
    try:
        allTodo = Todo.query.all()
    except Exception as e:
        return f"Error retrieving todos: {e}", 500
    
    return 'This is the products page'

if __name__ == '__main__':
    app.run(debug=True, port=7000)
