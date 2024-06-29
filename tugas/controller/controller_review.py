from flask import request
from connectors.mysql_connector import connection
from models.review import Review
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
# from flask_login import current_user
# from flask_jwt_extended import jwt_required
from functools import wraps


#chek connection
def get_test():
   return 'test'

#fetchiing data
def fetch_review():
    review_query = select(Review)
    Session = sessionmaker(connection)
    with Session() as s:
        result = s.execute(review_query)
        for row in result.scalars():
            print(f'ID: {row.id}, Description: {row.description} Email: {row.email}, Rate: {row.rating}' )
        return "fetch sucsess"
    
#search data
def search_review_data():
   Session= sessionmaker(connection)
   s= Session()
   try:
    review_query = select(Review)
    search_keyword = request.args.get('query')
    if search_keyword!= None:
       review_query = review_query.where(Review.rating.like(f"%{search_keyword}%"))
       
    reviews = s.execute(review_query)
    for row in reviews.scalars():
         print(f'ID: {row.id}, Description: {row.description} Email: {row.email}, Rate: {row.rating}' )
   
   except Exception as c:
      print(c)
      return{'message':'unexpected error'}, 500
   return {'message':'sucsess fetch review data'},200