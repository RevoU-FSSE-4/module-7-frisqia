from flask import Flask
from dotenv import load_dotenv
from connectors.mysql_connector import connection
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text, select
from models.product import Product
from blueprint.route_product import product_bp

load_dotenv()

app = Flask(__name__)
app.register_blueprint(product_bp)

@app.route("/")
def hello_world():
    # insert data to product table
    # session = sessionmaker(connection)
    # with session() as s:
    #     s.execute(text("INSERT INTO product (name, price, description) VALUES ('Tas Rajut', 56000, 'Dibuat Dari kulit sapi impor')"))
    #     s.commit()

    # Insert data using SQLAlchemy Model
    # NewProduct = Product( name="Pisau Lipat" , price=600000, description="Made from Krakatau Steel")
    # Session = sessionmaker(connection)
    # with Session() as s:
    #     s.add(NewProduct)    
    #     s.commit()

# Fetch all products using ORM
    product_query = select(Product)
    Session = sessionmaker(connection)
    with Session() as s:
        result = s.execute(product_query)
        for row in result.scalars(): # scalars yaitu untuk di convert objek of product
            print(f'ID: {row.id}, Name: {row.name}')
    
    return"insert succsess"