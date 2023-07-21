# Program to calculate the BMI
Height =float (input ("Enter your height in centimeters:"))
Weight =float (input ("Enter your weight in KG:"))
Height=Height/100
bmi=Weight/(Height**2)
bmi=round(bmi, 1)
print ("BMI:",bmi)
