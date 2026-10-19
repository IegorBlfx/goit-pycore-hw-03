import datetime # importing datetime module

def get_days_from_today(date):
    today_date = datetime.date.today() #today's date
    try:
        delta = today_date - datetime.datetime.strptime(date, "%Y-%m-%d").date() # calculating the difference between today's date and the input date
        print(f"Days from today: {delta.days}") # printing the difference in days
        return delta.days
    
    except ValueError: # handling the exception if the input date format is incorrect
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None
    

get_days_from_today(input("Enter a date (YYYY-MM-DD): ")) # calling the function with user input