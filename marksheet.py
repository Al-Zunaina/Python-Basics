'''Write a Python program to determine a student's grade based on their marks.
Rules:
If the marks are 40 or more, the student passes. Otherwise, they fail.
If the student passes:
Marks ≥ 90 → Grade A+
Marks ≥ 75 but < 90 → Grade A
Marks ≥ 40 but < 75 → Grade B
If marks are below 40, display "Fail".
Input:
An integer representing the student's marks (0–100).
Output:
A message showing whether the student passed or failed, and if passed, the grade.'''
marks=int(input('Eneter the marks/'))
if marks>=40:
    print('PASS')
    if marks>=90:
        print('A+')
    elif marks>=75 and marks<90:
        print('A')
    elif marks>=40 and marks<75:
        print('B')
else:
    print('FAIL')