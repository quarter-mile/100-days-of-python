student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

top_score = student_scores[0]

for item in student_scores:
    if item > top_score:
        top_score = item

print(f"The highest score in the class is: {top_score}")
