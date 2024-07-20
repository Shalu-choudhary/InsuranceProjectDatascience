from flask import Flask, render_template, request, url_for
import sqlite3
import joblib

random_forest = joblib.load("./models/randomForest.lb")

app = Flask(__name__)

data_insert_query = """
INSERT INTO project 
(age, gender, bmi, children, region, smoker, weight, prediction)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        age = int(request.form["age"])
        gender = request.form["gender"]
        children = int(request.form["children"])
        smoker = request.form["smoker"]
        region = request.form["region"]
        weight = request.form["weight"]
        bmi = float(request.form["bmi"])  # Ensure BMI is parsed as float
        
        # Convert categorical variables to numerical values
        region_southeast = 1 if region == "southeast" else 0
        region_northeast = 1 if region == "northeast" else 0
        region_northwest = 1 if region == "northwest" else 0
        region_southwest = 1 if region == "southwest" else 0
        
        gender_type = 0 if gender == "Female" else 1
        
        smoker_type = 1 if smoker == "Yes" else 0
        
        # Assign weight_type based on weight category
        if weight == "Underweight":
            weight_type = 1
        elif weight == "Overweight":
            weight_type = 2
        elif weight == "Healthyweight":
            weight_type = 3
        elif weight == "Obese":
            weight_type = 4
        else:
            weight_type = 0  # Default or handle error
        
        unseen_data = [[age, gender_type, children, smoker_type, region_northeast,
                        region_northwest, region_southeast, region_southwest,
                        weight_type, bmi]]
        
        prediction = str(random_forest.predict(unseen_data)[0])
        print("Prediction:", prediction)
        
        # Insert data into SQLite database
        connection = sqlite3.connect("insurance.db")
        cur = connection.cursor()
        
        Data = (age, gender, children, smoker,region, weight,bmi, prediction)
        cur.execute(data_insert_query, Data)
        print("Data inserted into database:", Data)
        
        connection.commit()
        cur.close()
        connection.close()
        
        return render_template("final.html", output=prediction)
    
    return "Prediction failed"

    
if __name__ == "__main__":
    app.run(debug=True)