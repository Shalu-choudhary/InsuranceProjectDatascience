from flask import Flask, render_template,url_for,request
import joblib

# model=joblib.load("linearmodel.lb")
# model=joblib.load("decisiontree.lb")
# model=joblib.load("randomforest.lb")

app=Flask(__name__)
@app.route("/")

def home():
    return render_template("index.html")

@app.route("/project")
def project():
    return render_template("project.html")


@app.route("/prediction",methods=['GET','POST'])
def project():
    
    if request.method=="POST":
        region=request.form["region"]
        children=request.form["Children"]
        gender=request.form["Gender"]
        smoker=request.form["smoker"]
        health=request.form["Health"]
        age=request.form["Age"]
        bmi=request.form["bmi"]
        
        data=[region,children,gender,smoker,health,age,bmi]
        return data
        # prediction_=model.predict(data)[0]
        # prediction
        
        
        


if __name__=="__main__":
    app.run(debug=True)




