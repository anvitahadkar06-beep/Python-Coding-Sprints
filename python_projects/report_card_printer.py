#Build a Report Card Printer

num=int(input("Enter the number of students: "))
students=[] #Creating an empty list to store student data

for i in range(num):
    print(f"\n-----Collecting Details of Student {i+1}-----\n")
    name=input("Enter the name: ")
    roll=int(input("Enter roll no: "))
    marks=float(input("Enter marks: "))
    stu={"Name":name,"Roll":roll,"Marks":marks}
    students.append(stu) #adding each dictionary to the end empty list

print("\n------Displaying the Report Cards-----")
print("\nName\tRoll\tMarks")
print("----------------------")

for stu in students:
    print(f"{stu['Name']}\t\t{stu['Roll']}\t\t{stu['Marks']}")

# Verified commit check.