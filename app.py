from flask import Flask, request,url_for, redirect,session,Response, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')
@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")
    # if username == "admin" and password == "123":
    #     return render_template('welcome.html', username=username)
    valid_users = {"admin": "123", "user1": "abc", "user2": "xyz"}
    if username in valid_users and password == valid_users[username]: 
        return render_template('welcome.html', username=username)
    
    else:        
        return "Invalid credenrtials. Please try again."