weight=int(input("Enter your Weight: "))
unit= input("Write your unit of weight for kilogram write kg and for pound write lb : ")
if unit=='lb':
        lb=weight*0.453
        print("You Entered weight in pound")
        print("weight in Kilogram = ",lb)
elif unit=='kg':
        kg=weight*2.206
        print("you Entered weight in Kilogram")
        print("Weight in Pound is = ",kg)
else:
        print("Invalid Input")