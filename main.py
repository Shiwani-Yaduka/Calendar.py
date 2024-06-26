#Code to check whether it is a leap year or not

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

#To find number of days

def days_in_month(y, m):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if is_leap(y)==True:
    if m==2:
      return 29
    else:
        return month_days[m-1]
  else:
    return month_days[m-1]

#inputs and calling functions
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)
