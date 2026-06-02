from sqlalchemy import create_engine

# mysql
# pip install mysql-connector-python
# engine = create_engine("mysql+mysqlconnector://root:rootpassword@localhost:3308/user", echo=True)

# postgres
# sudo apt install libpq-dev
# pip install psycopg2
engine = create_engine("postgresql+psycopg2://user:password@localhost:5434/user", echo=True)



