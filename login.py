from tkinter import *
import tkinter
import MySQLdb as sql
from home import *
from low_staff import *
class ui:
	def __init__(self):
		self.con=sql.connect(host='localhost',user='root',passwd='hwp@7299',db='hostel')
		self.root=tkinter.Tk()
		self.root.geometry("{}x{}".format(900,640))
		self.pic=PhotoImage(file="index.png")
		self.back=Label(self.root,image=self.pic)
		self.back.place(x=330,y=120)
		self.root.title("SJBIT Hostel")
		self.createwidget()
		self.root.mainloop()
	def login(self):
		i=None
		self.error=Label(self.root,text="Invalid Credentials",font="Helvetical 20")
		self.staff_id=self.username.get()
		self.password=self.passdata.get()
		
		try:
			self.con.query("select * from password where(staffid='"+self.staff_id+"' and pass='"+self.password+"'); ")
			i=self.con.store_result()
			j=i.fetch_row()
			if(j):
				if ('s' in j[0][0]):
					self.root.destroy()
					y=lower_staff(self.con,j[0][0])
				elif(j[0][0]=='1jb111'):
					self.root.destroy()
					y=home_principal(self.con)
				else:
					self.root.destroy()
					y=home(self.con,j[0][0])
			else:
				self.error=Label(self.root,text="Invalid Credentials",font="Helvetical 20")
				self.error.place(x=350,y=530)
		except:
			self.error=Label(self.root,text="Invalid Credentials",font="Helvetical 20")
			self.error.place(x=350,y=530)
				
	def createwidget(self):
		login=Button(self.root,text="LOGIN" , command=self.login)
		sinup=Button(self.root,text="CANCEL", command=self.root.destroy)
		login.place(x=380,y=490)
		sinup.place(x=480,y=490)
		name=Label(self.root,text="Staff-Id",font="Helvetical 10")
		pas=Label(self.root,text="Password", font="Helvetical 10")
		name.place(x=300,y=380)
		pas.place(x=300,y=420)
		self.username=Entry(self.root,width=25)
		self.passdata=Entry(self.root,width=25,show="*")
		self.username.place(x=395,y=380)
		self.passdata.place(x=395,y=420)
		heading=Label(self.root,text="SJBIT Hostel Management",font="Helvetical 40 ")
		heading.place(x=100,y=10)
if __name__=="__main__":
	 x=ui()



	
	
	

