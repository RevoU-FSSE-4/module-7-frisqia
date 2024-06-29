# from functools import wraps
# from flask_login import current_user

# #current useruntuk mengecek informasi user yg login

# def role_required(role):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             # admin dan user peran terpisah
#             if current_user.is_authenticated and current_user.role == role:
#                 return func(*args, **kwargs)
#             else:
#                 return {"message": "Unauthorized"}, 403
#             # admin punya kekuatan lebih dari user
        
#         return wrapper
    
#     return decorator