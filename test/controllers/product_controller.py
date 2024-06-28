from flask import request
from connectors.mysql_connector import connection
from models.product import Product
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

#fetch product
def get_product():
    Session = sessionmaker(connection)
    s = Session()
    try:
         #logic Apps
        product_query = select(Product)
        search_keyword = request.args.get('query')
        if search_keyword != None:
            product_query = product_query.where(Product.name.like(f"%{search_keyword}%"))
        products = s.execute(product_query)
        for row in products.scalars():
            print(f'ID: {row.id}, Name:{row.name}')
    except Exception as e:
        print(e)
        return {'message':'Unexpected Error'},500
    return {'message':'Success fetch product data'},200

#insert product
def create_product():
    Session = sessionmaker(connection)
    s = Session()
    s.begin()
    try:
        NewProduct = Product(
            name=request.form['name'],
            price=request.form['price'],
            description=request.form['description']
        )

        s.add(NewProduct)
        s.commit()
    except Exception as e:
        s.rollback()
        return { "message": "Fail to Insert" }, 500

    return { 'message': 'Success insert product data'}, 200

#mengganti
def update_product(id):
    Session = sessionmaker(connection)
    s = Session()
    s.begin()
    try:
        product = s.query(Product).filter(Product.id == id).first()
        product.name = request.form['name']
        product.price = request.form['price']
        product.description = request.form['description']        
        s.commit()
    except Exception as e:
        s.rollback()
        return { "message": "Fail to Update" }, 500

    return { 'message': 'Success Update product data'}, 200

#delete product
def delete_product(id):
    Session = sessionmaker(connection)
    s = Session()
    s.begin()
    try:
        product = s.query(Product).filter(Product.id == id).first()
        s.delete(product)
        s.commit()
    except Exception as e:
        s.rollback()
        return { "message": "Fail to Delete" }, 500

    return { 'message': 'Success delete product data'}, 200

