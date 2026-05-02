 n= int(input())
student_marks = {}
avg=0
for i in range(n):
   name, *line = input().split()
   scores = list(map(float, line))
   student_marks[name] = scores
query_name = input()
marks=student_marks[query_name]
avg=sum(marks)/len(marks)
print(f"{avg:.2f}")

    
