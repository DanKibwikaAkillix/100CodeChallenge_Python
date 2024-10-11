print("======================================\n"+ "    Welcome to the TIP calculator\n"+ "======================================")
total_bill = float(input("What was the Total Bill?"))

tip_percentage = float(input("How much tip would you like to give? <<10, 12, or 15>> :?"))
percentage_bill = (total_bill * (tip_percentage/100))
number_of_people = float(input("How many people tp split the Bill? : "))

payment = (total_bill + percentage_bill) / number_of_people
payment_to_two_decimal_places = round(payment, 2)


print(f"\n***************************************\n |Each person should pay: <<${payment_to_two_decimal_places}>>|\n**********************************")

