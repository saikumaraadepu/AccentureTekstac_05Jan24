name_list=[] 


with open('student_marks.txt')as file_obj:
    student_list=file_obj.readlines()
    for i in range(0,len(student_list),2):
        if (int)(student_list[i+1])>=80:
            name_list.append(student_list[i])
        

for i in name_list:
    print(i)