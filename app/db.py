from pymongo import MongoClient
from werkzeug.security import generate_password_hash

client = MongoClient("mongodb+srv://<username>:<password>@hackhub.umnjxm1.mongodb.net/?retryWrites=true&w=majority&appName=HackHub")

chat_db = client.get_database("Chatapp")
users_collection = chat_db.get_collection("users")


def save_user(username, email, password):
    password_hash = generate_password_hash(password)
    users_collection.insert_one({'_id': username, 'email': email, 'password': password_hash})