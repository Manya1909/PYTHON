name=input("enter student's name:")
roll_no=int(input("enter student's roll number:"))

sub1=float(input("Enter Marks for Subject 1:"))
sub2=float(input("Enter Marks for Subject 2:"))
sub3=float(input("Enter Marks for Subject 3:"))
sub4=float(input("Enter Marks for Subject 4:"))
sub5=float(input("Enter Marks for Subject 5:"))
total=(sub1 + sub2 + sub3 + sub4 + sub5)


percentage= (total/500) * 100
print(percentage)
if percentage >=90:
    print("Grade=A+","Remarks=Outstanding")
elif percentage >=80:
    print("Grade=A", "Remarks=Excellent")
elif percentage >=70:
    print("Grade=B","Remarks=Very Good")
elif percentage >=60:
    print("Grade=C","Remarks=Good")
elif percentage >=50:
    print("Grade=D","Remarks=Satisfactory")
else:
    print("Grade=E","Remarks=Marginal Pass")