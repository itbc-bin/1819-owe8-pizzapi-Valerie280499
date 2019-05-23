from flask import Flask, jsonify, request

app = Flask(__name__)

pizzaDB = [{'name': 'tonno'},
           {'name': 'salami'},
           {'name': 'hawaii'}]


# @app.route("/", methods=['GET'])
# def getPizza():
#     return jsonify({'pizzaDB': pizzaDB})

@app.route("/<string:name>", methods=['GET'])
def getOnePizza(name):
    resultPizza = []
    for pizza in pizzaDB:
        if pizza['name'] == name:
            resultPizza.append(pizza)
    return jsonify({'pizzaDB':resultPizza})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
