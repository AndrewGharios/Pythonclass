num_stud = int(input("How many students do you have? "))
num_test_score = int(input("How many test scores per student" ))

for student in range(num_stud):
    total = 0.0
print("Student number",  )
print("-------------")
for test_num in range(num_test_score):
    print("Test number", test_num +1, end= '')
    score = float(input(":"))
    total = total + score

avg = total/num_test_Scores
print("The average for student number is ", format(avg, '.1f'))
