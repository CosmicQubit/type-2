#User Inputs
#Imported Modules
import numpy as np

#Variables
def Age(input):#input = data obtained from user by the GUI
    try:#using a try/except to make it easier to deal with certain errors
        age = round(float(input))#rounding automatically so user doesn't have to
        if age >= 0 and age <= 130:#range check
            return age#if everything is ok, returns value
        else:
            return False#if range check fails, a 'False' is returned
    except (ValueError, TypeError):#type check
        return False#same as range check

def BMI(input):
        try:
            bmi = round(float(input), 1)
            if bmi > 0:
                return bmi
            else:
                return False
        except (ValueError, TypeError):
            return False

def Glucose(input):
        try:
            glucose = round(float(input), 1)
            if glucose > 0:
                return glucose
            else:
                return False
        except (ValueError, TypeError):
            return False

def BloodPressure(input):
        try:
            blood_p = round(float(input))
            if blood_p > 0:
                return blood_p
            else:
                return False
        except (ValueError, TypeError):
            return False
