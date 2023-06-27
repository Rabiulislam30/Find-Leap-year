#Python program to check if year is a leap year or not

year = 2000

year = int(input("Enter a year: "))

if(year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))


#not divided by 100 means not a century year
#year divided by 4 is a leap year

elif(year % 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))


#if npt divided by both 400(century year) and 4 (not century year)

#year is not leap year

else:
    print("{0} is not a leap year".format(year))

