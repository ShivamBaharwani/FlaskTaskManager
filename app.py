from sqlalchemy import create_engine

DATABASE_URI = "mysql+mysqldb://root:1234@localhost/todo"
engine = create_engine(DATABASE_URI)

try:
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print("Connection failed:", e)
