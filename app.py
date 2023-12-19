from flask import Flask,render_template,request
# from flask_pymongo import PyMongo

app=Flask('__main__')
app.secret_key="secretkey"
# app.config['MONGO_URI']="mongodb://localhost:27017/Consumer_db"

# mongo=PyMongo(app)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/contactUs')
def contactFunc():
    return render_template('contact.html')

@app.route('/faq')
def faqFunc():
    return render_template('faq.html')

# @app.route('/afterContact',methods=['POST'])
# def afterContact():
#     consumer=request.form
#     name=consumer['name']
#     mobile=consumer['mobile']
#     email=consumer['email']
#     user_requirement=consumer['user_requirement']

#     if name and mobile and email and user_requirement and request.method=='POST':
#         id=mongo.db.Consumer_collection.insert_one({'name':name,'mobile':mobile,'email':email,'user_requirement':user_requirement})
#         flash('Your request has been recorded, we will get back to you shortly !','success')
#         return redirect('/')
#     else:
#         flash('Please fill in all the required fields.', 'danger')
#         return redirect('/contactUs')

if __name__=='__main__':
    app.run(debug=True)