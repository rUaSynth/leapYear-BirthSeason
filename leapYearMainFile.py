# This program will take a users birth month and year, it will
# output what season the user was born in and determine if the
# entered birth year was a leap year, these operations will
# take place within functions
#This function holds main logic
def main():
    user_name = input("Enter your name(zzz to quit): ")
    while user_name != "zzz":
        month=get_month()
        season=find_season(month)
        year=get_year()
        leap=is_leap_year(year)
        if leap == True:
            print("Hello,", user_name+"!","You were born in the",season,"and", year,"was a leap year.")
        elif leap == False:
            print("Hello,", user_name+"!","You were born in the",season,"and", year,"was not leap year.")
        pennies=int(input("How many pennies are in your penny jar? "))
        penny_jar(pennies)
        user_name = input("Enter your name: ")
########################
#Function: get_month
#Input: users birth month
#Output: validated user input
#Purpose: validets user input
#######################
def get_month():
    birth_month = int(input("Enter your birth month(1-12): "))
    while birth_month < 1 or birth_month > 12:
        print("Invalid, please enter a single digit month 1-12")
        birth_month = int(input("Enter your birth month(1-12): "))
    return birth_month
################
#Function: find_season
#Input: user birth month
#Output: season birth month fall in
#Purpose: to determin and return a season
#################
def find_season(month):
    birth_month = month
    if birth_month == 1 or birth_month == 2 or birth_month == 12:
        season = "Winter"
    elif birth_month == 3 or birth_month == 4 or birth_month == 5:
        season = "Spring"
    elif birth_month == 6 or birth_month == 7 or birth_month == 8:
        season = "Summer"
    elif birth_month == 9 or birth_month == 10 or birth_month == 11:
        season = "Fall"
    return season
################
#Function: get_year
#Input: birth year
#Output:birth year
#Purpose: retrieve and validate use birth year
#################
def get_year():
    birth_year = int(input("Enter your four digit birth year: "))
    while birth_year <= 0:
        print("Invalid, please enter a year greater than 0")
        birth_year = int(input("Enter your four digit birth year: "))
    return birth_year
################
#Function: is_leap_year
#Input: year
#Output: bool
#Purpose: to determine is user birth year
# was a leap year
#################
def is_leap_year(year):
    birth_year=year
    if birth_year%4==0:
        if birth_year%100==0:
            if birth_year%400==0:
                return True
            else:
                return False
        else:
return True
else:
        return False
################
#Function: penny_jar
#Input: pennies
#Output: denominations
#Purpose: to sort and print coin amounts
#################
def penny_jar(pennies):
    print(pennies//100, "dollars")
    pennies = pennies%100
    print(pennies//25, "quarters")
    pennies = pennies%25
    print(pennies//10, "dimes")
    pennies = pennies%10
    print(pennies//5, "nickles")
    pennies = pennies%5
    print(pennies//1, "pennies")
main()
