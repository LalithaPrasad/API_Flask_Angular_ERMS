import json
from flask import request
from app_package import app, db
from app_package.models import Admin

@app.route("/signup", methods=["POST"])
def create_admin():
    admin=Admin.query.get(1)
    if admin:
        return json.dumps({"message":"AdminExists"})
    else:
        data=request.get_json() or {}
        if not data:
            return json.dumps({"message":"NoData"})
        else:
            un=data['username']
            pw=data['password']
            admin=Admin(username=un)
            admin.set_password(pw)
            db.session.add(admin)
            db.session.commit()
            return json.dumps({"message":"AdminSignedup"})

@app.route("/login", methods=["GET"])
def login():
    un=request.args.get("username")
    pw=request.args.get("password")
    if not (un and pw) :
        return json.dumps({"message":"NoData"})
    else:
        admin=Admin.query.filter_by(username=un).first()
        if admin and admin.check_password(pw):
            token=admin.get_token()
            db.session.commit()
            return json.dumps({"message":"AdminExists","token":token})
        else:
            return json.dumps({"message":"AdminNotExist"})

@app.route("/logout", methods=["PUT"])
def logout():
    admin=Admin.query.get(1)
    admin.invalidate_token()
    db.session.commit()
    return json.dumps({"message":"Logged out"})
