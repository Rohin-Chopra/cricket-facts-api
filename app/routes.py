import requests
import random
from flask import jsonify, request, make_response
import json
from app import app, cors
from app.models import db, CricketFact
from sqlalchemy import func

@app.route('/', methods=['POST'])
def add_fact():
    req = request.get_json()
    fact = req.get('fact')
    if fact == '':
        response = make_response(
            jsonify(
                {"message": "Fact cannot be empty!"}
            ),
            500,
        )
        response.headers["Content-Type"] = "application/json"
        return response

    if not CricketFact.does_fact_exist(fact=fact):
        response = make_response(
            jsonify(
                {"message": "This fact already exists"}
            ),
            500,
        )
        response.headers["Content-Type"] = "application/json"
        return response
    
    cricket_fact=CricketFact(fact=fact)
    db.session.add(cricket_fact)
    db.session.commit()
    response = make_response(
        jsonify(
            {"message": "Added",
             "fact": cricket_fact.get_json()
             }
        ),
        200,
    )
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/',methods=['GET'])
def get_fact():
    req= request.get_json()
    data = CricketFact.query.order_by(func.random()).all()
    fact = random.choice(data)

    return make_response(jsonify(fact.get_json()),200)