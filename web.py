from flask import Flask, render_template,url_for,request
import joblib

#load
# linear_model=joblib.load("./models/linearmodel.lb")
# decision_model=joblib.load("./models/decisiontree.lb")
random_model=joblib.load("./models/randomforest.lb")

app=Flask(__name__)
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
        prediction=random_model.predict(unseen_data)[0]
        print("total charges is : ",prediction)
        return unseen_data

        
#         # prediction_=model.predict(data)[0]
#         # prediction
        
        
        


if __name__=="__main__":
    app.run(debug=True)




