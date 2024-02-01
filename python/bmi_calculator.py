weight=int(input('Enter the weight of the person(kg):'))
height=float(input('Enter the height of the person(m):'))
if weight>0 and height>0:
    bmi=(weight/(height*height))
    BMI = round(bmi,1)
    if BMI>=27.5:
        print('Your BMI is '+str(BMI)+' (High Risk)')
    elif BMI>=23 and BMI<=27.4:
        print('Your BMI is '+str(BMI)+' (Moderate Risk)')
    elif BMI>=18.5 and BMI<=22.9:
        print('Your BMI is '+str(BMI)+' (Low Risk)')
    elif BMI<18.5:
        print('Your BMI is '+str(BMI)+' (Risk of nutritional deficiency diseases)')
else:
    print('Provide a valid input')