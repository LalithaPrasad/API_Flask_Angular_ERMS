import json
from bson.json_util import dumps
from flask import request
from app_package import app, db, auth
from app_package.models import Admin, Employee

@app.route("/add_employee", methods=["POST"])
@auth.valid_token
def add_employee():
    data=request.get_json() or {}
    if not data:
        return json.dumps({"message":"NoData"})
    else:
        n,a,e,r=data["name"],data["age"],data["ed"],data["role"]
        emp=Employee(name=n,age=a,ed=e,role=r)
        db.session.add(emp)
        db.session.commit()
        return json.dumps({"message":"EmployeeAdded"})

@app.route("/delete_employee", methods=["DELETE"])
@auth.valid_token
def delete_employee():
    id=request.args.get("id") or {}
    if not id:
        return json.dumps({"message":"NoData"})
    else:
        emp=Employee.query.get(int(id))
        db.session.delete(emp)
        db.session.commit()
        return json.dumps({"message":"EmployeeDeleted"})

@app.route("/modify_employee", methods=["PUT"])
@auth.valid_token
def modify_employee():
    data=request.get_json() or {}
    if not data:
        return json.dumps({"message":"NoData"})
    else:
        emp=Employee.query.get(int(data["id"]))
        if "ed" in data: emp.ed=data["ed"]
        if "role" in data: emp.role=data["role"]
        db.session.commit()
        return json.dumps({"message":"EmployeeModified"})

@app.route("/display_employees", methods=["GET"])
@auth.valid_token
def display_employees():
    employees=Employee.query.all()
    tmp=[]
    for emp in employees:
        tmp.append(dict(zip(['id','name','age','ed','role'],
            [emp.id,emp.name,emp.age,emp.ed,emp.role])))
    if employees:
        return json.dumps(tmp)
    else:
        return json.dumps({"message":"NoEmployeeData"})
