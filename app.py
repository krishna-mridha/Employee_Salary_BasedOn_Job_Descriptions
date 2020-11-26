from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("salary_pickle.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Years_of_Experiences
        Job_Experience = int(request.form["jobexperience"])
        # Distance
        distance = int(request.form["distance"])


        # Airline
        # AIR ASIA = 0 (not in column)
        job_type = request.form['jobtype']
        if job_type == 'CEO':
           CEO = 1
           CFO = 0
           CTO = 0
           Vice_President = 0
           Manager = 0
           Janitor = 0
           Senior = 0
           Junior = 0
                               

        elif job_type == 'CFO':
            CEO = 0
            CFO = 1
            CTO = 0
            Vice_President = 0
            Manager = 0
            Janitor = 0
            Senior = 0
            Junior = 0

        elif job_type == 'CTO':
           CEO = 0
           CFO = 0
           CTO = 1
           Vice_President = 0
           Manager = 0
           Janitor = 0
           Senior = 0
           Junior = 0

        elif job_type == 'Vice_President':
           CEO = 0
           CFO = 0
           CTO = 0
           Vice_President = 1
           Manager = 0
           Janitor = 0
           Senior = 0
           Junior = 0

        elif job_type == 'Manager':
           CEO = 0
           CFO = 0
           CTO = 0
           Vice_President = 0
           Manager = 1
           Janitor = 0
           Senior = 0
           Junior = 0

        elif job_type == 'Janitor':
           CEO = 0
           CFO = 0
           CTO = 0
           Vice_President = 0
           Manager = 0
           Janitor = 1
           Senior = 0
           Junior = 0
        elif job_type == 'Senior':
           CEO = 0
           CFO = 0
           CTO = 0
           Vice_President = 0
           Manager = 0
           Janitor = 0
           Senior = 1
           Junior = 0
      
        else:
           CEO = 0
           CFO = 0
           CTO = 0
           Vice_President = 0
           Manager = 0
           Janitor = 0
           Senior = 0
           Junior = 1

        
        # Degree
        degree = request.form["degree"]
        if degree == 'Doctoral':
            doctoral = 1
            masters = 0
            bachelors = 0
            high_school = 0
            none = 0

        elif degree == 'Masters':
            doctoral = 0
            masters = 1
            bachelors = 0
            high_school = 0
            none = 0

        elif degree == 'Bachelors':
            doctoral = 0
            masters = 0
            bachelors = 1
            high_school = 0
            none = 0
        elif degree == 'High School':
            doctoral = 0
            masters = 0
            bachelors = 0
            high_school = 1
            none = 0
        else:
            doctoral = 0
            masters = 0
            bachelors = 0
            high_school = 0

        # Major
        major = request.form["major"]
        if major == 'Biology':
           Biology = 1
           Business = 0
           Chemistry = 0
           Computer_Science = 0
           Engineering = 0
           Literature = 0
           Math = 0
           Physics = 0
           none = 0   

        elif major == 'Business':
           Biology = 0
           Business = 1
           Chemistry = 0
           Computer_Science = 0
           Engineering = 0
           Literature = 0
           Math = 0
           Physics = 0
           none = 0  
        elif major == ' Chemistry':
           Biology = 0
           Business = 0
           Chemistry = 1
           Computer_Science = 0
           Engineering = 0
           Literature = 0
           Math = 0
           Physics = 0
           none = 0 
        elif major == 'Computer_Science':
           Biology = 0
           Business = 0
           Chemistry = 0
           Computer_Science = 1
           Engineering = 0
           Literature = 0
           Math = 0
           Physics = 0
           none = 0  

        elif major == 'Engineering':
           Biology = 0
           Business = 0
           Chemistry = 0
           Computer_Science = 0
           Engineering = 1
           Literature = 0
           Math = 0
           Physics = 0
           none = 0  

        elif major == 'Literature':
           Biology = 0
           Business = 0
           Chemistry = 0
           Computer_Science = 0
           Engineering = 0
           Literature = 1
           Math = 0
           Physics = 0
           none = 0  
        elif major == 'Math':
            Biology = 0
            Business = 0
            Chemistry = 0   
            Computer_Science = 0
            Engineering = 0
            Literature = 0
            Math = 1
            Physics = 0
            none = 0  
        elif major == 'Physics':
            Biology = 0
            Business = 0
            Chemistry = 0  
            Computer_Science = 0
            Engineering = 0
            Literature = 0
            Math = 0
            Physics = 1
            none = 0 

        else:
            Biology = 0
            Business = 0
            Chemistry = 0 
            Computer_Science = 0
            Engineering = 0
            Literature = 0
            Math = 0
            Physics = 0
            none = 0

        # Industry
        industry = request.form["industry"]
        if industry == 'Auto':
          Auto = 1
          Education = 0
          Finance = 0
          Health = 0
          Oil = 0
          Service = 0
          Web = 0

        elif industry == 'Education':
          Auto = 0
          Education = 1
          Finance = 0
          Health = 0
          Oil = 0
          Service = 0
          Web = 0 

        elif industry == 'Finance':
          Auto = 0
          Education = 0
          Finance = 1
          Health = 0
          Oil = 0
          Service = 0
          Web = 0

        elif industry == 'Health':
          Auto = 0
          Education = 0
          Finance = 0
          Health = 1
          Oil = 0
          Service = 0
          Web = 0

        elif industry == 'oil':
          Auto = 0
          Education = 0
          Finance = 0
          Health = 0
          Oil = 1
          Service = 0
          Web = 0

        elif industry == 'Service':
          Auto = 0
          Education = 0
          Finance = 0
          Health = 0
          Oil = 0
          Service = 1
          Web = 0  
        
        
        else:
          Auto = 0
          Education = 0
          Finance = 0
          Health = 0
          Oil = 0
          Service = 0
          Web = 0
        

        prediction = model.predict([[
            Job_Experience,
            distance,
            CEO,
            CFO,
            CTO, 
            Vice_President, 
            Manager,
            Janitor, 
            Senior, 
            Junior,
            doctoral,
            masters,
            bachelors,
            high_school,
            none,
            Biology,
            Business,
            Chemistry,
            Computer_Science,
            Engineering,
            Literature,
            Math ,
            Physics,
            none,  
            Auto,
            Education, 
            Finance, 
            Health,
            Oil,
            Service, 
            Web 
        ]])

        output = round(prediction[0], 2)

        return render_template('result.html', prediction_text="Machine Predict the Employee salray is . {}".format(output))

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
