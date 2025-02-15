from flask import Blueprint, request, jsonify
from database import db
from models import Income, Spending

app_routes = Blueprint("app_routes", __name__)

@app_routes.route("/income/<int:user>/<int:summ>/<description>")
def income(user, summ, description):
    income = Income(add=summ, user=user, description=description)
    try:
        db.session.add(income)
        db.session.commit()
        return jsonify({"user": user, "summ": summ, "description": description})
    except Exception:
        return "Произошла ошибка", 500

@app_routes.route("/spending/<int:user>/<int:summ>/<description>")
def spending(user, summ, description):
    spending = Spending(summ=summ, user=user, description=description)
    try:
        db.session.add(spending)
        db.session.commit()
        return jsonify({"user": user, "summ": summ, "description": description})
    except Exception:
        return "Произошла ошибка", 500

@app_routes.route("/<int:user>/incomes")
def incomes(user):
    incomes = Income.query.filter_by(user=user).all()
    return jsonify([{"id": inc.id, "amount": inc.add, "description": inc.description, "date": inc.created_at} for inc in incomes])

@app_routes.route("/<int:user>/spends")
def spends(user):
    spendings = Spending.query.filter_by(user=user).all()
    return jsonify([{"id": spn.id, "amount": spn.summ, "description": spn.description, "date": spn.created_at} for spn in spendings])
