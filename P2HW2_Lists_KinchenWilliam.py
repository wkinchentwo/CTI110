# CTI-110
# P2HW2 - List
# William Kinchen 
# 17 OCT 2022
grades = []
grades.append(float(input('Enter grade for Module 1: ')))
grades.append(float(input('Enter grade for Module 2: ')))
grades.append(float(input('Enter grade for Module 3: ')))
grades.append(float(input('Enter grade for Module 4: ')))
grades.append(float(input('Enter grade for Module 5: ')))
grades.append(float(input('Enter grade for Module 6: ')))
print()
print('--------------Results-----------------')
print(f'Lowest Grade:       {min(grades):.2f}')
print(f'Highest Grade:      {max(grades):.2f}')
print(f'Sum of Grades:      {sum(grades):.2f}')
print(f'Average:            {sum(grades)/len(grades):.2f}')
print('--------------------------------------')
