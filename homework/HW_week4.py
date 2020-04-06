from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.HW_week4


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/order', methods=['POST'])
def save_data():
    name = request.form['name_data']
    quantity = request.form['quantity_data']
    address = request.form['address_data']
    phone_number = request.form['phone_number_data']

    info = {"name": name, 'quantity': quantity, 'address': address, "phone_number": phone_number}
    db.customer_data.insert_one(info)

    return jsonify({'result': 'success', 'message': '주문완료!'})


@app.route('/order', methods=['GET'])
def list_data():
    customer_list = list(db.customer_data.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'customer_list': customer_list})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)
