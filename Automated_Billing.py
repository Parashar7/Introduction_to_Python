print("\t\t\t\t\tThis is a program to automate a Billing System\n\n\n")

pre_mon=int(input("Enter the Previous Month Home Units:  "))
cur_mon=int(input("Enter the Current Home Month Units:  "))
ac1=int(input("Enter the Previous A.C Month Units:  "))
ac2=int(input("Enter the Current A.C Month Units:  "))
print("Home Units", ac2-ac1)
print("A.C Units", cur_mon-pre_mon )
diff=(ac2-ac1) + (cur_mon-pre_mon) +24
print("Total Unit including default 24 units is:  ", diff)
unit=float(input("Enter Cost Per Unit ="))
total_unit= diff * unit
print("Total Cost of Electricity is:   ", total_unit ,"\n\n")
print("Calculation of Default Charges:")
t_tloss=float(input("Enter the T&T Loss:  "))
mr=float(input("Enter the Meter Reading:  "))
tm=float(input("Enter Transformer Maintenance Charge:  "))
wm=float(input("Enter Water Management Charge:  "))
ac=float(input("Enter Admin. Charges:  "))
mw=float(input("Enter the Maintenance Work:  "))
default=(t_tloss+mr+tm+wm+ac+mw)/3
print("Default Charge is:  ",default, "\n\n")
rent= int(input("Rent:"))
print("Water:300")
print("Maintenance:400")
print("Electricity:", total_unit)
print("Default:", default)
due=int(input("Due, if any:"))
ad=int(input("Adjusted Amount:"))
water=300
maintain=400
bill=(rent+water+maintain+total_unit+default+due)-ad
print("\n\nTotal Bill is:----->>>", bill)
