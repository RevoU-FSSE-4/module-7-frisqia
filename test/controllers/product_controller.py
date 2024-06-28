from flask import request
from connectors.mysql_connector import connection
from models.product import Product
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from flask_login import current_user

from flask_jwt_extended import jwt_required

from decorators.role_checker import role_required
from cerberus import Validator
from validations.product_insert import product_insert_schema

#fetch product
@role_required('Admin')
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
# @jwt_required()
def create_product():

    v = Validator(product_insert_schema)
    request_body={
        "name":request.form['name'],
        "price":int(request.form['price']),
        "description":request.form['description']
    }
    if not v.validate(request_body):
        return {'error':v.errors},409
    
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

# #mengganti
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

# #delete product
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

