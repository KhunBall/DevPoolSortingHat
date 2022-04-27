import tkinter as tk
from tkinter import filedialog
import random

def select_txt_file():
    #Initial
    global file_path
    global file_Label
    file_Label.destroy()
    #file select
    file_path = filedialog.askopenfilename(title="กรุณาเลือกไฟล์", filetypes=(("txt files", "*.txt"),))
    #show file path 
    if file_path != "":
        file_Label = tk.Label(text=file_path)
        file_Label.grid(row = 0, column = 1, padx=5, pady=2.5, stick="W")
        check_file_path = 1

#read txt file to list
def read_txt(file):
    # opening the file in read mode
    my_file = open(file, "r", encoding='utf-8')
    # reading the file
    data = my_file.read()
    # replacing end splitting the text 
    students = data.split(",\n")
    my_file.close()
    return students

#write txt file to list
def write_txt(Slytherin,Gryffindor,Hufflepuff,Ravenclaw):
    index = file_path.rindex("/")
    result_path = file_path[:index]
    result_path = result_path + "/result.txt"

    f = open(result_path, "w", encoding='utf-8')
    f.write("Slytherin House : {} \n".format(Slytherin))
    f.write("Gryffindor House : {} \n".format(Gryffindor))
    f.write("Hufflepuff House : {} \n".format(Hufflepuff))
    f.write("Ravenclaw House : {} \n".format(Ravenclaw))
    f.close()

    return result_path

#get list of students to random houses
def random_houses(students):
    houses_Slytherin = []
    houses_Gryffindor = []
    houses_Hufflepuff = []
    houses_Ravenclaw = []

    # loop name all students.
    for i in range(len(students)):
        # random name of student and delete name from list 
        student_name = students.pop(random.randrange(len(students)))
        #select house by mod 4
        houses_select = i % 4
        if houses_select == 0:
            houses_Slytherin.append(student_name)
        elif houses_select == 1:
            houses_Gryffindor.append(student_name)
        elif houses_select == 2:
            houses_Hufflepuff.append(student_name)
        elif houses_select == 3:
            houses_Ravenclaw.append(student_name)

    return houses_Slytherin, houses_Gryffindor, houses_Hufflepuff, houses_Ravenclaw

def start_btn():
    #error pop up don't select file
    if file_path == "":
        response = tk.messagebox.showerror ("ERROR", "กรุณาเลือกไฟล์")
    else:
        students = read_txt(file_path)
        all_students = str(len(students))
        Slytherin,Gryffindor,Hufflepuff,Ravenclaw = random_houses(students)
        result_path = write_txt(Slytherin,Gryffindor,Hufflepuff,Ravenclaw)

        #Row2
        students_Label = tk.Label(text="All Students : {}".format(all_students))
        students_Label.grid(row = 2, column = 1, padx=5, pady=2.5, stick="W")
        #Row3
        Slytherin_Label = tk.Label(text="Slytherin Hose : {}".format(len(Slytherin)))
        Slytherin_Label.grid(row = 3, column = 1, padx=5, pady=2.5, stick="W")
        #Row4
        Gryffindor_Label = tk.Label(text="Gryffindor Hose : {}".format(len(Gryffindor)))
        Gryffindor_Label.grid(row = 4, column = 1, padx=5, pady=2.5, stick="W")
        #Row5
        Hufflepuff_Label = tk.Label(text="Hufflepuff Hose : {}".format(len(Hufflepuff)))
        Hufflepuff_Label.grid(row = 5, column = 1, padx=5, pady=2.5, stick="W")
        #Row6
        Ravenclaw_Label = tk.Label(text="Ravenclaw Hose : {}".format(len(Ravenclaw)))
        Ravenclaw_Label.grid(row = 6, column = 1, padx=5, pady=2.5, stick="W")
        #Row7
        Ravenclaw_Label = tk.Label(text="Result file : {}".format(result_path))
        Ravenclaw_Label.grid(row = 7, column = 1, padx=5, pady=2.5, stick="W")

# configure the tkinter Graphical User Interface (GUI).
root = tk.Tk()
# Set the tkinter window title.
root.title("Python Sorting Hat")
# Set the tkinter window size.
root.geometry("500x230")

#Row0
# open_btn = tk.Button(frame_1, text="เลือกไฟล์", command=select_file)
open_btn = tk.Button(text="เลือกไฟล์", command=select_txt_file)
open_btn.grid(row = 0, column = 0, padx=5, pady=2.5, stick="W")
file_Label = tk.Label(text="กรุณาเลือกไฟล์")
file_Label.grid(row = 0, column = 1, padx=5, pady=2.5, stick="W")

#Row1
start_btn = tk.Button(text="แบ่งคนตามบ้าน", command=start_btn)
start_btn.grid(row = 1, column = 1, padx=5, pady=2.5, stick="W")

root.mainloop()