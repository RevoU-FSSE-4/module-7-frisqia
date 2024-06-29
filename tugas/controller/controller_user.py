from flask import request
from connectors.mysql_connector import connection
from models.user import User
from sqlalchemy.orm import sessionmaker

from flask_login import login_user,logout_user, login_required


#chek connection
def chek_test():
   return 'test'

#register
def register_user():
   Session = sessionmaker (connection)
   s = Session()
   s.begin()                                                                                
   try:
      NewUser = User(
         email = request.form ['email'],
         username = request.form ['username']
      )
      NewUser.set_password(request.form['password'])
      s.add(NewUser)
      s.commit()
   except Exception as e:
      s.rollback()
      return{'message': 'Fail to Register'}, 500
   return {'message': 'Register Success'}, 200
   
#login
def user_login ():
   Session = sessionmaker (connection)
   s = Session()
   s.begin()

   try:
       email = request.form ['email']
       username = s.query(User).filter(User.email == email).first()

       if username == None:
          return {"message":"User not found"},403
       
       if not username.check_password(request.form['password']):
          return{"message":"Invalid password"},403
       
       login_user(username)
       session_id = request.cookies.get('session')


       return{
          "session_id": session_id,
          "message":"Login Success"
       }, 200
   
   except Exception as e:
      s.rollback()
      return {"message": "fail login"}, 500
   
@login_required
def user_logout():
    logout_user()
    return { "message": "Success logout" }