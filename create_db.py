from flask_app import app, db

# Create the database and tables within the application context
with app.app_context():
    db.create_all()
    print("Database and tables created.")
