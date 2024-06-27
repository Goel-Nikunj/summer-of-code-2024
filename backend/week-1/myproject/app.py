import os
import psycopg2
from flask import Flask,jsonify , render_template

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname="mydatabase",
        user="postgres",
        password="827957",
        host="localhost",
        port="5432"
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM customer;')
    customers = cur.fetchall()
    cur.close()
    conn.close()

    customers_list = []
    for row in customers:
        customer = {
            "c_id": row[0],
            "c_name": row[1],
            "c_email": row[2],
            "c_contact":row[3],
        }
        customers_list.append(customer)

    return jsonify(customers_list)

if __name__ == '__main__':
    app.run(debug=True)