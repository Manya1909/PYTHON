
print("CALENDAR VERIFICATION SYSTEM")

year_input = input("Enter year: ")
year = int(year_input)
    
    
if year <= 0:
      print("invalid year")


if year % 100 == 0:
        if year % 400 == 0:
            is_leap = True
            reason = "Century year divisible by 400"
        else:
            is_leap = False
            reason = "Century year not divisible by 400"
else:
        if year % 4 == 0:
            is_leap = True
            reason = "Divisible by 4 and not a century year"
        else:
            is_leap = False
            reason = "Common year (not divisible by 4)"

if is_leap:
        print("Status: LEAP YEAR")
        print("Days in Year: 366 days")
        print("Days in February: 29 days")
else:
        print("Status: COMMON YEAR")
        print("Days in Year: 365 days")
        print("Days in February: 28 days")
        