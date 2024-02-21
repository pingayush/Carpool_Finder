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
        #Fetch new form data
        userDetails=request.form
        Reg_No = userDetails['reg_no']
        Name=userDetails['name']
        Date = userDetails['date']
        Phone_No = userDetails['phone']
        Time = userDetails['time']
        Destination = userDetails['destination']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO final_users_caropool(Reg_No, Name, date, Phone_No, Time, Destination) VALUES(%s, %s, %s, %s, %s, %s)", (Reg_No, Name, Date, Phone_No, Time, Destination))
        mysql.connection.commit()
        cur.close()
        # return redirect('/final_users_caropool')
    return render_template('home.html')

# var_list=[]

@app.route('/index1',methods=["GET","POST"])
def index1():
    if request.method=='POST':
        #Fetch old form data
        userDetails_old=request.form
        Reg_No_old= userDetails_old['reg_no_old']
        # var_list.append(Reg_No_old)
        # print('hello11',var_list)
        # cur = mysql.connection.cursor()
        # print(Reg_No_old)
        # return Reg_No_old
        # return render_template('trial_users_carpoolhtm.html',userDetails=userDetails_old)
        # cur.close()
        # Reg_No_old=request.args.get("Reg_No_old")
        # Reg_No_old=input()
        users(Reg_No_old)
        return redirect('/final_users_caropool')
    return render_template('home_old.html')

# reg_No_old = index1
# reg_No_old=index1()
# print(Reg_No_old)

# @app.route('/index1')
# def index1():
#     return render_template('home_old.html')

# print('hello22',var_list)

# cur = mysql.connection.cursor()
# cur.execute("SELECT * FROM final_users_caropool WHERE Reg_No='21BAI1760'")
# print(result)

@app.route('/final_users_caropool')
def users(input):
    Reg_no_old=input
    # Reg_No_old=var_list.pop()
    # Reg_No_old=userDetails_old['reg_no_old']
    # print('Reg_No_old= ',Reg_No_old)
    cur = mysql.connection.cursor()
    # resultValue = cur.execute("SELECT * FROM trial_users_caropool")
    # resultValue = cur.execute("SELECT * FROM Carpool.trial_users_caropool WHERE (Destination='Chennai Airport' OR Destination='Chennai Railway Station') ORDER BY Destination, Date, Time")
    # Reg_No_old=input()
    result=cur.execute("SELECT * FROM final_users_caropool WHERE Reg_No=' "+Reg_no_old+" '")
    print(result)
    # row=cur.fetchall()
    # if cur.rowcount==0:
    #     print('Student doesnt exist, you have to register yourself')
    #     return 'Enter data'
    # else:
        # resultValue = cur.execute("SELECT * FROM Carpool.final_users_caropool WHERE (Destination='Chennai Airport' OR Destination='Chennai Railway Station') ORDER BY Destination, Date, Time")
        # if resultValue > 0:
        #     userDetails = cur.fetchall()
        #     return render_template('trial_users_carpoolhtm.html',userDetails=userDetails)

        
    # print(row)
    if result==1:
        resultValue = cur.execute("SELECT * FROM Carpool.final_users_caropool WHERE (Destination='Chennai Airport' OR Destination='Chennai Railway Station') ORDER BY Destination, Date, Time")
        if resultValue > 0:
            userDetails = cur.fetchall()
            # userDetails = cur.execute("SELECT * FROM Carpool.trial_users_caropool WHERE Destination='Chennai Airport'")

            return render_template('trial_users_carpoolhtm.html',userDetails=userDetails)
    # else:
    #     # call /index1 func
    #     return 'Enter data'
if __name__=='__main__':
    app.run(debug=True)

# result=cur.execute("SELECT * FROM final_users_caropool WHERE Reg_No="21BAI1760"")
# if result==1:
    # then proceed with resultValue
# else:
    # ask user to first enter data