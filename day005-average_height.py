student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)): # Last item not included
  student_heights[n] = int(student_heights[n])

summ = 0
cnt = 0

for item in student_heights:
    summ += item
    cnt += 1

avg_height = round(summ/cnt)

print(avg_height)
