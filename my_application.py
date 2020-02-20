from tkinter import *
import tkinter.messagebox
import sqlite3
db=sqlite3.connect('my_sqlproject.db')
cursor=db.cursor()
db.execute("CREATE TABLE IF NOT EXISTS Admin(ID TEXT,name TEXT,dept_name TEXT)")
db.execute("CREATE TABLE IF NOT EXISTS Advisor(s_id TEXT,i_id TEXT)")
db.execute("CREATE TABLE IF NOT EXISTS course(course_id TEXT,title TEXT,dept_name TEXT,credits TEXT)")
db.execute("CREATE TABLE IF NOT EXISTS instructor(ID TEXT,name TEXT,dept_name TEXT,salary TEXT)")
db.execute("CREATE TABLE IF NOT EXISTS student(ID TEXT,name TEXT,dept_name TEXT,tot_credit TEXT)")
db.execute("CREATE TABLE IF NOT EXISTS department(dept_name TEXT)")
db.execute("CREATE TABLE IF NOT EXISTS takes(ID TEXT,course_id TEXT)")
db.execute("CREATE TABLE IF NOT EXISTS teaches(ID TEXT,course_id TEXT)")
db.commit()
def main():
    root=Tk()
    root1=root
    app=window1(root1)
    root.mainloop()
class window1:
    def __init__(self,master):
        self.master=master
        self.master.title("University management system")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="powder blue")
        #========================================
        menu = Menu(self.master)
        self.master.config(menu=menu)
        def helpp():
            help(sqlite3)
        subm = Menu(menu)
        menu.add_cascade(label="Help",menu=subm)
        subm.add_command(label="Sqlite3 Docs",command=helpp)
        self.frame1=Frame(self.master,bg='powder blue')
        self.frame1.pack()
        self.frame=Frame(self.master,bg='powder blue')
        self.frame.pack()
        self.Username=StringVar()
        self.Password=StringVar()
        self.lbltitle=Label(self.frame1,text='University Management System',font=('arial',15,'bold'),bg='powder blue',fg='black')
        self.lbltitle.grid(row=1,column=0,pady=100)
        #=================================Login===============================
        self.loginframe1=LabelFrame(self.frame,width=350,height=200,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframe1.grid(row=1,column=0)
        self.loginframe2=LabelFrame(self.frame,width=350,height=100,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframe2.grid(row=2,column=0)
        #====================================Label and entry==============
        reg=self.master.register(self.correct)
        self.lblusername=Label(self.loginframe1,text='Username:',font=('arial',10,'bold'),bd=10,bg='cadet blue')
        self.lblusername.grid(row=0,column=0)
        self.txtusername=Entry(self.loginframe1,font=('arial',10,'bold'),textvariable=self.Username)
        self.txtusername.grid(row=0,column=1)
        self.txtusername.config(validate="key",validatecommand=(reg,'%P'))
        self.lblpassword=Label(self.loginframe1,text='Password:',font=('arial',10,'bold'),bd=20,bg='cadet blue')
        self.lblpassword.grid(row=1,column=0)
        self.txtpassword=Entry(self.loginframe1,show='*',font=('arial',10,'bold'),textvariable=self.Password)
        self.txtpassword.grid(row=1,column=1)
        #====================================Button=======================
        self.btnlogin=Button(self.loginframe2,width=17,font=('arial',10,'bold'), text="Login",command=self.login_system)
        self.btnlogin.grid(row=3,column=0)
        self.btnreset=Button(self.loginframe2,width=17,font=('arial',10,'bold'), text="Reset",command=self.reset)
        self.btnreset.grid(row=3,column=1)
        global a
        a=self.master
    def login_system(self):
        u=(self.Username.get())
        p=(self.Password.get())
        global x
        x=u
        self.conn =sqlite3.connect('my_sqlproject.db')
        with self.conn:
            self.cursor = self.conn.cursor()
            self.cur = self.conn.cursor()
            self.cursor.execute('SELECT COUNT(*) FROM Admin WHERE ID=?',(u,))
            self.cur.execute('SELECT COUNT(*) FROM Admin WHERE ID=?',(p,))
            check=self.cursor.fetchone()[0]
            check1=self.cur.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM instructor WHERE ID=?',(u,))
            self.cur.execute('SELECT COUNT(*) FROM instructor WHERE ID=?',(p,))
            checkk=self.cursor.fetchone()[0]
            checkk1=self.cur.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM student WHERE ID=?',(u,))
            self.cur.execute('SELECT COUNT(*) FROM student WHERE ID=?',(p,))
            checkkk=self.cursor.fetchone()[0]
            checkkk1=self.cur.fetchone()[0]
            if(check>0 and check1>0) and u==p:
                self.newwindow=Toplevel(self.master)
                self.app=window2(self.newwindow)
                self.master.withdraw()
            elif(checkk>0 and checkk1>0) and u==p:
                self.newwindow1=Toplevel(self.master)
                self.app1=window3(self.newwindow1)
                self.master.withdraw()
            elif(checkkk>0 and checkkk1>0) and u==p:
                self.newwindow2=Toplevel(self.master)
                self.app2=window4(self.newwindow2)
                self.master.withdraw()
            else:
                tkinter.messagebox.askyesno("Login system","Invalid login details")
                self.Username.set("")
                self.Password.set("")
                self.txtusername.focus()
                self.txtpassword.focus()
            db.close()
    def correct(self,inp):
        self.inp=inp
        if(self.inp.isalnum()):
            return True
        else:
            return False
    def reset(self):
        self.Username.set("")
        self.Password.set("")
        self.txtusername.focus()
        self.txtpassword.focus()
class window2:
    def __init__(self,master):
        self.master=master
        self.master.title("Coordinator")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="powder blue")
        self.frame=Frame(self.master,bg='powder blue')
        self.frame.pack(side=LEFT,fill=Y)
        self.course_id=StringVar()
        self.title=StringVar()
        self.dept_name=StringVar()
        self.credits=StringVar()
        self.lbltitle=Label(self.frame,text='Add course',font=('arial',15,'bold'),bg='powder blue',fg='black')
        self.lbltitle.grid(row=0,column=0,columnspan=2,pady=40)
        #===============================add course==================================
        self.loginframe1=LabelFrame(self.frame,width=600,height=300,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframe1.grid(row=1,column=0)
        self.loginframe2=LabelFrame(self.frame,width=350,height=100,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframe2.grid(row=2,column=0)
        self.loginframe3=LabelFrame(self.frame,bg='powder blue')
        self.loginframe3.grid(row=3,column=0)
        self.loginframe4=LabelFrame(self.frame,width=350,height=100,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframe4.grid(row=4,column=0)
        self.loginframe5=LabelFrame(self.frame,width=350,height=100,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframe5.grid(row=5,column=0)
        #============================labels and entry=====add course================
        self.lblcourse_id=Label(self.loginframe1,text='Course_Id:',font=('arial',10,'bold'),bd=10,bg='cadet blue')
        self.lblcourse_id.grid(row=0,column=0)
        self.txtcourse_id=Entry(self.loginframe1,font=('arial',10,'bold'),textvariable=self.course_id)
        self.txtcourse_id.grid(row=0,column=1)
        self.lbltitle=Label(self.loginframe1,text='Title:',font=('arial',10,'bold'),bd=20,bg='cadet blue')
        self.lbltitle.grid(row=1,column=0)
        self.txttitle=Entry(self.loginframe1,font=('arial',10,'bold'),textvariable=self.title)
        self.txttitle.grid(row=1,column=1)
        self.lbldept_name=Label(self.loginframe1,text='Dept_name:',font=('arial',10,'bold'),bd=10,bg='cadet blue')
        self.lbldept_name.grid(row=2,column=0)
        self.txtdept_name=Entry(self.loginframe1,font=('arial',10,'bold'),textvariable=self.dept_name)
        self.txtdept_name.grid(row=2,column=1)
        self.lblcredit=Label(self.loginframe1,text='Credit:',font=('arial',10,'bold'),bd=20,bg='cadet blue')
        self.lblcredit.grid(row=3,column=0)
        self.txtcredit=Entry(self.loginframe1,font=('arial',10,'bold'),textvariable=self.credits)
        self.txtcredit.grid(row=3,column=1)
        #===============================button==add course====================
        self.btnadd=Button(self.loginframe2,width=17,font=('arial',10,'bold'), text="Add",command=self.insert)
        self.btnadd.grid(row=3,column=0)
        self.btnreset=Button(self.loginframe2,width=17,font=('arial',10,'bold'), text="Reset",command=self.reset)
        self.btnreset.grid(row=3,column=1)
        #==============================Add teacher===================================
        self.ID=StringVar()
        self.Name=StringVar()
        self.Dept_name=StringVar()
        self.Salary=StringVar()
        self.frame1=Frame(self.master,bg='powder blue')
        self.frame1.pack(side=LEFT,fill=Y)
        self.lbltitle1=Label(self.frame1,text='Add teacher',font=('arial',15,'bold'),bg='powder blue',fg='black')
        self.lbltitle1.grid(row=0,column=0,columnspan=2,pady=40)
        #===============================frames in add teacher==================================
        self.loginframee1=LabelFrame(self.frame1,width=600,height=300,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframee1.grid(row=1,column=0)
        self.loginframee2=LabelFrame(self.frame1,width=350,height=100,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframee2.grid(row=2,column=0)
        self.loginframee3=LabelFrame(self.frame1,bg='powder blue')
        self.loginframee3.grid(row=3,column=0)
        self.loginframee4=LabelFrame(self.frame1,width=350,height=100,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframee4.grid(row=4,column=0)
        self.loginframee5=LabelFrame(self.frame1,width=350,height=100,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframee5.grid(row=5,column=0)
         #============================labels and entry=====add teacher================
        self.lblid=Label(self.loginframee1,text='ID:',font=('arial',10,'bold'),bd=10,bg='cadet blue')
        self.lblid.grid(row=0,column=0)
        self.txtid=Entry(self.loginframee1,font=('arial',10,'bold'),textvariable=self.ID)
        self.txtid.grid(row=0,column=1)
        self.lblname=Label(self.loginframee1,text='Name:',font=('arial',10,'bold'),bd=20,bg='cadet blue')
        self.lblname.grid(row=1,column=0)
        self.txtname=Entry(self.loginframee1,font=('arial',10,'bold'),textvariable=self.Name)
        self.txtname.grid(row=1,column=1)
        self.lblDept_name=Label(self.loginframee1,text='Dept_name:',font=('arial',10,'bold'),bd=10,bg='cadet blue')
        self.lblDept_name.grid(row=2,column=0)
        self.txtDept_name=Entry(self.loginframee1,font=('arial',10,'bold'),textvariable=self.Dept_name)
        self.txtDept_name.grid(row=2,column=1)
        self.lblsalary=Label(self.loginframee1,text='Salary:',font=('arial',10,'bold'),bd=20,bg='cadet blue')
        self.lblsalary.grid(row=3,column=0)
        self.txtsalary=Entry(self.loginframee1,font=('arial',10,'bold'),textvariable=self.Salary)
        self.txtsalary.grid(row=3,column=1)
          #===============================button==add teacher====================
        self.btnadd=Button(self.loginframee2,width=17,font=('arial',10,'bold'), text="Add",command=self.insert1)
        self.btnadd.grid(row=3,column=0)
        self.btnreset=Button(self.loginframee2,width=17,font=('arial',10,'bold'), text="Reset",command=self.reset1)
        self.btnreset.grid(row=3,column=1)
          #==============================Add student===================================
        self.St_ID=StringVar()
        self.St_Name=StringVar()
        self.Dept_name1=StringVar()
        self.Credit=StringVar()
        self.frame2=Frame(self.master,bg='powder blue')
        self.frame2.pack(side=LEFT,fill=Y)
        self.lbltitle2=Label(self.frame2,text='Add Student',font=('arial',15,'bold'),bg='powder blue',fg='black')
        self.lbltitle2.grid(row=0,column=0,columnspan=2,pady=40)
        #===============================frames in add student==================================
        self.loginframeee1=LabelFrame(self.frame2,width=600,height=300,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframeee1.grid(row=1,column=0)
        self.loginframeee2=LabelFrame(self.frame2,width=350,height=100,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframeee2.grid(row=2,column=0)
        self.loginframeee3=LabelFrame(self.frame2,width=350,height=100,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframeee3.grid(row=3,column=0)
         #============================labels and entry=====add student================
        self.lblid3=Label(self.loginframeee1,text='ID:',font=('arial',10,'bold'),bd=10,bg='cadet blue')
        self.lblid3.grid(row=0,column=0)
        self.txtid3=Entry(self.loginframeee1,font=('arial',10,'bold'),textvariable=self.St_ID)
        self.txtid3.grid(row=0,column=1)
        self.lblname1=Label(self.loginframeee1,text='Name:',font=('arial',10,'bold'),bd=20,bg='cadet blue')
        self.lblname1.grid(row=1,column=0)
        self.txtname1=Entry(self.loginframeee1,font=('arial',10,'bold'),textvariable=self.St_Name)
        self.txtname1.grid(row=1,column=1)
        self.lblDept_name1=Label(self.loginframeee1,text='Dept_name:',font=('arial',10,'bold'),bd=10,bg='cadet blue')
        self.lblDept_name1.grid(row=2,column=0)
        self.txtDept_name1=Entry(self.loginframeee1,font=('arial',10,'bold'),textvariable=self.Dept_name1)
        self.txtDept_name1.grid(row=2,column=1)
        self.lbltot_cred=Label(self.loginframeee1,text='Credit:',font=('arial',10,'bold'),bd=20,bg='cadet blue')
        self.lbltot_cred.grid(row=3,column=0)
        self.txttot_cred=Entry(self.loginframeee1,font=('arial',10,'bold'),textvariable=self.Credit)
        self.txttot_cred.grid(row=3,column=1)
          #===============================button==add student====================
        self.btnadd=Button(self.loginframeee2,width=17,font=('arial',10,'bold'), text="Add",command=self.insert2)
        self.btnadd.grid(row=3,column=0)
        self.btnreset=Button(self.loginframeee2,width=17,font=('arial',10,'bold'), text="Reset",command=self.reset4)
        self.btnreset.grid(row=3,column=1)
               #==============================Assign course to instructor===================================
        self.ID1=StringVar()
        self.course_id1=StringVar()
        self.lbltitle2=Label(self.loginframe3,text='Assign course to instructor',font=('arial',15,'bold'),bg='powder blue',fg='black')
        self.lbltitle2.grid(row=0,column=0,columnspan=2,pady=10)
         #============================labels and entry=====Assign course to instructor================
        self.lblid1=Label(self.loginframe4,text='ID:',font=('arial',10,'bold'),bd=10,bg='cadet blue')
        self.lblid1.grid(row=0,column=0)
        self.txtid1=Entry(self.loginframe4,font=('arial',10,'bold'),textvariable=self.ID1)
        self.txtid1.grid(row=0,column=1)
        self.lblname1=Label(self.loginframe4,text='Course_id:',font=('arial',10,'bold'),bd=20,bg='cadet blue')
        self.lblname1.grid(row=1,column=0)
        self.txtname1=Entry(self.loginframe4,font=('arial',10,'bold'),textvariable=self.course_id1)
        self.txtname1.grid(row=1,column=1)
          #===============================button==Assign course to instructor====================
        self.btnadd=Button(self.loginframe5,width=17,font=('arial',10,'bold'), text="Add",command=self.insert3)
        self.btnadd.grid(row=3,column=0)
        self.btnreset=Button(self.loginframe5,width=17,font=('arial',10,'bold'), text="Reset",command=self.reset2)
        self.btnreset.grid(row=3,column=1)
               #==============================Assign instructor to student===================================
        self.s_id=StringVar()
        self.i_id=StringVar()
        self.lbltitle2=Label(self.loginframee3,text='Assign instructor to student',font=('arial',15,'bold'),bg='powder blue',fg='black')
        self.lbltitle2.grid(row=0,column=0,columnspan=2,pady=10)
         #============================labels and entry=====Assign instructor to student================
        self.lblid2=Label(self.loginframee4,text='S_ID:',font=('arial',10,'bold'),bd=10,bg='cadet blue')
        self.lblid2.grid(row=0,column=0)
        self.txtid2=Entry(self.loginframee4,font=('arial',10,'bold'),textvariable=self.s_id)
        self.txtid2.grid(row=0,column=1)
        self.lblname2=Label(self.loginframee4,text='I_ID:',font=('arial',10,'bold'),bd=20,bg='cadet blue')
        self.lblname2.grid(row=1,column=0)
        self.txtname2=Entry(self.loginframee4,font=('arial',10,'bold'),textvariable=self.i_id)
        self.txtname2.grid(row=1,column=1)
          #===============================button==Assign instructor to student====================
        self.btnadd=Button(self.loginframee5,width=17,font=('arial',10,'bold'), text="Add",command=self.insert4)
        self.btnadd.grid(row=3,column=0)
        self.btnreset=Button(self.loginframee5,width=17,font=('arial',10,'bold'), text="Reset",command=self.reset3)
        self.btnreset.grid(row=3,column=1)
        #====================================BACK============================
        self.btnback=Button(self.loginframeee3,width=17,font=('arial',10,'bold'), text="Back",command=self.back)
        self.btnback.grid(row=3,column=0)
    def insert(self):
        global x
        id1 = self.course_id.get()
        title1 =self.title.get()
        dept_name1 =self.dept_name.get()
        credit1 =self.credits.get()
        self.conn =sqlite3.connect('my_sqlproject.db')
        with self.conn:
            self.cursor = self.conn.cursor()
            self.cursor.execute('SELECT COUNT(*) FROM Admin WHERE ID=? and dept_name=?',(x,dept_name1,))
            check=self.cursor.fetchone()[0]
            if(check==1):
                self.cursor.execute('SELECT COUNT(*) FROM course WHERE course_id=?',(id1,))
                check1=self.cursor.fetchone()[0]
                if(check1==0):
                    self.cursor.execute('INSERT INTO course(course_id,title,dept_name,credits) VALUES(?,?,?,?)',(id1,title1,dept_name1,credit1,))
                    db.close()
                else:
                    tkinter.messagebox.askyesno("Insert to system","This course_id already inserted")
                    self.course_id.set("")
                    self.txtcourse_id.focus()
            else:
                tkinter.messagebox.askyesno("Check system","You can't change another department")
                self.course_id.set("")
                self.txtcourse_id.focus()
    def insert1(self):
        global x
        id2 = self.ID.get()
        title2 =self.Name.get()
        dept_name2 =self.Dept_name.get()
        salary2 =self.Salary.get()
        self.conn =sqlite3.connect('my_sqlproject.db')
        with self.conn:
            self.cursor = self.conn.cursor()
            self.cursor.execute('SELECT COUNT(*) FROM Admin WHERE ID=? and dept_name=?',(x,dept_name2,))
            check=self.cursor.fetchone()[0]
            if(id2[0]=='1' and id2[1]=='9'):
                if(check==1):
                    self.cursor.execute('SELECT COUNT(*) FROM instructor WHERE ID=?',(id2,))
                    check1=self.cursor.fetchone()[0]
                    if(check1==0):
                        self.cursor.execute('INSERT INTO instructor(ID,name,dept_name,salary) VALUES(?,?,?,?)',(id2,title2,dept_name2,salary2))
                        db.close()
                    else:
                        tkinter.messagebox.askyesno("Insert to system","This ID already inserted")
                        self.ID.set("")
                        self.txtid.focus()
                else:
                    tkinter.messagebox.askyesno("Check system","You can't change another department")
                    self.course_id.set("")
                    self.txtcourse_id.focus()
            else:
                tkinter.messagebox.askyesno("Check system","Instructor Id starts with 19")
    def insert2(self):
        id3 = self.St_ID.get()
        title3 =self.St_Name.get()
        dept_name3 =self.Dept_name1.get()
        tot_credit3 =self.Credit.get()
        self.conn =sqlite3.connect('my_sqlproject.db')
        with self.conn:
            self.cursor = self.conn.cursor()
            self.cursor.execute('SELECT COUNT(*) FROM Admin WHERE ID=? and dept_name=?',(x,dept_name3,))
            check=self.cursor.fetchone()[0]
            if(id3[0]=='1' and id3[1]=='7'):
                if(check==1):
                    self.cursor.execute('SELECT COUNT(*) FROM student WHERE ID=?',(id3,))
                    check1=self.cursor.fetchone()[0]
                    if(check1==0):
                        self.cursor.execute('INSERT INTO student(ID,name,dept_name,tot_credit) VALUES(?,?,?,?)',(id3,title3,dept_name3,tot_credit3))
                        db.close()
                    else:
                        tkinter.messagebox.askyesno("Insert to system","This ID already inserted")
                        self.St_ID.set("")
                        self.txtid3.focus()
                else:
                    tkinter.messagebox.askyesno("Check system","You can't change another department")
                    self.course_id.set("")
                    self.txtcourse_id.focus()
            else:
                tkinter.messagebox.askyesno("Check system","Student Id starts with 17")
    def insert3(self):
        ins_id4 = self.ID1.get()
        course_id4 =self.course_id1.get()
        self.conn =sqlite3.connect('my_sqlproject.db')
        with self.conn:
            self.cursor = self.conn.cursor()
            self.cursor.execute('SELECT COUNT(*) FROM instructor WHERE ID=?',(ins_id4,))
            check=self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM course WHERE course_id=?',(course_id4,))
            check1=self.cursor.fetchone()[0]
            if(check==1 and check1==1):
                self.cursor.execute('INSERT INTO teaches(ID,course_id) VALUES(?,?)',(ins_id4,course_id4))
                db.close()
            else:
                tkinter.messagebox.askyesno("Check to system","Invalid ID or course_id")
                self.ID1.set("")
                self.txtid1.focus()
    def insert4(self):
        s_id5 = self.s_id.get()
        i_id5 =self.i_id.get()
        self.conn =sqlite3.connect('my_sqlproject.db')
        with self.conn:
            self.cursor = self.conn.cursor()
            self.cursor.execute('SELECT COUNT(*) FROM student WHERE ID=?',(s_id5,))
            check=self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM instructor WHERE ID=?',(i_id5,))
            check1=self.cursor.fetchone()[0]
            if(check==1 and check1==1):
                self.cursor.execute('INSERT INTO Advisor(s_id,i_id) VALUES(?,?)',(s_id5,i_id5))
                db.close()
            else:
                tkinter.messagebox.askyesno("Check to system","Invalid student_id or inst_id")
                self.s_id.set("")
                self.txtid2.focus()
                self.i_id.set("")
                self.txtname2.focus()
    def reset(self):
        self.course_id.set("")
        self.title.set("")
        self.dept_name.set("")
        self.credits.set("")
        self.txtcourse_id.focus()
        self.txttitle.focus()
        self.txtdept_name.focus()
        self.txtcredit.focus()
    def reset1(self):
        self.ID.set("")
        self.Name.set("")
        self.Dept_name.set("")
        self.Salary.set("")
        self.txtid.focus()
        self.txtname.focus()
        self.txtDept_name.focus()
        self.txtsalary.focus()
    def reset4(self):
        self.St_ID.set("")
        self.St_Name.set("")
        self.Dept_name1.set("")
        self.Credit.set("")
        self.txtid3.focus()
        self.txtname1.focus()
        self.txtDept_name1.focus()
        self.txttot_cred.focus()
    def reset2(self):
        self.ID1.set("")
        self.course_id1.set("")
        self.txtid1.focus()
        self.txtname1.focus()
    def reset3(self):
        self.s_id.set("")
        self.i_id.set("")
        self.txtid2.focus()
        self.txtname1.focus()
    def back(self):
        global a
        a.update()
        a.deiconify()
        self.master.destroy()
class window3:
    def __init__(self,master):
        self.master=master
        self.master.title("Instructor")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="powder blue")
        self.frame=Frame(self.master,bg='powder blue')
        self.frame.pack(side=LEFT,fill=Y)
        self.frame1=Frame(self.master,bg='powder blue')
        self.frame1.pack(side=LEFT,fill=Y)
        self.frame2=Frame(self.master,bg='powder blue')
        self.frame2.pack(side=LEFT,fill=Y)
        self.Id=StringVar()
        self.course_id=StringVar()

        self.student_id1=StringVar()
        self.course_id1=StringVar()

        self.lbltitle=Label(self.frame,text='Update and see',font=('arial',15,'bold'),bg='powder blue',fg='black')
        self.lbltitle.grid(row=0,column=0,columnspan=2,pady=40)
        #===============================see and update==================================
        self.loginframe1=LabelFrame(self.frame,width=600,height=300,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframe1.grid(row=1,column=0)
        self.loginframe2=LabelFrame(self.frame,width=350,height=100,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframe2.grid(row=2,column=0)
        #============================labels and entry=====See and update================
        self.lblcourse_id=Label(self.loginframe1,text='ID:',font=('arial',10,'bold'),bd=10,bg='cadet blue')
        self.lblcourse_id.grid(row=0,column=0)
        self.txtcourse_id=Entry(self.loginframe1,font=('arial',10,'bold'),textvariable=self.Id)
        self.txtcourse_id.grid(row=0,column=1)
        self.lbltitle=Label(self.loginframe1,text='Update Name:',font=('arial',10,'bold'),bd=20,bg='cadet blue')
        self.lbltitle.grid(row=1,column=0)
        self.txttitle=Entry(self.loginframe1,font=('arial',10,'bold'),textvariable=self.course_id)
        self.txttitle.grid(row=1,column=1)

        #=========================btn update=====================
        self.btnadd=Button(self.loginframe2,width=17,font=('arial',10,'bold'), text="Update",command=self.update)
        self.btnadd.grid(row=3,column=0)
        self.btnreset=Button(self.loginframe2,width=17,font=('arial',10,'bold'), text="Show",command=self.show2)
        self.btnreset.grid(row=3,column=1)
        #========================See the courses=====================
        self.lbltitle2=Label(self.frame1,text='See courses',font=('arial',15,'bold'),bg='powder blue',fg='black')
        self.lbltitle2.grid(row=0,column=0,columnspan=2,pady=40)
        self.loginframee1=LabelFrame(self.frame1,font=('arial',10,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframee1.grid(row=1,column=0)
        self.loginframee2=LabelFrame(self.frame1,width=350,height=100,font=('arial',10,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframee2.grid(row=2,column=0)
        self.loginframe4=LabelFrame(self.frame1,width=350,height=100,font=('arial',10,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframe4.grid(row=4,column=0)
        self.loginframe5=LabelFrame(self.frame1,width=350,height=100,font=('arial',10,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframe5.grid(row=5,column=0)
        #=====================label========see=========================
        self.lblid1=Label(self.loginframee1,text='Courses assigned to you:',font=('arial',20,'bold'),bd=10,bg='cadet blue')
        self.lblid1.grid(row=0,column=0)
        self.lblid1=Label(self.loginframe4,text='Course Info, List of students:',font=('arial',20,'bold'),bd=10,bg='cadet blue')
        self.lblid1.grid(row=3,column=0)
        #======================btn== see===============================
        self.btnadd=Button(self.loginframee2,width=17,font=('arial',10,'bold'), text="Show",command=self.show)
        self.btnadd.grid(row=1,column=0)
        self.btnadd=Button(self.loginframe5,width=17,font=('arial',10,'bold'), text="Show",command=self.show1)
        self.btnadd.grid(row=4,column=0)
        #===========================register======================
        self.lbltitle=Label(self.frame2,text='Register',font=('arial',15,'bold'),bg='powder blue',fg='black')
        self.lbltitle.grid(row=0,column=0,columnspan=2,pady=40)
        #============================================
        self.loginframeee1=LabelFrame(self.frame2,width=600,height=300,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframeee1.grid(row=1,column=0)
        self.loginframeee2=LabelFrame(self.frame2,width=350,height=100,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframeee2.grid(row=2,column=0)
        #===================================================================
        self.lblstudent_id=Label(self.loginframeee1,text='Student_ID:',font=('arial',10,'bold'),bd=20,bg='cadet blue')
        self.lblstudent_id.grid(row=0,column=0)
        self.txtstudent_id=Entry(self.loginframeee1,font=('arial',10,'bold'),textvariable=self.student_id1)
        self.txtstudent_id.grid(row=0,column=1)
        self.lblcourse_id1=Label(self.loginframeee1,text='Course_ID',font=('arial',10,'bold'),bd=10,bg='cadet blue')
        self.lblcourse_id1.grid(row=1,column=0)
        self.txtcourse_id1=Entry(self.loginframeee1,font=('arial',10,'bold'),textvariable=self.course_id1)
        self.txtcourse_id1.grid(row=1,column=1)
        #===================================================================
        self.btnadd=Button(self.loginframeee2,width=17,font=('arial',10,'bold'), text="Register",command=self.insert)
        self.btnadd.grid(row=2,column=0)
        #=================back============================
        self.btnback=Button(self.frame1,width=17,font=('arial',15,'bold'), text="Back",command=self.back)
        self.btnback.grid(row=6,columnspan=2)
    def update(self):
        global x
        id1=self.Id.get()
        crs1=self.course_id.get()
        self.con=sqlite3.connect('my_sqlproject.db')
        self.cursor=self.con.cursor()
        if(id1==x):
            self.cursor.execute("UPDATE instructor SET name=? WHERE ID=?",(crs1,id1))
            self.con.commit()
        else:
            tkinter.messagebox.askyesno("Update"," Incorrect id! ")
            self.Id.set("")
            self.txtcourse_id.focus()
    def show(self):
        global x
        self.conn =sqlite3.connect('my_sqlproject.db')
        with self.conn:
            self.cursor = self.conn.cursor()
            self.cursor.execute('SELECT * FROM teaches WHERE ID=?',(x,))
            print("  ID    course_id")
            for row in self.cursor.fetchall():
                print(row)
            db.close()
    def show1(self):
        global x
        self.conn =sqlite3.connect('my_sqlproject.db')
        with self.conn:
            self.cursor = self.conn.cursor()
            self.cursor.execute('SELECT name,'
                'takes.course_id FROM student,takes,teaches where teaches.ID=? and '
                'takes.ID=student.ID and takes.course_id=teaches.course_id',(x,))
            print("std_name course_id")
            for row in self.cursor.fetchall():
                print(row)
            db.close()
    def show2(self):
        global x
        self.conn =sqlite3.connect('my_sqlproject.db')
        with self.conn:
            self.cursor = self.conn.cursor()
            print("   ID       Name   Dept_name  Salary")
            self.cursor.execute('SELECT * FROM instructor WHERE ID=?',(x,))
            for row in self.cursor.fetchall():
                print(row)
            db.close()
    def insert(self):
        id1 = self.student_id1.get()
        crs1 =self.course_id1.get()
        self.conn =sqlite3.connect('my_sqlproject.db')
        with self.conn:
            self.cursor = self.conn.cursor()
            self.cursor.execute('select count(*) from student where ID=?',(id1,))
            check=self.cursor.fetchone()[0]
            self.cursor.execute('select count(*) from course where course_id=?',(crs1,))
            check1=self.cursor.fetchone()[0]
            if(check==1 and check1==1):
                self.cursor.execute('INSERT INTO takes(ID,course_id) VALUES(?,?)',(id1,crs1,))
                db.close()
            else:
                tkinter.messagebox.askyesno("Registration"," Incorrect student id"
                                                           " or course_id !")
    def back(self):
        global a
        a.update()
        a.deiconify()
        self.master.destroy()
class window4:
    def __init__(self,master):
        self.master=master
        self.master.title("Student")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="powder blue")
        self.frame=Frame(self.master,bg='powder blue')
        self.frame.pack()
        self.frame1=Frame(self.master,bg='powder blue')
        self.frame1.pack()
        self.Id=StringVar()
        self.course_id=StringVar()
        self.lbltitle=Label(self.frame,text='See and Update',font=('arial',15,'bold'),bg='powder blue',fg='black')
        self.lbltitle.grid(row=0,column=0,columnspan=2)
        #===============================see and update==================================
        self.loginframe1=LabelFrame(self.frame,width=600,height=300,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframe1.grid(row=1,column=0)
        self.loginframe2=LabelFrame(self.frame,width=350,height=100,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframe2.grid(row=2,column=0)
        #============================labels and entry=====See and update================
        self.lblcourse_id=Label(self.loginframe1,text='ID:',font=('arial',10,'bold'),bd=10,bg='cadet blue')
        self.lblcourse_id.grid(row=0,column=0)
        self.txtcourse_id=Entry(self.loginframe1,font=('arial',10,'bold'),textvariable=self.Id)
        self.txtcourse_id.grid(row=0,column=1)
        self.lbltitle=Label(self.loginframe1,text='Update Name:',font=('arial',10,'bold'),bd=20,bg='cadet blue')
        self.lbltitle.grid(row=1,column=0)
        self.txttitle=Entry(self.loginframe1,font=('arial',10,'bold'),textvariable=self.course_id)
        self.txttitle.grid(row=1,column=1)
         #=========================btn update=====================
        self.btnadd=Button(self.loginframe2,width=17,font=('arial',10,'bold'), text="Update",command=self.update)
        self.btnadd.grid(row=3,column=0)
        self.btnreset=Button(self.loginframe2,width=17,font=('arial',10,'bold'), text="Show",command=self.show2)
        self.btnreset.grid(row=3,column=1)
         #========================See the courses=====================
        self.loginframee1=LabelFrame(self.frame1,font=('arial',10,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframee1.grid(row=1,column=0)
        self.loginframee2=LabelFrame(self.frame1,width=350,height=100,font=('arial',10,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframee2.grid(row=2,column=0)
        self.loginframe4=LabelFrame(self.frame1,width=350,height=100,font=('arial',10,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframe4.grid(row=4,column=0)
        self.loginframe5=LabelFrame(self.frame1,width=350,height=100,font=('arial',10,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframe5.grid(row=5,column=0)
        #=====================label========see=========================
        self.lblid1=Label(self.loginframee1,text='Student Courses:',font=('arial',20,'bold'),bd=10,bg='cadet blue')
        self.lblid1.grid(row=0,column=0)
        self.lblid1=Label(self.loginframe4,text='Registered Students:',font=('arial',20,'bold'),bd=10,bg='cadet blue')
        self.lblid1.grid(row=2,column=0)
        #======================btn== see===============================
        self.btnadd=Button(self.loginframee2,width=17,font=('arial',10,'bold'), text="Show",command=self.show)
        self.btnadd.grid(row=1,column=0)
        self.btnadd=Button(self.loginframe5,width=17,font=('arial',10,'bold'), text="Show",command=self.show1)
        self.btnadd.grid(row=4,column=0)
        #==================================back===============================
        self.btnback=Button(self.frame1,width=17,font=('arial',15,'bold'), text="Back",command=self.back)
        self.btnback.grid(row=6,columnspan=2)
    def update(self):
        global x
        id1=self.Id.get()
        crs1=self.course_id.get()
        self.con=sqlite3.connect('my_sqlproject.db')
        self.cursor=self.con.cursor()
        if(id1==x):
            self.cursor.execute("UPDATE student SET name=? WHERE ID=?",(crs1,id1))
            self.con.commit()
        else:
            tkinter.messagebox.askyesno("Update"," Incorrect id! ")
            self.Id.set("")
            self.txtcourse_id.focus()
    def show(self):
        global x
        self.conn =sqlite3.connect('my_sqlproject.db')
        with self.conn:
            self.cursor = self.conn.cursor()
            print("  ID    Course_Id")
            self.cursor.execute('SELECT * FROM takes WHERE ID=?',(x,))
            for row in self.cursor.fetchall():
                print(row)
            db.close()
    def show1(self):
        global x
        self.conn =sqlite3.connect('my_sqlproject.db')
        with self.conn:
            self.cursor = self.conn.cursor()
            self.cursor.execute('SELECT dept_name FROM student where ID=?',(x,))
            check=self.cursor.fetchone()[0]
            self.cursor.execute('SELECT * FROM student where dept_name=?',(check,))
            print("List of registered students in your class:")
            print("Student_Id  Name   Dept_name   Total_credit")
            for row in self.cursor.fetchall():
                print(row)
            db.close()
    def show2(self):
        global x
        self.conn =sqlite3.connect('my_sqlproject.db')
        with self.conn:
            self.cursor = self.conn.cursor()
            self.cursor.execute('SELECT * FROM student WHERE ID=?',(x,))
            print("   ID       Name   Dept_name  Tot_credit")
            for row in self.cursor.fetchall():
                print(row)
            db.close()
    def back(self):
        a.update()
        a.deiconify()
        self.master.destroy()
main()
