# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇


# print(student_heights) 

sum_students = 0
for students in student_heights:
  sum_students += students
  # print(sum_students)


count_students = 0
for students in student_heights:
  count_students = count_students+1
  # print(count_students)
  
print(f"There are a total of {count_students} students who entered their heights!")

print(f"Average height for the students is {round(sum_students/count_students)}")

# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

# There are a total of 7 heights in student_heights

# 1146 ÷ 7 = 163.71428571428572

# Average height rounded to the nearest whole number = 164