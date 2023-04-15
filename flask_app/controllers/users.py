
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User


@app.route("/users", methods=["GET"])
def users():
    users = User.get_all()
    print(users)
    return render_template("read.html", users = users)

@app.route("/user/new", methods=["GET"])
def new():
    return render_template("create.html")

@app.route("/user/create", methods = ["POST"])
def create():
    create_user = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.create(create_user)
    return redirect("/users")

@app.route ("/user/show/<int:id>")
def show( id ):
    data = {
        "id": id
    }
    return render_template("show.html", user = User.get_one((data)))

@app.route ("/user/delete/<int:id>")
def delete( id ):
    data = {
        "id": id
    }
    User.delete_one(data)
    return redirect("/users")

@app.route ("/user/edit/<int:id>")
def edit(id):
    data = {
            "id": id
        }
    return render_template("edit.html", user = User.get_one(data))

@app.route ("/user/update", methods = ["POST"])
def update():
    User.update_one(request.form)
    return redirect("/users")