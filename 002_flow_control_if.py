# age = int(input("Age: "))
age = 40
citizenship = "Ukranian"

# if <condition 1>:
#       <run when condition 1 is true>
# elif <condition 2>
#       <run when condition 2 is true>
# else:
#       <run when false> 
if (age >= 18 and citizenship == "Ukranian"):
    print("You are allowed to vote in Ukraine")
    if (age >= 35 and citizenship == "Ukranian"):
        print("You can be the President of Ukraine")
else:
    print("You are not allowed to vote")

print("End")


# <var> = <value when true> if <condition> else <value when false>
msg = "even" if 10 % 2 == 0 else "odd"
print("10 is %s" % msg)

msg = "even" if 11 % 2 == 0 else "odd"
print("11 is %s" % msg)