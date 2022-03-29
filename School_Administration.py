
import csv
def write_into_csv(info_list):
    with open("student_info.csv", "a" ,newline='') as csv_file:
        writer = csv.writer(csv_file)
    
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact Number", "Email Id"])
            writer.writerow(info_list)
if __name__ == '__main__': 
    condition = True        

while (condition):

    student_info = input("Enter the Information of Student (Name Age Contact Numnber Email Id): ")

    #split
    student_info_list = student_info.split(" ")
    

    
    print("\nThe entered information is like : \nName: {} \nAge: {} \nContact number: {} \nEmail Id: {}".
    format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
    
    choice_check =input("Is the entered data is correct (yes/no) :")
    
    if choice_check == 'yes':
        write_into_csv(student_info_list)
        condition_check =input("Want to enter next data (Yes/No) : ")
        if condition_check == "yes":
            condition == True
        elif condition_check == "no":
            condition == False 
            break 
    elif choice_check == "no":
        print("ReEnter The Data Entries")          
     
            



