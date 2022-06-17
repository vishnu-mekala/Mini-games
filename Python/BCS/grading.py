marks = float(input('Enter the marks obtained: '))
if marks >= 90 and marks <= 100:
    print('Grade is S+')
elif marks >= 80 and marks < 90:
    print('Grade is S')
elif marks >= 70 and marks < 80:
    print('Grade is A')
elif marks >= 60 and marks < 70:
    print('Grade is B')
elif marks >= 50 and marks < 60:
    print('Grade is C')
elif marks >= 35 and marks < 50:
    print('Grade is D')
elif marks < 35 and marks >= 0:
    print('Grade is F')