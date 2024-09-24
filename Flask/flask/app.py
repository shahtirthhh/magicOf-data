from flask import Flask,render_template,request,jsonify

# Creating Web Server Gateway Interface (WSGI)
app = Flask(__name__)


# MVC method
@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/form",methods=["GET","POST"])
def products():
    if request.method == "POST":
        name=request.form['name']
        return f"Hello {name} !"
    
    return render_template("form.html")
@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score > 50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template("results.html",results = res)

# REST api
dummy = [
    {"name":"Asus ROG Strixxx","price":510},
    {"name":"Iphone 16 Pro","price":990}
]

@app.route("/api/item",methods=["GET"])
def home():
    return jsonify(dummy)


if __name__ == "__main__":
    app.run(debug=True) #debug work as Nodemon