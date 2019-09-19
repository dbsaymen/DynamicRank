import os
import pygal 
import pandas as pd
from flask import Flask, render_template, request
import DynamicRANK
app = Flask(__name__)

data1=pd.read_csv("Database.csv",index_col=None)
scoredbase=pd.read_csv("sortedbase.csv",index_col=None)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home/index.html",db_length=data1.shape[0],features_length=data1.shape[1],features=data1.columns,list=scoredbase,is_empty=False)


@app.route("/rank",methods=['GET','POST'])
def rank():
    scoredbase=pd.read_csv("sortedbase.csv",index_col=None)
    if request.args.getlist('choice') ==[]:
        print("empty list")
        return render_template("home/index.html",db_length=data1.shape[0],features_length=data1.shape[1],features=data1.columns,list=scoredbase,is_empty=True)

    print(str())
    rank_features=request.args.getlist('choice')
    DynamicRANK.rank(rank_features)
    #os.system('StaticFuzzyLogic.py')
    data=pd.read_csv("sortedbase.csv",index_col=None)
    score=list(data['Scores'])
    nomAgence=list(data['Agency_Name'])
    line_chart = pygal.HorizontalBar()
    ft=""
    for i in rank_features :
        ft=ft+i+", "

    line_chart.title = 'ranking according to: '+str(ft)
    for i in range(data.shape[0]):
        line_chart.add(nomAgence[i],score[i])
    graph_data = line_chart.render_data_uri()
    scoredbase=pd.read_csv("sortedbase.csv",index_col=None)
    return render_template("home/index.html", graph_data = graph_data,db_length=data1.shape[0],features_length=data1.shape[1],features=data1.columns,list=scoredbase)
    #return render_template("index.html", graph_data = graph_data)

    #return(str(data))
    #return str(rank_features)


if __name__ == '__main__':
    app.run(debug=True)
