import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect, url_for
import pymysql.cursors
import sqlalchemy
import pymongo
import json

app = Flask(__name__, static_folder='static', static_url_path='')

'''
global db

def init_connection_engine():
    db_config = {
        # Pool size is the maximum number of permanent connections to keep.
        "pool_size": 5,

        # Temporarily exceeds the set pool_size if no connections are available.
        "max_overflow": 2,

        "pool_timeout": 30,  # 30 seconds
        # [END cloud_sql_mysql_sqlalchemy_timeout]

        "pool_recycle": 1800,  # 30 minutes
        # [END cloud_sql_mysql_sqlalchemy_lifetime]

    }
    return init_tcp_connection_engine(db_config)

def init_tcp_connection_engine(db_config):
    # [START cloud_sql_mysql_sqlalchemy_create_socket]
    # Remember - storing secrets in plaintext is potentially unsafe. Consider using
    # something like https://cloud.google.com/secret-manager/docs/overview to help keep
    # secrets secret.
    db_user = "testuser"
    db_pass = "testpass"
    db_name = "usersearch"
    db_port = 3306
    db_hostname= "34.127.111.46"
    #db_socket_dir = "/cloudsql"
    #instance_connection_name = ""

    pool = sqlalchemy.create_engine(
        # Equivalent URL:
        # mysql+pymysql://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
        sqlalchemy.engine.url.URL.create(
            drivername="mysql+pymysql",
            username=db_user,  # e.g. "my-database-user"
            password=db_pass,  # e.g. "my-database-password"
            host=db_hostname,  # e.g. "127.0.0.1"
            port=db_port,  # e.g. 3306
            database= db_name,  # e.g. "my-database-name"
        ),
        **db_config
    )
    # [END cloud_sql_mysql_sqlalchemy_create_socket]

    return pool

db = init_connection_engine()
'''

#base route
@app.route('/')
def index():
    return app.send_static_file('index.html')

'''
#test POST method
@app.route('/test', methods=['GET', 'POST'])
def test():
    city = request.form.get("city")
    
    return "The var city has returned: " + city
'''

'''
@app.route('/test', methods=['GET', 'POST'])
def test():
    today = datetime.now()
    
    city = ""
    addr = ""
    
    longi = 0.0
    lat = 0.0
    streetZip = 0

    city = request.form.get("city")
    addr = request.form.get("addr")
    formType = request.form.get("type")
    streetZip = request.form.get("zip")
    state = request.form.get("state")
    longi = request.form.get("long")
    lat = request.form.get("lat")     
    emptytest = "not empty"
    if (not addr):
        emptytest = "addr is null or empty"

    if formType == 1:
        city = request.form.get("city")
    elif formType == 2:
        addr = request.form.get("addr")
        zip = request.form.get("zip")
    elif formType == 3:
        longi = request.form.get("long")
        lat = request.form.get("lat") 
    
    curDate = today.strftime("%m/%d/%y")
    st = []
    try:
        with db.connect() as conn:
            #test2 = sqlalchemy.text("INSERT INTO searches (date, address, city, zip, state, latitude, longitude) values (:date, :address, :city, :sZip, :state, :latitude, :longitude)")
            if formType == "1":
                query = sqlalchemy.text("INSERT INTO searches (date, city, state, formType) values (:date, :icity, :istate, :iformType)")
                conn.execute(query, date = curDate, icity = city, istate = state, iformType = formType)
            if formType == "2":
                query = sqlalchemy.text("INSERT INTO searches (date, address, city, zip, state, formType) values (:date, :iaddr, :icity, :izip, :istate, :iformType)")
                conn.execute(query, date = curDate, iaddr = addr, icity = city, izip = streetZip, istate = state, iformType = formType)
            if formType == "3":
                query = sqlalchemy.text("INSERT INTO searches (latitude, longitude, formType) values (:ilat, :ilong, :iformType)")
                conn.execute(query, ilat = lat, ilong = longi, iformType = formType)
            #conn.execute(test2, , address = addr, city = city, sZip = streetZip, state = state, latitude = lat, longitude = longi)
            test = conn.execute("SELECT * from searches").fetchall()
            for row in test:
                st.append(row)

            conn.close()
    finally:
        db.dispose()
    return str(st) + "Form type: " + emptytest
'''
@app.route("/query", methods=['GET', 'POST'])
def connMongodb():
    client = pymongo.MongoClient("mongodb+srv://saira:csusmrocks@cluster0.xvjos.mongodb.net/?retryWrites=true&w=majority")
    db = client.UserSearch
    collect = db.Searches

    #grab todays date and time in pst
    today = datetime.now()
    todayFormat = today.strftime("%m/%d/%y %H:%M:%S %Z")

    #requests from html page
    city = request.form.get("city")
    addr = request.form.get("addr")
    formType = request.form.get("type")
    longi = request.form.get("long")
    lat = request.form.get("lat")  
    searchRange = request.form.get("range")


    #turn requests into dict
    dict = {
        "formType": formType,
        "date": todayFormat,
        "city": city,
        "searchRange": searchRange,
        "address": addr,
        "latitude": lat,
        "longitude": longi
    }
    '''
    if formType == "1":
        dict = {
            "formType": formType,
            "city": city,     
        }
    elif formType == "2":
        
            dict = {
            "formType": formType,
            "city": city,
        }
    '''

    collect.insert_one(dict)
    
    #collects most recent search
    #lastInsert = collect.find({}, {"date": 1, "city": 1} ).sort("_id", -1).limit(1)

    return app.send_static_file('calculations.html')

@app.route("/clearusersearches")
def clearuserdb():
    client = pymongo.MongoClient("mongodb+srv://saira:csusmrocks@cluster0.xvjos.mongodb.net/?retryWrites=true&w=majority")
    db = client.UserSearch
    collect = db.Searches
    collect.delete_many({})
    return "searches cleared"

@app.route("/clearresults")
def clearresults():
    client = pymongo.MongoClient("mongodb+srv://saira:csusmrocks@cluster0.xvjos.mongodb.net/?retryWrites=true&w=majority")
    db = client.Osmnx
    collect = db.Results
    collect.delete_many({})
    return "results cleared"

@app.route("/calculations")
def calc():
    return app.send_static_file('calculations.html')

@app.route("/getcalc", methods=['GET','POST'])
def getCalc():
    client = pymongo.MongoClient("mongodb+srv://saira:csusmrocks@cluster0.xvjos.mongodb.net/?retryWrites=true&w=majority")
    db = client.Osmnx
    collect = db.UserChoice

    radioChoice = request.form.get("type2")
    pointsToPull = request.form.get("choice")

    dict = {
        "choice": radioChoice,
        "points": pointsToPull
    }

    collect.insert_one(dict)

    return app.send_static_file('intResults.html')

@app.route("/results")
def results():
    return app.send_static_file('results.html')


if __name__ == "__main__":
    # This is used when running locally. Gunicorn is used to run the
    # application on Cloud Run. See entrypoint in Dockerfile.
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
