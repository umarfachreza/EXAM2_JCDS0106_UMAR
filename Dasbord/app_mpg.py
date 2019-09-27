from flask import Flask,render_template
from Datampg import data_mpg,Data_horsepower,Data_irit
from plots import Dist_MPG,Dist_Horsepower

app = Flask(__name__)

@app.route("/")
def hello():
    data=data_mpg()
    return render_template('Home.html',data=data)

@app.route('/Data')
def Data():
    data=data_mpg()
    return render_template('table_data.html',data=data)

@app.route('/Stats')
def Stats():
    data=Data_horsepower()
    data1=Data_irit()
    return render_template('stats.html',data=data,data1=data1)

@app.route('/Plots')    
def plots():    
    data=Dist_MPG()
    data2=Dist_Horsepower()
    return render_template('plots.html',data=data,data2=data2)



if __name__=='__main__':
    app.run(debug=True,port=9999)