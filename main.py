import datetime
from flask import Flask,redirect,url_for,render_template,request, flash, session
from flaskext.mysql import MySQL
import base64
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import datefinder

app=Flask(__name__)
app.secret_key="earth"
mysql_db = MySQL()
app.config['MYSQL_DATABASE_HOST']='127.0.0.1'
app.config['MYSQL_DATABASE_USER']='sysbot'
app.config['MYSQL_DATABASE_PASSWORD']='abc1'
app.config['MYSQL_DATABASE_DB']='terremotos'
mysql_db.init_app(app)
@app.route('/')
def build_plot():

    sql = "SELECT YEAR(`fec_locTerr`) from `Terremotos`"
    

    conexion = mysql_db.connect()
    cursor= conexion.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    conexion.commit()
    conexion.close()
    data_list = []
    for i in data:   
        data_list.append(i)
    print(data_list)











    img = io.BytesIO()
    mag_y = [1,2,3,4,5]
    year_x = [1,2,3,4,5]
    plt.plot(year_x,mag_y)
    plt.xlabel('AÑO')
    plt.ylabel('MAGNITUD')
    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode()

    grafico = 'data:image/png;base64,{}'.format(plot_url)

    return render_template("home.html", grafico = grafico)



def convert_date():
    pass
    



if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host="192.168.1.93", port=5000,debug=True)


""" grafico = '<img src="data:image/png;base64,{}">'.format(plot_url) """