from flask import Flask
from datetime import datetime

print("__name__")

app = Flask(__name__)
books = {1: "Python book", 2: "Java book", 3: "Flask book"}


@app.route("/sum/x=<x>&y=<y>")
def my_self(x, y):
    try:
        total = eval(x) + eval(y)
        return f"{x}+{y}={total}"
    except Exception as e:
        print(e)
        return f"<h2 style='color:red'>請輸入數字</h2>"


@app.route("/book/<int:id>")
def show_book(id):
    if id not in books:
        return f"<h2 style='color:red' >無此編號:{id}<h2>"
    return f"第{id}本書:{books[id]}"


@app.route("/")
def index():
    today = datetime.now()
    print(today)
    print("123")
    return f"<h1>Hello Flask!<br>{today}</hz1>"


@app.route("/books")
def show_books():
    return books


@app.route("/bmi/name=<name>&weight=<int:weight>&height=<int:height>")
def w_bmi(name, height, weight):
    try:
        bmi = round(weight / (height / 100) ** 2, 2)
        return f"{name}的BMI:{bmi}"
    except Exception as a:
        return "輸入錯誤"


app.run(debug=True)
