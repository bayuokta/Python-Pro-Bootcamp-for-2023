# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
x = 0
for height in student_heights:
    x += height
    
print(f'total height = {x}')
print(f'number of student = {len(student_heights)}')
print(f'average height = {int(x / len(student_heights))}')

