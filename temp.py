from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'
mysql = MySQL(app)

adrNo, fname, eml = "", "", ""

@app.route('/')
def rootFun():
	return render_template('/index.html')

@app.route('/index.html')
def showIndex():
	return render_template('/index.html')

@app.route('/login.html', methods = ['GET', 'POST'])
def showLogin():
    global adrNo, fname, eml
    if (request.method == 'POST') :
        details = request.form
        firstName = details['uname']
        psw = details['psw']
        email, aadharNo = "", ""

        return render_template('/afterLogin/profile.html', adhr = aadharNo, name = firstName, email = email)

    return render_template('/login.html')

@app.route('/signup.html', methods = ['GET', 'POST'])
def showSignUp():
    global adrNo, fname, eml
    if (request.method == 'POST') :
        details = request.form
        firstName = details['Firstname']
        email = details['email']
        aadharNo = details['adhar']
        psw = details['psw']

        #cur = mysql.connection.cursor()
        #cur.execute("INSERT INTO MyUsers(firstName, psw, email, aadharNo) VALUES (%s, %d, %s, %s)", (firstName, psw, email, aadharNo))
        #mysql.connection.commit()
        #cur.close()
        adrNo, eml, fname = aadharNo, email, firstName
        return render_template('/afterLogin/profile.html', adhr = aadharNo, name = firstName, email = email)

    return render_template('/signup.html')

@app.route('/contact.html')
def showContact():
    return render_template('/contact.html')

@app.route('/forgot-password.html')
def showForgorPwd():
    return render_template('/forgot-password.html')


@app.route('/afterLogin/index.html')
def showIndex1():
	return render_template('/afterLogin/index.html')

@app.route('/afterLogin/contact.html')
def showContact1():
    return render_template('/afterLogin/contact.html')

@app.route('/afterLogin/profile.html')
def profile():
    return render_template('/afterLogin/profile.html', adhr = adrNo, name = fName, email = eml)

@app.route('/afterLogin/forgot-password.html')
def showForgorPwd1():
    return render_template('/afterLogin/forgot-password.html')

@app.route('/afterLogin/directions.html')
def showDirections():
    return render_template('/afterLogin/directions.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5001)