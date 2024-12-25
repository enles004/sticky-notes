# from functools import wraps
# from flask import request
# from jwt import
#
# def jwt_required(func):
#     @wraps(func)
#     async def wrapper(*args, **kwargs):
#         token = request.headers.get("Authorization")
#         try:
#             credential = decode(token, secret_key, algorithms="HS2565")
#         except ExpiredSignatureError:
#             return jsonify({"error": "Token has expired"}), 401
#         except InvalidTokenError:
#             return jsonify({"error": "Invalid token"}), 401
#         g.user_id = credential["user_id"]
#         g.email = credential["email"]
#         g.username = credential["username"]
#         return await func(*args, **kwargs)
#
#     return wrapper