#CTI-110
#P3LAB LEAP YEAR
#MODULE 10.19
#William Kinchen

is_leap_year = False
   
input_year = int(input('Enter year to determine if it is a leap year => '))
if (input_year % 4) == 0:
    if (input_year % 100) == 0:
        if (input_year % 400) == 0:
            is_leap_year = True
        else:
            is_leap_year = False
    else:
        is_leap_year = True
else:
    is_leap_year = False

if is_leap_year == True:
    print(f'{input_year} - is a leap year.')
else:
    print(f'{input_year} - is not a leap year.')
