from flask import Flask, render_template,url_for,request
import joblib
import sqlite3




#load
# linear_model=joblib.load("./models/linearmodel.lb")
# decision_model=joblib.load("./models/decisiontree.lb")
random_model=joblib.load("./models/randomforest.lb")


app=Flask(__name__)
data_insertquery=""" create table project
(age,gender,bmi,region,children,smoker,health,prediction)
values(?,?,?,?,?,?,?,?)"""

@app.route("/")

def home():
    return render_template("index.html")

@app.route("/project")
def project():
    return render_template("project.html")


@app.route("/predict",methods=['GET','POST'])
def predict():
    
    
    if request.method=="POST":
        # to receive the data
        region=request.form["region"]
        children=int(request.form["children"])
        gender=int(request.form["gender"])
        smoker=int(request.form["smoker"])
        health=int(request.form["health"])
        age=int(request.form["age"])
        bmi=int(request.form["bmi"])
        region_northeast=0
        region_northwest=0
        region_southeast=0
        region_southwest=0
        if region=="se":
            region_southeast=1
        elif region=="sw":
            region_southwest=1
        elif region=="ne":
            region_northeast=1
        else:
            region_northwest=1
            
        
        unseen_data=[[age,gender,bmi,children,smoker,health,region_northeast,region_northwest,region_southeast,region_southwest]]
        # return[region,children,gender,smoker,health,age,bmi]
        prediction=str(random_model.predict(unseen_data)[0])
        print("total charges is : ",prediction)
        connection=sqlite3.connect('insurance.db')
        cur=connection.cursor()
       
        data=(age,gender,bmi,region,children,smoker,health,prediction)
        cur.execute(data_insertquery,data)
        print("your data is inserted",data)
        connection.commit()
        cur.close()
        connection.close()
        # return unseen_data
        return render_template('final.html',output=prediction)

        
#         # prediction_=model.predict(data)[0]
#         # prediction
        
      # assignment--->  
        


if __name__=="__main__":
    app.run(debug=True)




