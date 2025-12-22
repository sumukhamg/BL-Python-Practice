def checkLeap(year):
    if year % 4 == 0 and year % 400 == 0 or year % 100 != 0:
        print("The year ", year , " is a leap year")
    else:
        print("The year ", year , " is not a leap year") 

year = int(input("Enter the year"))
checkLeap(year)