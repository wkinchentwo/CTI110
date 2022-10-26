# CTI-110
#P3HW1 DEBUGGING
# William Kinchen


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

lowestGrade = min(grades)
highestGrade = max(grades)
gradesSum = sum(grades)
average = sum(grades)/len(grades)

# determine letter grade for average
print('----------------Results----------------')
print(f'Lowest Grade:       {min(grades):.2f}')
print(f'Highest Grade:      {max(grades):.2f}')
print(f'Sum of Grades:      {sum(grades):.2f}')
print(f'Average:            {sum(grades)/len(grades):.2f}')
print('---------------------------------------')

if average >= 90:
    print('Your grade is: A')
elif average >= 80:
    print('Your grade is: B')
elif average >= 70:
    print('Your grade is: C')
elif average >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')


    





