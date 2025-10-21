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

# how can you use the data what you get from backend or frontend and use it
# we use jinja 
# no need to import or install any thing
# it works just like that
@app.route("/demo/<int:score>")
def jinja(score):
  return f'Score : {score}'

# how to render for loop
@app.route("/demo/integarteCodeInHTML/for/<int:score>")
def jinjaFor(score):
  status=""
  if score>55 :
    status="PASS"
  else :
    status="FAIL"
  arg={'Status':status,'Score':score}
  return render_template("forLoop.html",arg=arg)

# how to render if
@app.route("/demo/integarteCodeInHTML/if/<int:score>")
def jinjaif(score):
  
  return render_template("if.html",score=score)

if __name__=="__main__":
  app.run(debug=True)

# debug=True -> to fecilate auto reload