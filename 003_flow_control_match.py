number_of_day = int(input("Enter number of a day (1-7)"))

day_name = "unknown"
match number_of_day:
    case 1: day_name = "Monday"
    case 2: day_name = "Tuesday"
    case 3: day_name = "Wednesday"
    case 4: day_name = "Thursday"
    case 5: day_name = "Friday"
    case 6: day_name = "Saturday"
    case 7: day_name = "Sunday"

print("The %d day is %s" % (number_of_day, day_name))

match day_name:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("%s is a workday" % day_name)
    case "Saturday" | "Sunday":
        print("%s is a weekend!" % day_name)
