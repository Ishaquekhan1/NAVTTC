count = 0

while count < 4:
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    marks = int(input("Enter the marks: "))
    rollno = int(input("Enter the Roll No: "))
        
    with open("marksheet.csv", "a+") as file:
        file.write(name+","+str(age)+","+str(marks)+","+str(rollno))
    count +=1