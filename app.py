from flask import Flask,render_template

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

if __name__=="__main__":
  app.run(debug=True)

# debug=True -> to fecilate auto reload