from flask import Flask, render_template, request
from datetime import datetime
from scrape import sripe_stocks, scrape_pm25

print("__name__")

app = Flask(__name__)
books = {
    1: {
        "name": "Python book",
        "price": 299,
        "image_url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/CN1/136/11/CN11361197.jpg&v=58096f9ck&w=348&h=348",
    },
    2: {
        "name": "Java book",
        "price": 399,
        "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/087/31/0010873110.jpg&v=5f7c475bk&w=348&h=348",
    },
    3: {
        "name": "C# book",
        "price": 499,
        "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/036/04/0010360466.jpg&v=62d695bak&w=348&h=348",
    },
}


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
    name = "aaa"
    # return f"<h1>Hello Flask!<br>{today}</hz1>"
    return render_template("index.html", date=today, name=name)


@app.route("/stocks")
def get_stocks():
    datas = sripe_stocks()
    return render_template("stocks.html", datas=datas)


@app.route("/books")
def show_books():
    # return books
    print(books)

    for key in books:
        print(books[key])
    return render_template("books.html", books=books)


@app.route("/bmi/name=<name>&weight=<int:weight>&height=<int:height>")
def w_bmi(name, height, weight):
    try:
        bmi = round(weight / (height / 100) ** 2, 2)
        return f"{name}的BMI:{bmi}"
    except Exception as a:
        return "輸入錯誤"


@app.route("/pm25", methods=["GET", "POST"])
def get_pm25():
    # GET
    print(request.args)
    # POST
    print(request.form)
    sort = False
    ascending = True
    today = datetime.now()
    print(today)

    if request.method == "POST":

        if "sort" in request.form:
            sort = True
            ascending = True if request.form.get("sort") == "true" else False
    columns, values = scrape_pm25(sort, ascending)
    data = {
        "columns": columns,
        "values": values,
        "today": today.strftime("%Y/%m/%d %H:%M:%S"),
    }
    return render_template("pm.html", data=data)


app.run(debug=True)
