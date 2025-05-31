'''
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
'''

My_Dict = {'Alice': 85, 'Sam': 90, 'Alex': 75}
Stu_Name = input("Enter the student's name: ")

if Stu_Name in My_Dict:
    print(f"{Stu_Name}'s marks: {My_Dict[Stu_Name]}")
else:
    print("Student not found.")
