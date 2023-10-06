from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
  return render_template("home.html")

@app.route("/loginpage" , methods = ["post" , "get"])
def loginpage():
    data = request.form
    print(data)
    return render_template("login.html")

@app.route("/signuppage" , methods = ["post", "get"])
def signup():
  return render_template("signup.html")

@app.route("/dashboard" , methods = ["post", "get"])
def dashboard():
  return render_template("new jobs.html")
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)