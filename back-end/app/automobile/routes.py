from flask import Response, request
from flask_restful import Resource, reqparse
from datetime import datetime

from . import automobile_api
from .. import cursor

# user

user_parser = reqparse.RequestParser()
user_parser.add_argument('id', type=int)
user_parser.add_argument('type', type=int)
user_parser.add_argument('name', type=str)
user_parser.add_argument('address', type=str)
user_parser.add_argument('zip', type=str)

user_parser.add_argument('category', type=str)
user_parser.add_argument('gross', type=int)

user_parser.add_argument('gender', type=int)
user_parser.add_argument('marriage', type=str)
user_parser.add_argument('age', type=int)
user_parser.add_argument('income', type=int)

user_parser.add_argument('email', type=str)
user_parser.add_argument('jobTitle', type=int)
user_parser.add_argument('storeId', type=int)
user_parser.add_argument('salary', type=int)

user_parser.add_argument('data', type=dict)


class User(Resource):
    def get(self):
        args = user_parser.parse_args()
        cursor.execute(
            'SELECT * FROM user WHERE id={id}'.format(id=args['id']))
        data = cursor.fetchone()
        if data is not None:
            data['status'] = True
            data['userId'] = data['id']
            if data['type'] == 0:
                return data
            if data['type'] == 1:
                cursor.execute(
                    'SELECT * FROM salesperson WHERE id={id};'.format(id=args['id']))
            elif data['type'] == 2:
                cursor.execute(
                    'SELECT * FROM businessCustomer WHERE id={id};'.format(id=args['id']))
            elif data['type'] == 3:
                cursor.execute(
                    'SELECT * FROM homeCustomer WHERE id={id};'.format(id=args['id']))
            data.update(cursor.fetchone())
            return data
        else:
            return {'status': False}

    def put(self):
        args = user_parser.parse_args()
        cursor.execute(
            'SELECT * FROM user WHERE id={id}'.format(id=args['id']))
        data = cursor.fetchone()
        if data is not None:
            cursor.execute("UPDATE user SET name='{name}', type={type}, address='{address}', zip='{zip}' WHERE id={id};".format(
                id=args['id'], name=args['name'], type=args['type'], address=args['address'], zip=args['zip']))
            if args['type'] == 1:
                cursor.execute("UPDATE salesperson SET email='{email}', jobTitle='{jobTitle}', storeId={storeId}, salary={salary} WHERE id={id};".format(
                    id=args['id'], email=args['email'], jobTitle=args['jobTitle'], storeId=args['storeId'], salary=args['salary']))
            elif args['type'] == 2:
                cursor.execute("UPDATE businessCustomer SET category='{category}', gross={gross} WHERE id={id};".format(
                    id=args['id'], category=args['category'], gross=args['gross']))
            elif args['type'] == 3:
                cursor.execute("UPDATE homeCustomer SET gender={gender}, marriage='{marriage}', age={age}, income={income} WHERE id={id};".format(
                    id=args['id'], gender=args['gender'], marriage=args['marriage'], age=args['age'], income=args['income']))
            return {'status': True}
        else:
            return {'status': False}

    def post(self):
        args = user_parser.parse_args()['data']
        cursor.execute(
            'SELECT * FROM user WHERE id={id}'.format(id=args['id']))
        data = cursor.fetchone()
        if data is None:
            cursor.execute("INSERT INTO user (id, name, type, address, zip) VALUES ({id}, '{name}', '{type}', '{address}', '{zip}');".format(
                id=args['id'], name=args['name'], type=args['type'], address=args['address'], zip=args['zip']))
            if args['type'] == 1:
                cursor.execute("INSERT INTO salesperson (id, email, jobTitle, storeId, salary) VALUES ({id}, '{email}', '{jobTitle}', {storeId}, {salary});".format(
                    id=args['id'], email=args['email'], jobTitle=args['jobTitle'], storeId=args['storeId'], salary=args['salary']))
            elif args['type'] == 2:
                cursor.execute("INSERT INTO businessCustomer (id, category, gross) VALUES ({id}, '{category}', '{gross}');".format(
                    id=args['id'], category=args['category'], gross=args['gross']))
            elif args['type'] == 3:
                cursor.execute("INSERT INTO homeCustomer (id, gender, marriage, age, income) VALUES ({id}, '{gender}', '{marriage}', '{age}', '{income}');".format(
                    id=args['id'], gender=args['gender'], marriage=args['marriage'], age=args['age'], income=args['income']))
            return {'status': True}
        else:
            return {'status': False}

    def delete(self):
        args = user_parser.parse_args()
        cursor.execute(
            'SELECT * FROM user WHERE id={id}'.format(id=args['id']))
        data = cursor.fetchone()
        if data:
            try:
                cursor.execute(
                    'DELETE FROM user WHERE id={id}'.format(id=args['id']))
                if data['type'] == 1:
                    cursor.execute(
                        'DELETE FROM salesperson WHERE id={id}'.format(id=args['id']))
                elif data['type'] == 2:
                    cursor.execute(
                        'DELETE FROM businessCustomer WHERE id={id}'.format(id=args['id']))
                elif data['type'] == 3:
                    cursor.execute(
                        'DELETE FROM homeCustomer WHERE id={id}'.format(id=args['id']))
                return {'status': True}
            except:
                return {'status': False}
        else:
            return {'status': False}


# product

product_parser = reqparse.RequestParser()
product_parser.add_argument('productId', type=int)
product_parser.add_argument('type', type=int)
product_parser.add_argument('price', type=int)
product_parser.add_argument('productName', type=str)
product_parser.add_argument('inventory', type=int)
product_parser.add_argument('description', type=int)

product_parser.add_argument('data', type=dict)


class Products(Resource):
    def get(self):
        cursor.execute('SELECT * FROM product;')
        data = cursor.fetchall()
        if data:
            data = {
                'status': True,
                'data': data
            }
            return data
        else:
            return {'status': False}


class Product(Resource):
    def get(self):
        args = product_parser.parse_args()
        cursor.execute(
            'SELECT * FROM product WHERE productName LIKE "%{productName}%";'.format(productName=args['productName']))
        data = cursor.fetchall()
        if data:
            data = {
                'status': True,
                'data': data
            }
            return data
        else:
            return {'status': False}

    def post(self):
        args = product_parser.parse_args()['data']
        cursor.execute(
            'SELECT * FROM product WHERE productId = {productId}'.format(productId=args['productId']))
        data = cursor.fetchone()
        if data is None:
            cursor.execute("INSERT INTO product (productId, productName, price, type, inventory, description) VALUES ({productId}, '{productName}', {price}, {type}, {inventory}, '{description}');".format(
                productId=args['productId'], productName=args['productName'], price=args['price'], type=args['type'], inventory=args['inventory'], description=args['description']))
            return {'status': True}
        else:
            return {'status': False}

    def put(self):
        args = product_parser.parse_args()['data']
        cursor.execute(
            'SELECT * FROM product WHERE productId = {productId}'.format(productId=args['productId']))
        data = cursor.fetchone()
        if data is not None:
            cursor.execute("UPDATE product SET productName = '{productName}', price = {price}, type = {type}, inventory = {inventory}, description = '{description}' WHERE productId = {productId};".format(
                productId=args['productId'], productName=args['productName'], price=args['price'], type=args['type'], inventory=args['inventory'], description=args['description']))
            return {'status': True}
        else:
            return {'status': False}

    def delete(self):
        args = product_parser.parse_args()
        cursor.execute(
            'SELECT * FROM product WHERE productId = {productId}'.format(productId=args['productId']))
        data = cursor.fetchone()
        if data is not None:
            try:
                cursor.execute('DELETE FROM product WHERE productId = {productId}'.format(productId=args['productId']))
                return {'status': True}
            except:
                return {'status': False}
        else:
            return {'status': False}


# store

store_parser = reqparse.RequestParser()
store_parser.add_argument('id', type=int)
store_parser.add_argument('address', type=str)
store_parser.add_argument('managerId', type=int)
store_parser.add_argument('regionId', type=int)
store_parser.add_argument('numberOfSalesperson', type=int)

store_parser.add_argument('data', type=dict)

class Stores(Resource):
    def get(self):
        cursor.execute('SELECT * FROM store;')
        data = cursor.fetchall()
        if data:
            data = {
                'status': True,
                'data': data
            }
            return data
        else:
            return {'status': False}


class Store(Resource):
    def get(self):
        args = store_parser.parse_args()
        cursor.execute(
            'SELECT * FROM store WHERE id = {id}";'.format(id=args['id']))
        data = cursor.fetchall()
        if data:
            data = {
                'status': True,
                'data': data
            }
            return data
        else:
            return {'status': False}

    def post(self):
        args = store_parser.parse_args()['data']
        cursor.execute(
            'SELECT * FROM store WHERE id = {id}'.format(id=args['id']))
        data1 = cursor.fetchone()
        cursor.execute(
            'SELECT * FROM salesperson WHERE id = {id}'.format(id=args['managerId']))
        data2 = cursor.fetchone()
        cursor.execute(
            'SELECT * FROM region WHERE id = {id}'.format(id=args['regionId']))
        data3 = cursor.fetchone()
        if data1 is None and data2 is not None and data3 is not None:
            cursor.execute("INSERT INTO store (id, address, managerId, regionId, numberOfSalesperson) VALUES ({id}, '{address}', {managerId}, {regionId}, {numberOfSalesperson});".format(
                id=args['id'], address=args['address'], managerId=args['managerId'], regionId=args['regionId'], numberOfSalesperson=args['numberOfSalesperson']))
            return {'status': True}
        else:
            return {'status': False}

    def put(self):
        args = store_parser.parse_args()['data']
        cursor.execute(
            'SELECT * FROM store WHERE id = {id}'.format(id=args['id']))
        data = cursor.fetchone()
        if data is not None:
            cursor.execute("UPDATE store SET address = '{address}', managerId = {managerId}, regionId = {regionId}, numberOfSalesperson = {numberOfSalesperson} WHERE id = {id};".format(
                id=args['id'], address=args['address'], managerId=args['managerId'], regionId=args['regionId'], numberOfSalesperson=args['numberOfSalesperson']))
            return {'status': True}
        else:
            return {'status': False}

    def delete(self):
        args = store_parser.parse_args()
        cursor.execute(
            'SELECT * FROM store WHERE id = {id}'.format(id=args['id']))
        data = cursor.fetchone()
        if data is not None:
            try:
                cursor.execute('DELETE FROM store WHERE id = {id}'.format(id=args['id']))
                return {'status': True}
            except:
                return {'status': False}
        else:
            return {'status': False}


# transaction


transaction_parser = reqparse.RequestParser()
transaction_parser.add_argument('id', type=int)
transaction_parser.add_argument('date', type=str)
transaction_parser.add_argument('customerId', type=int)
transaction_parser.add_argument('salespersonId', type=int)
transaction_parser.add_argument('storeId', type=int)
transaction_parser.add_argument('productName', type=str)
transaction_parser.add_argument('price', type=int)
transaction_parser.add_argument('quantity', type=int)

transaction_parser.add_argument('data', type=dict)

class TransactionsCustomer(Resource):
    def get(self):
        args = transaction_parser.parse_args()
        cursor.execute('SELECT * FROM transaction WHERE customerId = {customerId};'.format(customerId=args['customerId']))
        data = cursor.fetchall()
        for item in data:
            item['date'] = item['date'].strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute('SELECT name FROM user WHERE id = ' + str(item['salespersonId']))
            item['salespersonName'] = cursor.fetchone()['name']
            cursor.execute('SELECT name FROM user WHERE id = ' + str(item['customerId']))
            item['customerName'] = cursor.fetchone()['name']
        if data:
            data = {
                'status': True,
                'data': data
            }
            return data
        else:
            return {'status': False}

class TransactionsSalesperson(Resource):
    def get(self):
        args = transaction_parser.parse_args()
        cursor.execute('SELECT * FROM transaction WHERE salespersonId = {salespersonId};'.format(salespersonId=args['salespersonId']))
        data = cursor.fetchall()
        for item in data:
            item['date'] = item['date'].strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute('SELECT name FROM user WHERE id = ' + str(item['salespersonId']))
            item['salespersonName'] = cursor.fetchone()['name']
            cursor.execute('SELECT name FROM user WHERE id = ' + str(item['customerId']))
            item['customerName'] = cursor.fetchone()['name']
        if data:
            data = {
                'status': True,
                'data': data
            }
            return data
        else:
            return {'status': False}

class Transaction(Resource):
    def get(self):
        cursor.execute('SELECT * FROM transaction')
        data= cursor.fetchall()
        for item in data:
            item['date'] = item['date'].strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute('SELECT name FROM user WHERE id = ' + str(item['salespersonId']))
            item['salespersonName'] = cursor.fetchone()['name']
            cursor.execute('SELECT name FROM user WHERE id = ' + str(item['customerId']))
            item['customerName'] = cursor.fetchone()['name']
        if data:
            data = {
                'status': True,
                'data': data
            }
            return data
        else:
            return {'status': False}

    def post(self):
        args = transaction_parser.parse_args()['data']
        cursor.execute(
            'SELECT * FROM transaction WHERE id = {id}'.format(id=args['id']))
        data1 = cursor.fetchone()
        cursor.execute("SELECT inventory FROM product WHERE productName='{productName}'".format(productName=args['productName']))
        data2 = cursor.fetchone()
        if data1 is None and data2 is not None and data2['inventory'] > int(args['quantity']):
            cursor.execute("INSERT INTO transaction (id, date, customerId, salespersonId, storeId, productName, price, quantity) VALUES ({id}, '{date}', {customerId}, {salespersonId}, {storeId}, '{productName}', {price}, {quantity});".format(
                id=args['id'], date=datetime.strptime(args['date'],'%Y-%m-%d %H:%M:%S'), customerId=args['customerId'], salespersonId=args['salespersonId'], storeId=args['storeId'], productName=args['productName'], price=args['price'], quantity=args['quantity']))
            return {'status': True}
        else:
            return {'status': False}

    def put(self):
        args = transaction_parser.parse_args()['data']
        cursor.execute(
            'SELECT * FROM transaction WHERE id = {id}'.format(id=args['id']))
        data = cursor.fetchone()
        if data is not None:
            cursor.execute("UPDATE transaction SET date = '{date}', customerId = {customerId}, salespersonId = {salespersonId}, storeId = {storeId}, productName = '{productName}', price = {price}, quantity = {quantity} WHERE id = {id};".format(
                id=args['id'], date=datetime.strptime(args['date'],'%Y-%m-%d %H:%M:%S'), customerId=args['customerId'], salespersonId=args['salespersonId'], storeId=args['storeId'], productName=args['productName'], price=args['price'], quantity=args['quantity']))
            return {'status': True}
        else:
            return {'status': False}

    def delete(self):
        args = transaction_parser.parse_args()
        cursor.execute(
            'SELECT * FROM transaction WHERE id = {id}'.format(id=args['id']))
        data = cursor.fetchone()
        if data is not None:
            try:
                cursor.execute('DELETE FROM transaction WHERE id = {id}'.format(id=args['id']))
                return {'status': True}
            except:
                return {'status': False}
        else:
            return {'status': False}


class Statistics(Resource):
    def get(self):
        data = {}
        cursor.execute('SELECT SUM(price * quantity) AS s FROM transaction;')
        data['totalSales'] = int(cursor.fetchone()['s'])
        cursor.execute('SELECT name, s FROM user, (SELECT customerId, SUM(price * quantity) AS s FROM transaction GROUP BY customerId ORDER BY s DESC LIMIT 1) AS tmp WHERE id = tmp.customerId;')
        res = cursor.fetchone()
        data['mostBuyer'] = res['name']
        data['mostBuyerSpent'] = int(res['s'])
        cursor.execute('SELECT productName, SUM(price * quantity) AS s FROM transaction GROUP BY productName ORDER BY s DESC LIMIT 1;')
        res = cursor.fetchone()
        data['mostPopularProduct'] = res['productName']
        data['mostPopularProductSales'] = int(res['s'])
        cursor.execute('SELECT storeId, COUNT(*) AS c FROM transaction GROUP BY storeId ORDER BY c DESC LIMIT 1;')
        res = cursor.fetchone()
        data['mostPopularStore'] = res['storeId']
        data['mostPopularStoreCount'] = int(res['c'])

        return data


automobile_api.add_resource(User, '/user')
automobile_api.add_resource(Product, '/product')
automobile_api.add_resource(Products, '/products')
automobile_api.add_resource(Store, '/store')
automobile_api.add_resource(Stores, '/stores')
automobile_api.add_resource(Transaction, '/transaction')
automobile_api.add_resource(TransactionsSalesperson, '/transactionsSalesperson')
automobile_api.add_resource(TransactionsCustomer, '/transactionsCustomer')
automobile_api.add_resource(Statistics, '/statistics')

