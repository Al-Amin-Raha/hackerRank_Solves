import calendar
given_month, given_day , given_year = map(int, input().split())
week_day = calendar.weekday(year=given_year,month=given_month,day=given_day)
day_name= calendar.day_name[week_day].upper()
print(day_name)