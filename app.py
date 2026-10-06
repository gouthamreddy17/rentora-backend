from database.connection import DatabaseConnection
from flask import Flask,jsonify,request

from database.query import *

from flask_cors import CORS


app=Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "hello"

@app.route('/signup',methods=['POST'])
def signup():
    data=request.get_json()
    name=data.get('name')
    email=data.get('email')
    phone=data.get('phone')
    city=data.get('city')
    password=data.get('password')
    confirm_password=data.get('confirm_password')
    
    if password!=confirm_password:
        return jsonify({
            'message':"password not matching"
            
        }),409
    result=get_email_from_db(email)
    print("email",result)
    if result:
        return jsonify({
            'message':"email already registerd"
        }),409
    record=insert_user_to_db(name,email,password,phone,city)
    print(record)
    if record==True:
        return jsonify({
            'message':'registration sussessfull'
        }),201
    return jsonify({
        'message': "registration failed"
    }),500
@app.route('/login',methods=['POST'])
def login():
    data=request.get_json()
    email=data.get('email')
    password=data.get('password')
    result=get_user_by_email(email)
    if not result:
        return jsonify({
            'message':'Email not registerd'
        }),401
    if result['password']!=password:
        return jsonify({
            'message':'password is inncorrect'
        }),401
    return jsonify({
        'message':'login sucessfull','user':{
            'user_id':result['user_id'],
            'name':result['name'],
            'email':result['email'],
            'role':result['role']
        }
    }),200
    
@app.route('/items')
def items():
    result=get_items_from_db()
    return jsonify(result)
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)