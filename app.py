from flask import Flask

app=Flask(__name__)

@app.route("/")
def welcome():
  return "Welcome To Learning Flask."

@app.route("/demo")
def demo():
  return "Welcome To Learning Flask.Creating Routes."

if __name__=="__main__":
  app.run(debug=True)

# debug=True -> to fecilate auto reload