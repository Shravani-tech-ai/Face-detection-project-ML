from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("student")

        img=Image.open(r"C:\Users\Avinash M Jadhav\Desktop\Project ML\Images\student_background.jpg")
        img=img.resize((1350,700))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1350,height=700)

        title_lbl=Label(f_lbl, text="  Student Details", font=("times new roman",35,"bold"), fg="black", bg="white")
        title_lbl.place(x=0, y=0,width=1350,height=100)

        logo = Image.open(r"C:\Users\Avinash M Jadhav\Desktop\Project ML\Images\student.jpg")
        logo = logo.resize((100,100))
        self.photologo=ImageTk.PhotoImage(logo)

        b1=Button(f_lbl, image=self.photologo)
        b1.place(x=0, y=0, width=100, height=100)

        main_frame= Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=150, y=150, width=1000, height=500)

        left_frame= LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE, text="Student Details",font=30)
        left_frame.place(x=20, y=20, width=450, height=450)

        right_frame= LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE, text="Student Details",font=30)
        right_frame.place(x=510, y=20, width=450, height=450)

        img1 = Image.open(r"C:\Users\Avinash M Jadhav\Desktop\Project ML\Images\student_background.jpg")
        img1 = img1.resize((450,150))
        self.photoimg1=ImageTk.PhotoImage(img1)

        b2=Button(left_frame, image=self.photoimg1)
        b2.place(x=0, y=0, width=450, height=150)

        left_frame1 = Label(left_frame,bd=2,bg="white",relief=RIDGE)
        left_frame1.place(x=20, y=170, width=400, height=200)

        dep_label=Label(left_frame1, text="Department", font=("times new roman",12, "bold"))
        dep_label.grid(row=0, column=0)

        dep_combo=ttk.Combobox(left_frame1, font=("times new roman",12, "bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer", "IT", "Civil","Mechanical","Electrical","AI&DS")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1)


if __name__ =="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()