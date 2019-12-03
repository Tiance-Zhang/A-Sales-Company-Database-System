from flask import Response, request
from flask_restful import Resource, reqparse

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
user_parser.add_argument('income', type=int)

user_parser.add_argument('email', type=str)
user_parser.add_argument('jobTitle', type=int)
user_parser.add_argument('storeId', type=int)
user_parser.add_argument('salary', type=int)

user_parser.add_argument('data', type=str)

class User(Resource):
    def get(self):
        args=user_parser.parse_args()
        cursor.execute('SELECT * FROM user WHERE id={id}'.format(id=args['id']))
        data = cursor.fetchone()
        if data is not None:
            data['status'] = True
            data['userId'] = data['id']
            if data['type'] == 0:
                return data
            if data['type'] == 1:
                cursor.execute('SELECT * FROM salesperson WHERE id={id}'.format(id=args['id']))
            elif data['type'] == 2:
                cursor.execute('SELECT * FROM businessCustomer WHERE id={id}'.format(id=args['id']))
            elif data['type'] == 3:
                cursor.execute('SELECT * FROM homeCustomer WHERE id={id}'.format(id=args['id']))
            data.update(cursor.fetchone())
            return data
        else:
            return {'status': False}

    def put(self):
        args=user_parser.parse_args()
        cursor.execute('SELECT * FROM user WHERE id={id}'.format(id=args['id']))
        data = cursor.fetchone()
        if data is not None:
            cursor.execute('''UPDATE user
                            SET name='{name}',
                                type='{type}',
                                address='{address}',
                                zip='{zip}'
                            WHERE id={id};'''.format(id=args['id'],
                                                    name=args['name'],
                                                    type=args['type'],
                                                    address=args['address'],
                                                    zip=args['zip']))
            if args['type'] == 1:
                cursor.execute('''UPDATE salesperson
                                SET email='{email}',
                                    jobTitle='{jobTitle}',
                                    storeId='{storeId}',
                                    salary='{salary}'
                                WHERE id={id};'''.format(id=args['id'],
                                                                email=args['email'],
                                                                jobTitle=args['jobTitle'],
                                                                storeId=args['storeId'],
                                                                salary=args['salary']))
            elif args['type'] == 2:
                cursor.execute('''UPDATE businessCustomer
                                SET category='{category}',
                                    gross='{gross}'
                                WHERE id={id};'''.format(id=args['id'],
                                                                category=args['category'],
                                                                gross=args['gross']))
            elif args['type'] == 3:
                cursor.execute('''UPDATE homeCustomer
                                SET gender='{gender}',
                                    marriage='{marriage}',
                                    income='{income}'
                                WHERE id={id};'''.format(id=args['id'],
                                                                gender=args['gender'],
                                                                marriage=args['marriage'],
                                                                income=args['income']))
            return {'status': True}
        else:
            return {'status': False}

    def post(self):
        args=user_parser.parse_args()['data']
        cursor.execute('SELECT * FROM user WHERE id={id}'.format(id=args['id']))
        data = cursor.fetchone()
        if data is None:
            cursor.execute('''INSERT INTO user (id, name, type, address, zip) VALUES
                            ({id}, '{name}', '{type}', '{address}', '{zip}');'''.format(id=args['id'],
                                                                                        name=args['name'],
                                                                                        type=args['type'],
                                                                                        address=args['address'],
                                                                                        zip=args['zip']))
            if args['type'] == 1:
                cursor.execute('''INSERT INTO user (id, email, jobTitle, storeId, salary) VALUES
                                ({id}, '{email}', '{jobTitle}', '{storeId}', '{salary}');'''.format(id=args['id'],
                                                                                                    email=args['email'],
                                                                                                    jobTitle=args['jobTitle'],
                                                                                                    storeId=args['storeId'],
                                                                                                    salary=args['salary']))
            elif args['type'] == 2:
                cursor.execute('''INSERT INTO user (id, category, gross) VALUES
                                ({id}, '{category}', '{gross}');'''.format(id=args['id'],
                                                                            category=args['category'],
                                                                            gross=args['gross']))
            elif args['type'] == 3:
                cursor.execute('''INSERT INTO user (id, gender, marriage, income) VALUES
                                ({id}, '{gender}', '{marriage}', '{income}');'''.format(id=args['id'],
                                                                                        gender=args['gender'],
                                                                                        marriage=args['marriage'],
                                                                                        income=args['income']))
            return {'status': True}
        else:
            return {'status': False}

    def delete(self):
        args=user_parser.parse_args()
        cursor.execute('SELECT * FROM user WHERE id={id}'.format(id=args['id']))
        data = cursor.fetchone()
        if data is not None:
            try:
                cursor.execute('DELETE FROM user WHERE id={id}'.format(id=args['id']))
                if data['type'] == 1:
                    cursor.execute('DELETE FROM salesperson WHERE id={id}'.format(id=args['id']))
                elif data['type'] == 2:
                    cursor.execute('DELETE FROM businessCustomer WHERE id={id}'.format(id=args['id']))
                elif data['type'] == 3:
                    cursor.execute('DELETE FROM homeCustomer WHERE id={id}'.format(id=args['id']))
                return {'status': True}
            except:
                return {'status': False}
        else:
            return {'status': False}

automobile_api.add_resource(User, '/user')