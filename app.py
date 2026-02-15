from flask import Flask, request,url_for, redirect,session,Response
app = Flask(__name__)
app.secret_key = 'supersecret'
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == '123':
            session['username'] = username
            return redirect(url_for('welcome'))
        else:
            return Response('Invalid credentials', mimetype='text/plain')
    return '''
    <h1>Login</h1>
        <form method="POST">
            Username: <input type="text" name="username" placeholder="Username"><br>
            Password: <input type="password" name="password" placeholder="Password"><br>
            <input type="submit" value="Login">
        </form>
    ''' 
@app.route('/welcome')
def welcome():
    if 'username' in session:
        return f'''
        <h1>Welcome, {session["username"]}!</h1>
        <a href="{url_for('logout')}">Logout</a>
        
        
        '''
    return redirect(url_for('login'))
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))