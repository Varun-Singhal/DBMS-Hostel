import tkinter as tk
import MySQLdb as sql
from tkinter import *
class details:
	def __init__(self,con,data):
		self.con=con
		self.con.query("select * from staff where(staffid='"+data+"');")
		self.data=self.con.store_result()
		self.data=self.data.fetch_row()
		self.head=tk.Toplevel()
		self.head.title(self.data[0][0])
		f=self.data[0][10]
		self.head.geometry("{}x{}".format(800,400))
		self.pic=PhotoImage(file=f)
		self.pic1=Label(self.head,image=self.pic)
		self.pic1.place(x=500,y=20)
		staffid=Label(self.head,text="StaffID :",font="Helvetical 15")
		staffid.place(x=10,y=10)
		staffid=Label(self.head,text=self.data[0][0],font="Helvetical 15")
		staffid.place(x=200,y=10)
		name=Label(self.head,text="Name :",font="Helvetical 15")
		name.place(x=10,y=40)
		name=Label(self.head,text=self.data[0][1],font="Helvetical 15")
		name.place(x=200,y=40)
		phone=Label(self.head,text="Phone :",font="Helvetical 15")
		phone.place(x=10,y=70)
		phone=Label(self.head,text=str(self.data[0][2]),font="Helvetical 15")
		phone.place(x=200,y=70)
		address=Label(self.head,text="Address :",font="Helvetical 15")
		address.place(x=10,y=100)
		address=Label(self.head,text=self.data[0][3],font="Helvetical 15")
		address.place(x=200,y=100)
		DOB=Label(self.head,text="DOB :",font="Helvetical 15")
		DOB.place(x=10,y=130)
		dob=Label(self.head,text=str(self.data[0][4]),font="Helvetical 15")
		dob.place(x=200,y=130)
		Email=Label(self.head,text="Email :",font="Helvetical 15")
		Email.place(x=10,y=160)
		Email=Label(self.head,text=self.data[0][5],font="Helvetical 15")
		Email.place(x=200,y=160)
		Salary=Label(self.head,text="Salary : ",font="Helvetical 15")
		Salary.place(x=10,y=190)
		salary=Label(self.head,text=str(self.data[0][6]),font="Helvetical 15")
		salary.place(x=200,y=190)
		des=Label(self.head,text="Designation :",font="Helvetical 15")
		des.place(x=10,y=220)
		des=Label(self.head,text=self.data[0][7],font="Helvetical 15")
		des.place(x=200,y=220)
		rep=Label(self.head,text="Reported :",font="Helvetical 15")
		rep.place(x=10,y=250)
		reports=Label(self.head,text=self.data[0][8],font="Helvetical 15")
		reports.place(x=200,y=250)
		room=Label(self.head,text="Room-No :",font="Helvetical 15")
		room.place(x=10,y=280)
		roomn=Label(self.head,text=self.data[0][9],font="Helvetical 15")
		roomn.place(x=200,y=280)
		self.head.mainloop()
class alter:
	def __init__(self,con,data):
		self.con=con
		self.data=data
		self.con.query("select * from staff where(staffid='"+data+"');")
		self.data=self.con.store_result()
		self.data=self.data.fetch_row()
		self.head=tk.Toplevel()
		self.head.title(self.data[0][0])
		f=self.data[0][10]
		self.head.geometry("{}x{}".format(800,400))
		self.pic=PhotoImage(file=f)
		self.pic1=Label(self.head,image=self.pic)
		self.pic1.place(x=500,y=20)
		staffid=Label(self.head,text="StaffID :",font="Helvetical 15")
		staffid.place(x=10,y=10)
		staffid=Label(self.head,text=self.data[0][0],font="Helvetical 15")
		staffid.place(x=200,y=10)
		name=Label(self.head,text="Name :",font="Helvetical 15")
		name.place(x=10,y=40)
		name=Label(self.head,text=self.data[0][1],font="Helvetical 15")
		name.place(x=200,y=40)
		phone=Label(self.head,text="Phone :",font="Helvetical 15")
		phone.place(x=10,y=70)
		self.phone=Entry(self.head)
		self.phone.insert(0,str(self.data[0][2]))
		self.phone.place(x=200,y=70)
		address=Label(self.head,text="Address :",font="Helvetical 15")
		address.place(x=10,y=100)
		self.address=Entry(self.head)
		self.address.insert(0,self.data[0][3])
		self.address.place(x=200,y=100)
		DOB=Label(self.head,text="DOB :",font="Helvetical 15")
		DOB.place(x=10,y=130)
		dob=Label(self.head,text=str(self.data[0][4]),font="Helvetical 15")
		dob.place(x=200,y=130)
		Email=Label(self.head,text="Email :",font="Helvetical 15")
		Email.place(x=10,y=160)
		self.Email=Entry(self.head)
		self.Email.insert(0,self.data[0][5])
		self.Email.place(x=200,y=160)
		Salary=Label(self.head,text="Salary : ",font="Helvetical 15")
		Salary.place(x=10,y=190)
		self.salary=Entry(self.head)
		self.salary.insert(0,self.data[0][6])
		self.salary.place(x=200,y=190)
		des=Label(self.head,text="Designation :",font="Helvetical 15")
		des.place(x=10,y=220)
		des=Label(self.head,text=self.data[0][7],font="Helvetical 15")
		des.place(x=200,y=220)
		rep=Label(self.head,text="Reported :",font="Helvetical 15")
		rep.place(x=10,y=250)
		reports=Label(self.head,text=self.data[0][8],font="Helvetical 15")
		reports.place(x=200,y=250)
		room=Label(self.head,text="Room-No :",font="Helvetical 15")
		room.place(x=10,y=280)
		self.roomn=Entry(self.head)
		self.roomn.insert(0,self.data[0][9])
		self.roomn.place(x=200,y=280)
		submit=Button(self.head,text="Submit",command=self.action)
		submit.place(x=200,y=320)
		self.head.mainloop()
	def action(self):
		
		self.email=self.Email.get()
		self.phone=self.phone.get()
		self.address=self.address.get()
		self.salary=self.salary.get()
		self.roomn=self.roomn.get()
		self.head.destroy()
		self.con.query("update staff set email='"+self.email+"', phont="+str(self.phone)+", address='"+self.address+"',sal="+str(self.salary)+", room="+str(self.roomn)+" where(staffid='"+self.data[0][0]+"');")
		self.con.commit()
		self.head=tk.Tk()
		self.head.title("Success")
		self.head.geometry("{}x{}".format(150,150))
		x=Label(self.head,text="Data Altered Successfully")
		x.place(x=10,y=20)
		self.head.mainloop()
class remove:
	def __init__(self,con,data):
		self.con=con
		self.con.query("delete from staff where(staffid='"+data+"');")
		self.con.commit()
		self.con.query("delete from password where(staffid='"+data+"');")
		self.con.commit()
		self.head=tk.Tk()
		self.head.title("Success")
		self.head.geometry("{}x{}".format(250,150))
		x=Label(self.head,text="Record Deleted Successfully")
		x.place(x=10,y=20)
		self.head.mainloop()
class add:
	def __init__(self):
		self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hostel")
		self.head=tk.Toplevel()
		self.head.title("Add Staff")
		self.head.geometry("{}x{}".format(600,600))
		staffid=Label(self.head,text="StaffId :",font="Helvetical 15")
		staffid.place(x=10,y=10)
		self.staffid=Entry(self.head)
		self.staffid.place(x=200,y=10)
		name=Label(self.head,text="Name :",font="Helvetical 15")
		name.place(x=10,y=40)
		self.name=Entry(self.head)
		self.name.place(x=200,y=40)
		phone=Label(self.head,text="Phone :",font="Helvetical 15")
		phone.place(x=10,y=70)
		self.phone=Entry(self.head)
		self.phone.place(x=200,y=70)
		address=Label(self.head,text="Address :",font="Helvetical 15")
		address.place(x=10,y=100)
		self.address=Entry(self.head)
		self.address.place(x=200,y=100)
		DOB=Label(self.head,text="DOB :",font="Helvetical 15")
		DOB.place(x=10,y=130)
		self.dob=Entry(self.head)
		self.dob.place(x=200,y=130)
		email=Label(self.head,text="Email :",font="Helvetical 15")
		email.place(x=10,y=160)
		self.email=Entry(self.head)
		self.email.place(x=200,y=160)
		sal=Label(self.head,text="Salary : ",font="Helvetical 15")
		sal.place(x=10,y=190)
		self.sal=Entry(self.head)
		self.sal.place(x=200,y=190)
		des=Label(self.head,text="Designation : ",font="Helvetical 15")
		des.place(x=10,y=220)
		self.des=Entry(self.head)
		self.des.place(x=200,y=220)
		room=Label(self.head,text="Room :",font="Helvetical 15")
		room.place(x=10,y=250)
		self.room=Entry(self.head)
		self.room.place(x=200,y=250)
		pic=Label(self.head,text="Pic Url :",font="Helvetical 15")
		pic.place(x=10,y=280)
		self.pic=Entry(self.head)
		self.pic.place(x=200,y=280)
		pas=Label(self.head,text="Password :",font="Helvetical 15")
		pas.place(x=10,y=310)
		self.pas=Entry(self.head,show='*')
		self.pas.place(x=200,y=310)
		submit=Button(self.head,text="Submit",command=self.action)
		submit.place(x=200,y=350)
		self.head.mainloop()
	def action(self):
		self.name=self.name.get()
		self.staffid=self.staffid.get()
		self.phone=self.phone.get()
		self.address=self.address.get()
		self.dob=self.dob.get()
		self.email=self.email.get()
		self.sal=self.sal.get()
		self.des=self.des.get()
		self.room=self.room.get()
		self.pic=self.pic.get()
		self.pas=self.pas.get()
		self.head.destroy()
		if(self.name and self.staffid and self.phone and self.address and self.dob and self.email and self.sal and self.des and self.room and self.pas and self.pic):
			if('@' in self.email):
				self.con.query("insert into password values('"+self.staffid+"','"+self.pas+"');")
				self.con.commit()
				#self.con.close()
				#self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hostel")
				#self.con.query("set foreign_key_checks=0;")
				#self.con.commit()
				self.con.query("insert into staff values(' "+self.staffid+" ',' "+self.name+" ', "+str(self.phone)+" ,' "+self.address+" ',' "+self.dob+" ',' "+self.email+" ', "+str(self.sal)+ ",' "+self.des+" ',0, "+str(self.room)+" , ' "+self.pic+" ');" )
				self.con.commit()
				#self.con.query("set foreign_key_checks=1;")
				#self.con.commit()
				self.con.close()
			else:
				self.con.close()
				self.head=tk.Tk()
				self.head.title("Error")
				self.head.geometry("{}x{}".format(150,150))
				x=Label(self.head,text="Invalid Email")
				x.place(x=10,y=20)
				self.head.mainloop()
		else:
			self.con.close()
			self.head=tk.Tk()
			self.head.title("Error")
			self.head.geometry("{}x{}".format(150,150))
			x=Label(self.head,text="Data Missing")
			x.place(x=10,y=20)
			self.head.mainloop()