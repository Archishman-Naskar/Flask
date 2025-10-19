from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def welcome():
  return "Welcome To Learning Flask."

@app.route("/demo")
def demo():
  return "Welcome To Learning Flask.Creating Routes."

@app.route("/demo/html1")
def html1():
  return "<html><h1>To Intregrate HTML Just Return HTML Text</h1><br><h2>Like This.</h2></html>"

@app.route("/demo/html2")
def html2():
  return render_template("index.html")

# This is How We Can Set a Route Particular Methods
@app.route("/demo/method",methods=['GET','POST'])
def method():
  if request.method=='POST':
    name=request.form['name']
    #the submitted form will have input field with name="name" we are using that
    return f'Hello {name}'
  return render_template('form.html')

if __name__=="__main__":
  app.run(debug=True)

# debug=True -> to fecilate auto reload