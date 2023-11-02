from flask import Flask, render_template, redirect, request
app = Flask(__name__)
app.secret_key = 'secret'

#things that will move
from user import User


@app.route("/users")
def Read():
    all_users = User.get_all()
    return render_template("Read.html", all_users = all_users)


@app.route("/users/new")
def new_user():
   return render_template("Create.html")

@app.route("/create_user", methods=['POST'])
def create_user():
   User.create_one(request.form)
   return redirect("/users")



#end of the moving content
if __name__ == "__main__":
    app.run(debug=True)

