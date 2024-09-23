from flask import Flask,render_template,request

# Creating Web Server Gateway Interface (WSGI)
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/form",methods=["GET","POST"])
def products():
    if request.method == "POST":
        name=request.form['name']
        return f"Hello {name} !"
    
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True) #debug work as Nodemon