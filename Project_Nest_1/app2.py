from flask import Flask, render_template,request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection settings
#   # Replace with your database name
client=MongoClient('mongodb://localhost:27017') 
db=client['mydb']
users_collection=db['orders']
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
   if request.method == 'POST':
       
        email = request.form['email']
        password = request.form['password']
        user_data = {
            'email': email,
            'password': password
        }
        users_collection.insert_one(user_data)
        return redirect(url_for('home'))
   return render_template('login.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/diet')
def diet():
    return render_template('diet.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/exercises')
def exercises():
    return render_template('exercises.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user_data = {
            'username': username,
            'email': email,
            'password': password
        }
        users_collection.insert_one(user_data)
        return redirect(url_for('login'))
    


    return render_template('signup.html')
@app.route('/home')
def house():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)