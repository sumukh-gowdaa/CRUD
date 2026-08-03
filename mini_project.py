students=[]
while True:
    print("""===== Student Management =====

1. Add Student
2. View Students
3. Search Student
4. Update Marks
5. Delete Student
6. Highest Marks
7. Lowest Marks
8. Average Marks
9. Exit""")
    
    while True:
        try:
            choice=int(input("choose: "))
            if  0<choice<10:
                break
            else:
                print("choice should be choosen between 1 and 9")
        except ValueError:
            print("enter digits only")

    if choice==1:
        while True:
            try:
                n=int(input("enter the number of students you want to enter : "))
                if n==0:
                    print(" Zero students can not be added")
                elif n<0:
                    print("enter positive numbers greater than Zero only")
                else:
                    for _ in range(n):
                        while True:
                            roll_no=int(input("enter the roll number of the student"))
                            roll_flag=True
                            for student in students:
                                if student["roll"]==roll_no:
                                    print("the student with the roll number already exists")
                                    roll_flag= False
                                    break
                            if roll_flag:
                                break
                                
                            
                        while True:
                            name=input("enter name: ")
                            name=name.strip()
                            if not name:
                                print("Name can not be empty")
                            else:
                                break

                        while True:
                            marks=int(input("Enter marks: "))
                            if not 0<=marks<=100:
                                print("marks should be between 0 to 100")
                            else:
                                break
                        student={
                            "roll":roll_no,
                            "name":name,
                            "marks":marks
                        }
                        students.append(student)
                break
            except ValueError:
                print("enter only digits")

    elif choice==2:
        if len(students)==0:
            print("no student records found")
        else:
            print("Roll   Name      Marks")
            print("-----------------------")

            for student in students:
                print(f"{student['roll']:<7}{student['name']:<10}{student['marks']}")

    elif choice==3:
        while True:
            try:
                find_roll=int(input("enter the roll number: "))
                found=False
                for student in students:
                    if student["roll"]==find_roll:
                        print("student found")
                        print("name: ",student["name"])
                        print("Marks: ",student["marks"])
                        found=True
                        break
                if not found:
                    print("student not found")
                else:
                    break
            except ValueError:
                print("enter digits only")

    elif choice==4:
        while True:
            try:
                update_roll=int(input("enter the roll number: "))
                update_flag=False
                for student in students:
                    if student["roll"]==update_roll:
                        print("student found")
                        while True:
                            marks=int(input("Enter new marks: "))
                            if not 0<=marks<=100:
                                print("marks should be between 0 to 100")
                            else:
                                update_flag=True
                                break
                        if update_flag:
                            student["marks"]=marks
                            print("Done")
                            break
                if not update_flag:
                    print("student not found")
                else:
                    break
            except ValueError:
                print("Enter digits only")

    elif choice==5:
        while True:
            try:
                del_flag=False
                delete_roll=int(input("enter the roll number: "))
                for student in students:
                    if student["roll"]==delete_roll:
                        print("student found")
                        students.remove(student)
                        print("deleted successfully")
                        del_flag=True
                        break
                if del_flag:
                    break
                else:
                    print("student not found")

            except ValueError:
                print("enter digits only")

    elif choice==6:
        if not students:
            print("no students present")
        else:
            Max_mark=students[0]
            for student in students:
                if student["marks"]>Max_mark["marks"]:
                    Max_mark=student
            print(Max_mark["name"], Max_mark["roll"],  Max_mark["marks"])

    elif choice==7:
        if not students:
            print("no students are present")
        else:
            min_mark=students[0]
            for student in students:
                if student["marks"]<min_mark["marks"]:
                    min_mark=student
            print(min_mark["name"],  min_mark["roll"], min_mark["marks"])

    elif choice==8:
        if not students:
            print("no students found")
        else:
            avg_total=0
            for student in students:
                avg_total+=(student["marks"])

            print("the avg marks of students is: ",avg_total/len(students))


    elif choice==9:
        print("you have exited")
        break
    
                

            

                    


        


    



                            



