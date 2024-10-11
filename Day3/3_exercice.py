weight = 85
height = 1.85

bmi = weight / (height ** 2)

bmi_rounded = round(bmi,1)
a = float( 18.5)
b = float(25)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi_rounded <a:
    print("underweight")
    
elif bmi_rounded >a :
        print("normal weight")

elif  bmi_rounded< b:
         print("normal weight")
        
elif bmi_rounded > b:
        print("overweight")