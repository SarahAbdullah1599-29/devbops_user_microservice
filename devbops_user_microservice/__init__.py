from flask import Flask, request
from devbops_user_microservice.user_functions import Users

user = Users()
app = Flask(__name__)


@app.route('/register', methods=['POST'])
def signup():
    res = request.json
    username = res["Username"]
    password = res["Password"]
    email = res["Email"]

    firstname = res["FirstName"]
    lastname = res["LastName"]
    currentcity = res["City"]
    currentcountry = res["Country"]

    if user.verifying_email_and_user_are_available(username, currentcity, currentcountry, email, firstname, lastname,
                                                   password):

        return {
            "Result": True,
            "Error": None
        }
    else:
        return {
            "Result": False,
            "Error": "Username or email is already taken"
        }


@app.route("/login", methods=['POST'])
def login():
    res = request.json
    username = res["Username"]
    password = res["Password"]
    r = user.authincate_user(username, password)
    # return dict{}
    return r


@app.route("/delete", methods=['POST'])
def delete():
    res = request.json
    username = res["Username"]
    deleted = user.delete_user(username)
    return deleted



@app.route("/updated-pw", methods=['POST'])
def updated_pw():
    res = request.json
    username = res["Username"]
    password = res["Password"]
    updated = user.update_user_pw(username, password)
    return updated



if __name__ == "__main__":
    app.run(debug=True)
