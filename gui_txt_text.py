txt_help_text = """
This app will predict the probability of you developing type-2 diabetes.
In order to use it, fill in all the fields and press send. To make sure
everything runs smoothly, there are some restrictions:
1) Negative numbers cannot be given.
2) The correct type of information must be entered e.g no words for age.
3) There are limits to prevent extreme values so the app doesn't break
but feel free to play around.
4) Don't leave any fields empty.

Range
-------
Age: 0 - 130
BMI/Glucose/Blood Pressure: Any positive number

Obtaining the data
--------------------
Age: Current year - your birth year
BMI: weight[kg]/Height^2[m]
Glucose: Use a blood glucose meter
Blood Pressure: Use a blood pressure moniter and take the lower number.

Have fun! And remember, this is just an app. Consult a doctor for serious
medical related issues.
"""

txt_about_text = """
Name: Type-2 diabetes predictor
Version: 2.0
Modules used: Numpy, tkinter, SciKit-learn, Pandas
description: Tests the probability of the user developing type-2 diabetes.
Machine Learning Model: Logistic Regression
Dataset used: rb.gy/mrwkvd
"""

txt_info_text = """
Important notice: This is just an app, consult a doctor for serious medical issues.
---------------------------------------------------------------------------------------------------------
This section contains information on type-2 diabetes:
1) What is it?
Type-2 diabetes occurs when your body cannot produce enough insulin or becomes resistant to it.

2)What causes it?
-Being overweight
-Being too inactive
-A family history of the disease.

3)What are the symptoms?
-Peeing a lot
-tiredness
-constantly thiirsty
-losing weight without trying
-cuts take long to heal
-blurred vision

4)How is it diagnosed?
Go to your GP who will do a urine and blood test. If the test comes back positive, they will
call you back and explain the next step.

5)What is the treatment?
-They will give you medicine to help maintain your blood-sugar levels.
-You will be expected to make lifestyle changes such improving your diet and being more active.
-You will be given regular checkups to make sure everything is ok.

Measurements of a healthy person
----------------------------------
Age: n/a
BMI: 18.5 - 25.0
Glucose: 140[mg/dL]/7.8[mmol/L] 90mins after a meal
Blood Pressure: <80[mm Hg] (This is your lower/diastolic one)
---------------------------------------------------------------------------------------------------------
It is important to remember that diabetes (both type-1 and type-2) are serious illnesses and
if you think you have it then you consult a medical professional. It is a lifetime disease
which means once you get it, there is no permenant cure. So make sure to maintain your health
even if the app says your risk is low. Also remember that this is just an app, it does not
replace the opinion of a medical professional at all.
---------------------------------------------------------------------------------------------------------
Source:
1) https://www.nhs.uk/conditions/diabetes/
2) https://www.nhs.uk/conditions/type-2-diabetes/
3) https://www.diabetes.co.uk/diabetes_care/blood-sugar-level-ranges.html
4) https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings
5) https://www.nhs.uk/common-health-questions/lifestyle/what-is-the-body-mass-index-bmi/
"""

lbl_result_text = """
Please fill in all the blanks in the entry fields.
Once done press send to get your result.
It will be displayed on this screen.

This app doesn't replace the opinion of doctors
"""
