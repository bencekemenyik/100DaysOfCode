from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record

@app.route('/random')
def get_random_cafe():
    all_cafes = Cafe.query.all()
    random_cafe = random.choice(all_cafes)
    # return jsonify(
    #     cafe={
    #         "can_take_calls": random_cafe.can_take_calls,
    #         "coffee_price": random_cafe.coffee_price,
    #         "has_sockets": random_cafe.has_sockets,
    #         "has_toilet": random_cafe.has_toilet,
    #         "has_wifi": random_cafe.has_wifi,
    #         "id": random_cafe.id,
    #         "img_url": random_cafe.img_url,
    #         "location": random_cafe.location,
    #         "map_url": random_cafe.map_url,
    #         "name": random_cafe.name,
    #         "seats": random_cafe.seats,
    #
    #     }
    # )
    return jsonify(cafe=random_cafe.to_dict())

@app.route('/all')
def get_all_cafe():
    all_cafes = Cafe.query.all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route('/search')
def get_cafe_by_location():
    location = request.args.get('loc')
    given_location_cafes = Cafe.query.filter_by(location=location).all()
    if len(given_location_cafes) > 0:
        return jsonify(cafes=[cafe.to_dict() for cafe in given_location_cafes])
    else:
        return jsonify(error={
            "Not found": f"Sorry, we don't have a cafe at {location if location is not None else 'that location' }"
        })

## HTTP POST - Create Record

@app.route('/add', methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        seats=request.form.get('seats'),
        has_toilet=bool(request.form.get('has_toilet')),
        has_wifi=bool(request.form.get('has_wifi')),
        has_sockets=bool(request.form.get('has_sockets')),
        can_take_calls=bool(request.form.get('can_take_calls')),
        coffee_price=request.form.get('coffee_price'),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={
        "success": "Successfully added the new cafe."
    })

## HTTP PUT/PATCH - Update Record

@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def change_cafe_price(cafe_id):
    new_price = request.args.get('new_price')
    cafe_to_patch = Cafe.query.get(cafe_id)
    if cafe_to_patch:
        cafe_to_patch.coffee_price = new_price
        db.session.commit()
        return jsonify(response={
            "success": "Successfully updated the price."
        }), 200
    else:
        return jsonify(response={
            "Not found": "Sorry a cafe with that id was not found in the database."
        }), 404

## HTTP DELETE - Delete Record

@app.route('/report-closed/<cafe_id>', methods=['DELETE'])
def delete_closed_cafe(cafe_id):
    api_key = request.args.get('api-key')
    if api_key == "TopSecretAPIKey":
        cafe_to_delete = Cafe.query.get(cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={
                "success": "Successfully deleted the cafe."
            }), 200
        else:
            return jsonify(response={
                "Not found": "Sorry a cafe with that id was not found in the database."
            }), 404
    else:
        return jsonify(response={
            "Access denied": "Sorry, you are not authorized to delete in the database."
        }), 403

if __name__ == '__main__':
    app.run(debug=True)
