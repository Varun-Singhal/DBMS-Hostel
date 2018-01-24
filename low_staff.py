import tkinter as tk
from tkinter import *
import student
import staff_set
class lower_staff:
	def __init__(self,con,data):
		self.con=con
		self.staffid=data
		self.root=tk.Tk()
		self.root.title(data)
		self.root.geometry("{}x{}".format(500,500))
		self.a=Button(self.root,text="Student Details",command=self.student, width=15)
		self.a.place(x=150,y=20)
		self.b=Button(self.root,text="Staff Details",command=self.staff, width=15)
		self.b.place(x=150,y=50)
		self.c=Button(self.root,text="Report Student",command=self.report, width=15)
		self.c.place(x=150,y=80)
		self.d=Button(self.root,text="Logout",command=self.root.destroy,width=15)
		self.d.place(x=150,y=110)
		self.root.mainloop()
	def student(self):
			self.head=tk.Tk()
			self.head.geometry("{}x{}".format(300,300))
			x=Label(self.head,text="Enter Student's USN")
			x.place(x=10,y=20)
			self.head.title("Student's Details")
			self.widget=Entry(self.head,width=13)
			button=Button(self.head,text="Submit",command=self.fetch1)
			self.widget.place(x=10,y=50)
			button.place(x=10,y=100)
			self.head.mainloop()
	def fetch1(self):
			data=self.widget.get()
			self.head.destroy()
			student.detail(self.con,data)
	def report(self):
			self.head=tk.Tk()
			self.head.geometry("{}x{}".format(300,300))
			x=Label(self.head,text="Enter Student's USN")
			x.place(x=10,y=20)
			self.head.title("Student's Details")
			self.widget=Entry(self.head,width=13)
			button=Button(self.head,text="Submit",command=self.fetch)
			self.widget.place(x=10,y=50)
			button.place(x=10,y=100)
			self.head.mainloop()
	def fetch(self):
			data=self.widget.get()
			self.head.destroy()
			student.report(self.con,data,self.staffid)
	def staff(self):
		self.head=tk.Tk()
		self.head.geometry("{}x{}".format(300,300))
		x=Label(self.head,text="Enter Staff ID")
		x.place(x=10,y=20)
		self.head.title("Staff ID")
		self.widget=Entry(self.head,width=13)
		button=Button(self.head,text="Submit",command=self.fetch_staff)
		self.widget.place(x=10,y=50)
		button.place(x=10,y=100)
		self.head.mainloop()
	def fetch_staff(self):
		data=self.widget.get()
		self.head.destroy()
		staff_set.details(self.con,data)
		