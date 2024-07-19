from flask import Flask, render_template,url_for,request
import joblib
import sqlite3

#load
# linear_model=joblib.load("./models/linearmodel.lb")
# decision_model=joblib.load("./models/decisiontree.lb")
random_model=joblib.load("./models/randomforest.lb")


app=Flask(__name__)
data_insertquery=""" create table project
(age,gender,bmi,children,smoker,region,weight,prediction)
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
        age=int(request.form["age"])
        children=int(request.form["children"])
        gender=int(request.form["gender"])
        smoker=int(request.form["smoker"])
        region=request.form["region"]
        weight=int(request.form["weight"])
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
            
        if gender=="Female":
            gender_type="Female"
        else:
            gender_type="Male"
            
        if smoker=="Yes":
            smoker_type=0
        else:
            smoker_type=1
            
        if weight=="UnderWeight":
            under_weight=1
        elif weight=="OverWeight":
            over_weight=2
        elif weight=="HealthyWeight":
            healthy_weight=3
        else:
            obese=4
            
        
        unseen_data=[[age,gender_type,bmi,children,smoker_type,under_weight,over_weight,healthy_weight,obese,region_northeast,region_northwest,region_southeast,region_southwest]]
        # return[region,children,gender,smoker,health,age,bmi]
        prediction=str(random_model.predict(unseen_data)[0])
        print("total charges is : ",prediction)
        connection=sqlite3.connect('insurance.db')
        cur=connection.cursor()
       
        data=(age,gender,bmi,children,smoker,region,weight,prediction)
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




