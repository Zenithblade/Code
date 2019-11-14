en=input("Employee's name: ")
nh=float(input("Number of hours worked in a week: "))
hpr=float(input("Enter hourly pay rate: "))
ftw=float(input("Enter federal tax withholding rate: "))
stw=float(input("Enter state tax withholding rate: "))

gp=hpr*nh
fw=gp*ftw
sw=gp*stw
td=fw+sw
np=gp-td

print(en)
print(nh)
print("$"+str(hpr))
print("$"+str(gp))
print("Deductions:")
print("Federal Withholding" + "(" + str(ftw * 100) +"%): "+"$"+str(fw))
print("State Withholding" + "(" + str(stw* 100) +"%): "+"$"+str(sw))
print("Total Deduction: "+"$"+str(td))
print("Net pay: "+"$"+str(np))