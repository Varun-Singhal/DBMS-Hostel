import tkinter
from tkinter import *
import student
import prof
import MySQLdb as sql
import staff_set
import matplotlib.pyplot as plt
class home_principal:
	def __init__(self,con,staffid='1jb111'):
		self.root=tkinter.Tk()
		self.con=con
		self.staffid=staffid
		self.root.geometry("{}x{}".format(900,640))
		self.count=0
		self.root.title("SJBIT Hostel")
		heading=Label(self.root,text="SJBIT Hostel Management",font="Helvetical 40 ")
		heading.place(x=100,y=10)
		self.createmenu()
		self.root.mainloop()
	def createmenu(self):
		self.con.close()
		self.con=sql.connect(host='localhost',user='root',passwd='hwp@7299',db='hostel')
		self.con.query('select * from staff where(staffid="'+self.staffid+'");')
		self.data=self.con.store_result()
		self.data=self.data.fetch_row()
		self.greet=Label(self.root,text=("Welcome "+str(self.data[0][1])),font="Helvetical 15")
		self.greet.place(x=350,y=60)
		self.show()
		self.stu1=Button(self.root,text="Student Details",width=20,font="Helvetical 10",command=lambda:self.student(1))
		self.stu1.place(x=15,y=130)
		self.stu2=Button(self.root,text="Add Student",font="Helvetical 10",width=20,command=lambda:self.student(2))
		self.stu2.place(x=15,y=170)
		self.stu3=Button(self.root,text="Remove Student",font="Helvetical 10",width=20,command=lambda:self.student(3))
		self.stu3.place(x=15,y=210)
		self.stu4=Button(self.root,text="Alter Student Details",font="Helvetical 10",width=20,command=lambda:self.student(4))
		self.stu4.place(x=15,y=250)
		self.stu5=Button(self.root,text="FEE Status",font="Helvetical 10",width=20,command=lambda:self.student(5))
		self.stu5.place(x=15,y=290)
		self.stu6=Button(self.root,text="Fine Details",font="Helvetical 10",width=20,command=lambda:self.student(6))
		self.stu6.place(x=15,y=330)
		self.stu7=Button(self.root,text="Report Student",font="Helvetical 10",width=20,command=lambda:self.student(7))
		self.stu7.place(x=15,y=370)
		self.stu8=Button(self.root,text="Collect Fine",font="Helvetical 10",width=20,command=lambda:self.student(8))
		self.stu8.place(x=15,y=410)
		self.stu9=Button(self.root,text="Add Visitor",font="Helvetical 10",width=20,command=lambda:self.student(9))
		self.stu9.place(x=700,y=130)
		self.stu10=Button(self.root,text="Visitor Details",font="Helvetical 10",width=20,command=lambda:self.student(10))
		self.stu10.place(x=700,y=170)
		self.staff1=Button(self.root,text="Staff Details",font="Helvetical 10",width=20,command=lambda:self.staff(1))
		self.staff1.place(x=700,y=250)
		self.staff2=Button(self.root,text="Alter Staff Details",font="Helvetical 10",width=20,command=lambda:self.staff(2))
		self.staff2.place(x=700,y=290)
		self.staff3=Button(self.root,text="Remove Staff",font="Helvetical 10",width=20,command=lambda:self.staff(3))
		self.staff3.place(x=700,y=330)
		self.staff6=Button(self.root,text="Add Staff",font="Helvetical 10",width=20,command=lambda:self.staff(4))
		self.staff6.place(x=700,y=370)
		self.staff4=Button(self.root,text="My Profile",font="Helvetical 10",width=20,command=self.profile)
		self.staff4.place(x=15,y=480)
		self.staff5=Button(self.root,text="Logout",font="Helvetical 10",width=20,command=self.root.destroy)
		self.staff5.place(x=15,y=520)
	def fetch_staff(self,flag):
		self.temp_data=self.widget.get()
		self.con.close()
		self.con=sql.connect(host='localhost',user='root',passwd='hwp@7299',db='hostel')
		self.con.query("select staffid from password where(staffid='"+self.temp_data+"');")
		self.temp_data=self.con.store_result()
		self.temp_data=self.temp_data.fetch_row()
		if(self.temp_data):
			if(flag==1):
				self.head.destroy()
				l=staff_set.details(self.con,self.temp_data[0][0])
			elif(flag==2):
				self.head.destroy()
				l=staff_set.alter(self.con,self.temp_data[0][0])
			elif(flag==3):
				self.head.destroy()
				l=staff_set.remove(self.con,self.temp_data[0][0])
					
		else:
			self.head.destroy()
			self.head=tkinter.Tk()
			self.head.title("Error")
			self.head.geometry("{}x{}".format(150,150))
			x=Label(self.head,text="Invalid StaffID")
			x.place(x=10,y=20)
			self.head.mainloop()
	def show(self):
		self.con.query("call attendance_min();")
		x=self.con.store_result()
		x=x.fetch_row()
		self.con.close()
		self.con=sql.connect(host='localhost',user='root',passwd='hwp@7299',db='hostel')
		self.con.query("select pic,usn from student where(attendance="+str(x[0][0])+");")
		x=self.con.store_result()
		x=x.fetch_row()
		self.ll=PhotoImage(file=x[0][0])
		self.ll=self.ll.zoom(25)
		self.ll=self.ll.subsample(40)
		self.o=Label(self.root,image=self.ll)
		self.o.place(x=500,y=145)
		self.o=Label(self.root,text="Student (minimum Attendance)" ,font="Helvetical 10")
		self.o.place(x=450,y=120)
		self.o=Label(self.root,text=x[0][1] ,font="Helvetical 12")
		self.o.place(x=530,y=295)
		self.con.query("call visitor_max();")
		x=self.con.store_result()
		x=x.fetch_row()
		self.con.close()
		self.con=sql.connect(host='localhost',user='root',passwd='hwp@7299',db='hostel')
		self.con.query("select pic,usn from student where(visitor_count="+str(x[0][0])+");")
		x=self.con.store_result()
		x=x.fetch_row()
		self.lp=PhotoImage(file=x[0][0])
		self.lp=self.lp.zoom(25)
		self.lp=self.lp.subsample(40)
		self.o=Label(self.root,image=self.lp)
		self.o.place(x=260,y=145)
		self.o=Label(self.root,text="Student (miximum visitors)" ,font="Helvetical 9")
		self.o.place(x=230,y=120)
		self.o=Label(self.root,text=x[0][1] ,font="Helvetical 12")
		self.o.place(x=290,y=295)	
		self.con.query("select max(reported) from staff;")
		x=self.con.store_result()
		x=x.fetch_row()
		self.con.query("select pic,staffid from staff where(reported="+str(x[0][0])+");")
		x=self.con.store_result()
		x=x.fetch_row()
		self.lz=PhotoImage(file=x[0][0])
		self.lz=self.lz.zoom(25)
		self.lz=self.lz.subsample(40)
		self.o=Label(self.root,image=self.lz)
		self.o.place(x=330,y=400)
		self.o=Label(self.root,text="Staff (maximum Reported)" ,font="Helvetical 10")
		self.o.place(x=335,y=380)
		self.o=Label(self.root,text=x[0][1] ,font="Helvetical 12")
		self.o.place(x=395,y=600)
	def staff(self,flag):
		if(flag==4):
			staff_set.add()
		else:
			self.head=tkinter.Tk()
			self.head.geometry("{}x{}".format(300,300))
			x=Label(self.head,text="Enter Staff ID")
			x.place(x=10,y=20)
			self.head.title("Staff ID")
			self.widget=Entry(self.head,width=13)
			button=Button(self.head,text="Submit",command=lambda:self.fetch_staff(flag))
			self.widget.place(x=10,y=50)
			button.place(x=10,y=100)
			self.head.mainloop()
	def fetch(self,flag):
			self.temp_data=self.widget.get()
			self.con.close()
			self.con=sql.connect(host='localhost',user='root',passwd='hwp@7299',db='hostel')
			self.con.query("select usn from student where(usn='"+self.temp_data+"');")
			self.temp_data=self.con.store_result()
			self.temp_data=self.temp_data.fetch_row()
			if(self.temp_data):
				self.head.destroy()
				if(flag==1):
					l=student.detail(self.con,self.temp_data[0][0])
				elif(flag==3):
					l=student.remove(self.con,self.temp_data[0][0])
				elif(flag==4):
					l=student.alter(self.con,self.temp_data[0][0])
				elif(flag==5):
					l=student.fees(self.con,self.temp_data[0][0])
				elif(flag==6):
					l=student.fine(self.con,self.temp_data[0][0])
				elif(flag==7):
					l=student.report(self.con,self.temp_data[0][0],self.staffid)
				elif(flag==8):
					l=student.collect_fine(self.con,self.temp_data[0][0])
				elif(flag==9):
					l=student.add_visitor(self.con,self.temp_data[0][0])
				else:
					l=student.vis_detail(self.con,self.temp_data[0][0])
			else:
				self.head.destroy()
				self.head=tkinter.Tk()
				self.head.title("Error")
				self.head.geometry("{}x{}".format(150,150))
				x=Label(self.head,text="Invalid USN")
				x.place(x=10,y=20)
				self.head.mainloop()
	def student(self,flag):
		if(flag==2):
				l=student.add(self.con)
		else:
			self.head=tkinter.Tk()
			self.head.geometry("{}x{}".format(300,300))
			x=Label(self.head,text="Enter Student's USN")
			x.place(x=10,y=20)
			self.head.title("Student's Details")
			self.widget=Entry(self.head,width=13)
			button=Button(self.head,text="Submit",command=lambda:self.fetch(flag))
			self.widget.place(x=10,y=50)
			button.place(x=10,y=100)
			self.head.mainloop()
	def profile(self):
		prof.profile_manage(self.con,self.staffid)
class home:
	def __init__(self,con,staffid):
		self.root=tkinter.Tk()
		self.con=con
		self.staffid=staffid
		self.root.geometry("{}x{}".format(900,640))
		self.count=0
		self.root.title("SJBIT Hostel")
		heading=Label(self.root,text="SJBIT Hostel Management",font="Helvetical 40 ")
		heading.place(x=100,y=10)
		self.createmenu()
		self.root.mainloop()
	def show(self):
		self.con.close()
		self.con=sql.connect(host='localhost',user='root',passwd='hwp@7299',db='hostel')
		self.con.query("call attendance_min();")
		x=self.con.store_result()
		x=x.fetch_row()
		self.con.close()
		self.con=sql.connect(host='localhost',user='root',passwd='hwp@7299',db='hostel')
		self.con.query("select pic,usn from student where(attendance="+str(x[0][0])+");")
		x=self.con.store_result()
		x=x.fetch_row()
		self.ll=PhotoImage(file=x[0][0])
		self.ll=self.ll.zoom(25)
		self.ll=self.ll.subsample(40)
		self.o=Label(self.root,image=self.ll)
		self.o.place(x=500,y=145)
		self.o=Label(self.root,text="Student (minimum Attendance)" ,font="Helvetical 10")
		self.o.place(x=450,y=120)
		self.o=Label(self.root,text=x[0][1] ,font="Helvetical 12")
		self.o.place(x=530,y=295)
		self.con.query("call visitor_max();")
		x=self.con.store_result()
		x=x.fetch_row()
		self.con.close()
		self.con=sql.connect(host='localhost',user='root',passwd='hwp@7299',db='hostel')
		self.con.query("select pic,usn from student where(visitor_count="+str(x[0][0])+");")
		x=self.con.store_result()
		x=x.fetch_row()
		self.lp=PhotoImage(file=x[0][0])
		self.lp=self.lp.zoom(25)
		self.lp=self.lp.subsample(40)
		self.o=Label(self.root,image=self.lp)
		self.o.place(x=260,y=145)
		self.o=Label(self.root,text="Student (miximum visitors)" ,font="Helvetical 9")
		self.o.place(x=230,y=120)
		self.o=Label(self.root,text=x[0][1] ,font="Helvetical 12")
		self.o.place(x=290,y=295)	
		self.con.query("select max(reported) from staff;")
		x=self.con.store_result()
		x=x.fetch_row()
		self.con.query("select pic,staffid from staff where(reported="+str(x[0][0])+");")
		x=self.con.store_result()
		x=x.fetch_row()
		self.lz=PhotoImage(file=x[0][0])
		self.lz=self.lz.zoom(25)
		self.lz=self.lz.subsample(40)
		self.o=Label(self.root,image=self.lz)
		self.o.place(x=330,y=400)
		self.o=Label(self.root,text="Staff (maximum Reported)" ,font="Helvetical 10")
		self.o.place(x=335,y=380)
		self.o=Label(self.root,text=x[0][1] ,font="Helvetical 12")
		self.o.place(x=395,y=600)
	def createmenu(self):
		self.con.query('select * from staff where(staffid="'+self.staffid+'");')
		self.data=self.con.store_result()
		self.data=self.data.fetch_row()
		self.show()
		self.greet=Label(self.root,text=("Welcome "+str(self.data[0][1])),font="Helvetical 15")
		self.greet.place(x=350,y=80)
		self.stu1=Button(self.root,text="Student Details",width=20,font="Helvetical 10",command=lambda:self.student(1))
		self.stu1.place(x=15,y=130)
		self.stu2=Button(self.root,text="Add Student",font="Helvetical 10",width=20,command=lambda:self.student(2))
		self.stu2.place(x=15,y=170)
		self.stu3=Button(self.root,text="Remove Student",font="Helvetical 10",width=20,command=lambda:self.student(3))
		self.stu3.place(x=15,y=210)
		self.stu4=Button(self.root,text="Alter Student Details",font="Helvetical 10",width=20,command=lambda:self.student(4))
		self.stu4.place(x=15,y=250)
		self.stu5=Button(self.root,text="FEE Status",font="Helvetical 10",width=20,command=lambda:self.student(5))
		self.stu5.place(x=15,y=290)
		self.stu6=Button(self.root,text="Fine Details",font="Helvetical 10",width=20,command=lambda:self.student(6))
		self.stu6.place(x=15,y=330)
		self.stu7=Button(self.root,text="Report Student",font="Helvetical 10",width=20,command=lambda:self.student(7))
		self.stu7.place(x=15,y=370)
		self.stu8=Button(self.root,text="Collect Fine",font="Helvetical 10",width=20,command=lambda:self.student(8))
		self.stu8.place(x=15,y=410)
		self.stu9=Button(self.root,text="Add Visitor",font="Helvetical 10",width=20,command=lambda:self.student(9))
		self.stu9.place(x=700,y=130)
		self.stu10=Button(self.root,text="Visitor Details",font="Helvetical 10",width=20,command=lambda:self.student(10))
		self.stu10.place(x=700,y=170)
		self.staff1=Button(self.root,text="Staff Details",font="Helvetical 10",width=20,command=lambda:self.staff(1))
		self.staff1.place(x=700,y=250)
		self.staff2=Button(self.root,text="Alter Staff Details",font="Helvetical 10",width=20,command=lambda:self.staff(2))
		self.staff2.place(x=700,y=290)
		self.staff3=Button(self.root,text="Remove Staff",font="Helvetical 10",width=20,command=lambda:self.staff(3))
		self.staff3.place(x=700,y=330)
		self.staff4=Button(self.root,text="My Profile",font="Helvetical 10",width=20,command=self.profile)
		self.staff4.place(x=15,y=480)
		self.staff5=Button(self.root,text="Logout",font="Helvetical 10",width=20,command=self.root.destroy)
		self.staff5.place(x=15,y=520)
	def fetch_staff(self,flag):
		self.temp_data=self.widget.get()
		self.con.query("select staffid from password where(staffid='"+self.temp_data+"');")
		self.temp_data=self.con.store_result()
		self.temp_data=self.temp_data.fetch_row()
		if(self.temp_data):
			if(flag==1):
				self.head.destroy()
				l=staff_set.details(self.con,self.temp_data[0][0])
			elif(flag==2):
				self.head.destroy()
				l=staff_set.alter(self.con,self.temp_data[0][0])
			elif(flag==3):
				if(self.temp_data[0][0] == "1jb111"):
					self.head.destroy()
					self.head=tkinter.Tk()
					self.head.title("Error")
					self.head.geometry("{}x{}".format(200,150))
					x=Label(self.head,text="You cannot remove Principal")
					x.place(x=10,y=20)
					self.head.mainloop()
				else:
					self.head.destroy()
					l=staff_set.remove(self.con,self.temp_data[0][0])
					
		else:
			self.head.destroy()
			self.head=tkinter.Tk()
			self.head.title("Error")
			self.head.geometry("{}x{}".format(150,150))
			x=Label(self.head,text="Invalid StaffID")
			x.place(x=10,y=20)
			self.head.mainloop()
	def staff(self,flag):
		self.head=tkinter.Tk()
		self.head.geometry("{}x{}".format(300,300))
		x=Label(self.head,text="Enter Staff ID")
		x.place(x=10,y=20)
		self.head.title("Staff ID")
		self.widget=Entry(self.head,width=13)
		button=Button(self.head,text="Submit",command=lambda:self.fetch_staff(flag))
		self.widget.place(x=10,y=50)
		button.place(x=10,y=100)
		self.head.mainloop()
	def fetch(self,flag):
			self.temp_data=self.widget.get()
			self.con.query("select usn from student where(usn='"+self.temp_data+"');")
			self.temp_data=self.con.store_result()
			self.temp_data=self.temp_data.fetch_row()
			if(self.temp_data):
				self.head.destroy()
				if(flag==1):
					l=student.detail(self.con,self.temp_data[0][0])
				elif(flag==3):
					l=student.remove(self.con,self.temp_data[0][0])
				elif(flag==4):
					l=student.alter(self.con,self.temp_data[0][0])
				elif(flag==5):
					l=student.fees(self.con,self.temp_data[0][0])
				elif(flag==6):
					l=student.fine(self.con,self.temp_data[0][0])
				elif(flag==7):
					l=student.report(self.con,self.temp_data[0][0],self.staffid)
				elif(flag==8):
					l=student.collect_fine(self.con,self.temp_data[0][0])
				elif(flag==9):
					l=student.add_visitor(self.con,self.temp_data[0][0])
				else:
					l=student.vis_detail(self.con,self.temp_data[0][0])
			else:
				self.head.destroy()
				self.head=tkinter.Tk()
				self.head.title("Error")
				self.head.geometry("{}x{}".format(150,150))
				x=Label(self.head,text="Invalid USN")
				x.place(x=10,y=20)
				self.head.mainloop()
	def student(self,flag):
		if(flag==2):
				l=student.add(self.con)
		else:
			self.head=tkinter.Tk()
			self.head.geometry("{}x{}".format(300,300))
			x=Label(self.head,text="Enter Student's USN")
			x.place(x=10,y=20)
			self.head.title("Student's Details")
			self.widget=Entry(self.head,width=13)
			button=Button(self.head,text="Submit",command=lambda:self.fetch(flag))
			self.widget.place(x=10,y=50)
			button.place(x=10,y=100)
			self.head.mainloop()
	def profile(self):
		prof.profile_manage(self.con,self.staffid)
		