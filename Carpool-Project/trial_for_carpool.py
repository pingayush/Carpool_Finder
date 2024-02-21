from flask import Flask, render_template, request, redirect
import mysql.connector
import yaml
from flask_mysqldb import MySQL
# from flaskext.mysql import MySQL

app= Flask(__name__)

#Configure db
db = yaml.load(open('/Users/siddhantagrawal/Desktop/Web dovel/Carpool/venv/db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER']= db['mysql_user']
app.config['MYSQL_PASSWORD']= db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

# mysql=mysql.connector(app)
mysql=MySQL(app)

@app.route('/',methods=["GET","POST"])
def index():
    if request.method=='POST':
        #Fetch form data
        userDetails=request.form
        Reg_No = userDetails['reg_no']
        Name=userDetails['name']
        Date = userDetails['date']
        Phone_No = userDetails['phone']
        Time = userDetails['time']
        Destination = userDetails['destination']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO trial_users_caropool(Reg_No, Name, date, Phone_No, Time, Destination) VALUES(%s, %s, %s, %s, %s, %s)", (Reg_No, Name, Date, Phone_No, Time, Destination))
        mysql.connection.commit()
        cur.close()
        return redirect('/trial_users_carpool')
    return render_template('lola_ghanti.html')

@app.route('/trial_users_carpool')
def users():
    cur = mysql.connection.cursor()
    # resultValue = cur.execute("SELECT * FROM trial_users_caropool")
    # resultValue = cur.execute("SELECT * FROM Carpool.trial_users_caropool WHERE (Destination='Chennai Airport' OR Destination='Chennai Railway Station') ORDER BY Destination, Date, Time")
    resultValue = cur.execute("SELECT * FROM Carpool.trial_users_caropool WHERE (Destination=Destination) ORDER BY Destination, Date, Time")
    if resultValue > 0:
        userDetails = cur.fetchall()
        # userDetails = cur.execute("SELECT * FROM Carpool.trial_users_caropool WHERE Destination='Chennai Airport'")

        return render_template('trial_users_carpoolhtm.html',userDetails=userDetails)

if __name__=='__main__':
    app.run(debug=True)