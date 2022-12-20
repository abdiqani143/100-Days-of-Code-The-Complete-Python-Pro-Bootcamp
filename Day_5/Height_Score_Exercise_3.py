
student_score = input("Iput a list of student scores: ").split()
for n in range(0,len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

height_score = 0
for score in student_score:
    if score > height_score:
        height_score = score
print(f"The height score is: {height_score}")




