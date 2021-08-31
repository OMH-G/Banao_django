import sys
from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
import requests

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:password@127.0.0.1/tanmanfoundation"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Details(db.Model):
    userid=db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80),unique=True) 
    password=db.Column(db.String(80))
@app.route('/register',methods=['POST','GET'])
def register():
    if(request.form.get('pass')!='' and request.form.get('ema')!=''):       
        password=request.form.get('pass')
        email=request.form.get('ema')
        user=Details(email=email,password=password) 
        db.session.add(user)
        db.session.commit()
    return render_template('two.html',)
    # a=requests.get('http://127.0.0.1:3000/home')
    # print(a.text)
@app.route('/login',methods=['POST','GET'])
def login():
    if(request.form.get('pass')!='' and request.form.get('ema')!=''):       
        password=request.form.get('pass')
        email=request.form.get('ema')
        res=requests.get(f'http://127.0.0.1:3000/check/{email}/{password}')
        if(res.text!='No'):
            return '{ success:200}'
        else:
            return render_template('two.html')
    return render_template('one.html')
if __name__=="__main__":
    app.run(debug=True,port=5000)