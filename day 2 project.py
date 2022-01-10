print("welcome to the tip calculater!")

bill=float(input("what was the total bill?"))
tip=int(input("how much much tip would you like to give?"))
person =int(input("how many people to split the bill? "))
bill_with_tip= tip/100 *bill +bill
bill_with=round(bill_with_tip,2)
print(bill_with)
bill_per_person=bill_with_tip/person
total_amount=(round(bill_per_person,2))
total_amount="{:.2f}".format (bill_per_person)


print(f"each person should pay"+f"total_amount of {total_amount}")