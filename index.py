from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
import csv
import subprocess
from tkinter import Toplevel, Text, Scrollbar, END
import os


root = Tk()
root.title("ELECTION")

root.iconbitmap("campaign.ico")


def HOME():
    root.deiconify()
    root.state('zoomed')
    try:
        rc.withdraw()
    except:
        rv.withdraw()

def quit():
    result=messagebox.askquestion('system','Are you sure you want to exit?')
    if result=='yes':
          
        root.destroy()
        exit()

def rc1():
    #global img11
    #global sec    
    rc1=Toplevel()
    rc1.title("REGISTRATION")
    rc1.geometry("700x300")
     

    def HOME():
      root.deiconify()
      root.state('zoomed')
      try:
        rc.withdraw()
      except:
        rv.withdraw()

    def rc():
     
     
      rc = Toplevel(rc1)
      rc.title("REGISTRATION FOR CANDIDATE")
      rc.geometry("1000x500")
      rc.iconbitmap("campaign.ico")


      Label(rc,text="CONTESTANTS NOMINATION",font=("Arial bold",30),fg="blue").pack()
      options=['11','12']
      options1=['A','B','C','D']
      options2=['PEARL','EMERALD','SAPPHIRE','RUBY']
      options3=['HEADBOY','HEADGIRL','CLASS REPRESTATIVE','SPORTSLEADER']

      name=StringVar(rc)
      cla=StringVar(rc)
      sec=StringVar(rc)
      post=StringVar(rc)
      house=StringVar(rc)

      r=IntVar()

      Label(rc,text="NAME OF CANDIDATE",font=("Arial italic",18)).place(x=140,y=140)
      e1=Entry(rc,font=('arial',18),textvariable=name,width=20)
      e1.place(x=410,y=140)

      Label(rc,text="ENROLL",font=("Arial italic",18)).place(x=700,y=140)
      e3=Entry(rc,font=('arial',18),width=10)
      e3.place(x=800,y=140)
   

      #Label(rc,text="CLASS",font=("Arial italic",18)).place(x=140,y=200)
      #options=["11","12"]
      #cla = StringVar(rc)
      # Set the default value of the variable
      #cla.set("Select an Option")
      #cl=OptionMenu(rc,cla,*options)
      #cl.place(x=410,y=200)

      Label(rc,text="CLASS",font=("Arial italic",18)).place(x=140,y=200)
      cl=Entry(rc,font=('arial',18),textvariable=cla,width=10)
      cl.place(x=410,y=200)


      Label(rc,text="SECTION",font=("Arial italic",18)).place(x=600,y=200)
      #sect=OptionMenu(rc,sec,*options1)
      #sect.place(x=800,y=200)
      sect=Entry(rc,font=('arial',18),textvariable=sec,width=10)
      sect.place(x=800,y=200)

      Label(rc,text="GENDER",font=("Arial italic",18)).place(x=140,y=250)
      e2=Radiobutton(rc,text='Male',variable=r,value=1)
      e2.place(x=410,y=250)
      e2=Radiobutton(rc,text='Female',variable=r,value=2)
      e2.place(x=480,y=250)

      Label(rc,text="HOUSE",font=("Arial italic",18)).place(x=140,y=300)

      ho=OptionMenu(rc,house,*options2)
      ho.place(x=410,y=300)

 
      Label(rc,text="POST",font=("Arial italic",18)).place(x=600,y=300)
      po=OptionMenu(rc,post,*options3)
      po.place(x=800,y=300)

      def submit():
        nonlocal sec
        
        if sec.get()== ""or e3.get()=="" or e1.get()== "" or r.get()== "" or house.get()== ""or cla.get()== "":
            
                    messagebox.showinfo("WARNING","Please complete the required field!")
        else:

 
            if r.get()==1:
                 g="M"
            else:
                 g="F"
                 
            enroll=str(e3.get())
            name=e1.get()
            cla=cl.get()
            sec=sect.get()
            posting=post.get()
            housing=house.get()
            with open("cl.csv","r",newline='')as h:
             rec=list(csv.reader(h,delimiter=','))
             for i in rec:
               if enroll in i[0]:    
                 messagebox.showinfo("WARNING","ENROLL ALREADY EXIST!")
                 break
             else:
               f=open("cl.csv","a",newline='')
               wobj=csv.writer(f,delimiter=',') 
               while True:  
                   rec=[enroll,name.upper(),cla.upper(),sec.upper(),g,housing.upper(),posting.upper()]
                   wobj.writerow(rec)
                   break
       
               f.close()  
               messagebox.showinfo("info","Succesfully registered")          


      Button(rc,text="SUBMIT",font=("Arial italic",18),command=submit).place(x=450,y=400)

      Button(rc,text="BACK",font=("Arial italic",18)).place(x=140,y=400)

      Button(rc,text="HOME",font=("Arial italic",18),command=HOME).place(x=800,y=400)

    def rv():
      
      rv = Tk()
      rv.title("VOTER REGISTRATION")
      rv.geometry("1000x500")
      rv.iconbitmap("campaign.ico")
      '''def submit1():

        if e3.get() == "" or e1.get() == "" or r.get() == "" or sec.get() == ""or house.get()== ""or cla.get()== "":
       
                      messagebox.showinfo("WARNING","Please complete the required field!")
        else:

 
            if r.get()==1:
                     g="M"
            else:
                     g="F"
            a=str(e3.get())
            b=name.get()
            c=cla.get()
            d=sec.get()
            e=post.get()
            f=house.get()
            with open("cl.csv","r",newline='')as h:
             rec=list(csv.reader(h,delimiter=','))
             for i in rec:
               if a in i[0]:    
                 messagebox.showinfo("WARNING","ENROLL ALREADY EXIST!")
                 break
             else:
               f=open("cl.csv","a",newline='')
               wobj=csv.writer(f,delimiter=',')
               while True:
                       enroll=a
                       name=b
                       cla=c
                       sec=d
                       ge=g
                       ho=f
                       po=e
                       rec=[enroll,name.upper(),cla,sec.upper(),ge.upper(),ho.upper(),po.upper()]
                       wobj.writerow(rec)             
       
               f.close()  
               messagebox.showinfo("info","Succesfully registered")'''
                

      Label(rv,text="REGISTRATION FOR VOTER",font=("Arial bold",30),fg="blue").pack()
      options=['11','12']
      options1=['A','B','C','D']
      options2=['PEARL','EMERALD','SAPPHIRE','RUBY']

      name=StringVar(rv)
      cla=StringVar(rv)
      sec=StringVar(rv)
      
      house=StringVar(rv)

      r=IntVar()

      Label(rv,text="NAME OF CANDIDATE",font=("Arial italic",18)).place(x=140,y=140)
      e1=Entry(rv,font=('arial',18),textvariable=name,width=20)
      e1.place(x=410,y=140)

      Label(rv,text="ENROLL",font=("Arial italic",18)).place(x=700,y=140)
      e3=Entry(rv,font=('arial',18),width=10)
      e3.place(x=800,y=140)

      Label(rv,text="CLASS",font=("Arial italic",18)).place(x=140,y=200)
      cl=Entry(rv,font=('arial',18),textvariable=cla,width=10)
      cl.place(x=410,y=200)


      Label(rv,text="SECTION",font=("Arial italic",18)).place(x=600,y=200)
      #sect=OptionMenu(rc,sec,*options1)
      #sect.place(x=800,y=200)
      sect=Entry(rv,font=('arial',18),textvariable=sec,width=10)
      sect.place(x=800,y=200)

      Label(rv,text="GENDER",font=("Arial italic",18)).place(x=140,y=250)
      e2=Radiobutton(rv,text='Male',variable=r,value=1)
      e2.place(x=410,y=250)
      e2=Radiobutton(rv,text='Female',variable=r,value=2)
      e2.place(x=480,y=250)

      Label(rv,text="HOUSE",font=("Arial italic",18)).place(x=140,y=300)

      ho=OptionMenu(rv,house,*options2)
      ho.place(x=410,y=300)


      def submit1():
        nonlocal sec
        nonlocal cla
        nonlocal house
        if sec.get()== ""or e3.get()=="" or e1.get()== "" or r.get()== "" or house.get()== ""or cla.get()== "":
            
                    messagebox.showinfo("WARNING","Please complete the required field!")
        else:    
         
            if r.get()==1:
                 g="M"
            else:
                 g="F"
                     
            enroll=str(e3.get())
            name=e1.get()
            cla=cl.get()
            sec=sect.get()
            
            housing=house.get()
            with open("vl.csv","r",newline='')as h:
             rec=list(csv.reader(h,delimiter=','))
             for i in rec:
               if enroll in i[0]:    
                 messagebox.showinfo("WARNING","ENROLL ALREADY EXIST!")
                 break
             else:
               f=open("cl.csv","a",newline='')
               wobj=csv.writer(f,delimiter=',') 
               while True:  
                   rec=[enroll,name.upper(),cla.upper(),sec.upper(),g,housing.upper()]
                   wobj.writerow(rec)
                   break
       
               f.close()  
               messagebox.showinfo("info","Succesfully registered")          




      Button(rv,text="SUBMIT",font=("Arial italic",18),command=submit1).place(x=450,y=400)

      Button(rv,text="BACK",font=("Arial italic",18)).place(x=140,y=400)
   
      Button(rv,text="HOME",font=("Arial italic",18),command=HOME).place(x=800,y=400)

    r1=Button(rc1,text="CONTESTANTS NOMINATION",font=("Arial italic",18),fg="green",command=rc)
    r1.place( x=170, y=90)
    r2=Button(rc1,text="VOTER REGISTRATION ",font=("Arial italic",18),fg="green",command=rv)
    r2.place( x=200, y=160)

def tl():
      
      te=Toplevel()

      te.title("TEACHER LOGIN")
      te.geometry("700x300")
      Label(te,text="TEACHER LOGIN",font=("Arial bold",30),fg="blue").pack()
      name=StringVar(te)
      
      r=IntVar()

      Label(te,text="NAME OF TEACHER",font=("Arial italic",18)).place(x=100,y=100)
      e1=Entry(te,font=('arial',18),textvariable=name,width=20)
      e1.place(x=350,y=100)

      Label(te,text="TCODE",font=("Arial italic",18)).place(x=100,y=150)
      e3=Entry(te,font=('arial',18),width=10)
      e3.place(x=350,y=150)

   
      def submit2():
        nonlocal e1
        nonlocal e3
        if e3.get() == "" or e1.get() == "":
       
                      messagebox.showinfo("WARNING","Please complete the required field!")
        else:
                
          f=open("cl.csv","r",newline='')
          rec=list(csv.reader(f,delimiter=','))
          for r in range(len(rec)):
             if rec[r][0]==str(e3.get()):
                   messagebox.showinfo("WARNING","this code doesnot exist!")
    
             else:
#new update and delete window 
#           def te2():
                te2=Toplevel(te)
                te2.title("UPDATE AND DELETE")
                te2.geometry("1000x500")

                def delete():
                      f=open("cl.csv","r",newline='')
                      rec=list(csv.reader(f,delimiter=','))
                      a=str(e5.get())
                      for r in range(len(rec)):
                        if rec[r][0]==a:
                           print(rec.pop(r))
                           break
                      f.close()
                      f=open("cl.csv","w",newline='')
                      wobj=csv.writer(f,delimiter=',')
                      for r in rec:
                           wobj.writerow(r) 
                      messagebox.showinfo("info","record successfully deleted")
                def update():
                     if e3.get() == "" or e1.get() == "" or r.get() == "" or sec.get() == ""or house.get()== ""or cla.get()== "":
       
                                    messagebox.showinfo("WARNING","Please complete the required field!")
                     else:
                         if r.get()==1:
                                 g="M"
                         else:
                                 g="F"
                     f=open("cl.csv","r+",newline='')
                     rec=list(csv.reader(f,delimiter=','))
                     a=str(e5.get())
                     b=name.get()
                     c=cla.get()
                     d=sec.get()
                     ge=g
                     e=house.get()
                     f=post.get()
    
                     for r in range(len(rec)):
                         if rec[r][0]==a:
                            rec[r][1]=b
                            rec[r][2]=c
                            rec[r][3]=d
                            rec[r][4]=ge
                            rec[r][5]=e
                            rec[r][6]=f
                            break
                     f.close()
    
                     f=open("cl.csv","w",newline='')
                     wobj=csv.writer(f,delimiter=',')
                     for r in rec:
                         wobj.writerow(r)
                            
                     messagebox.showinfo("info","record successfully updated")       
                                

                Label(te2,text="UPDATION AND DELETION",font=("Arial bold",30),fg="blue").pack()
                options=['11','12']
                options1=['A','B','C','D']
                options2=['PEARL','EMERALD','SAPPHIRE','RUBY']
                options3=['HEADBOY','HEADGIRL','CLASS REPRESTATIVE','SPORTSLEADER']

                name=StringVar(te2)
                cla=StringVar(te2)
                sec=StringVar(te2)
                house=StringVar(te2)
                post=StringVar(te2)

                r=IntVar()

                Label(te2,text="NAME OF CANDIDATE",font=("Arial italic",18)).place(x=140,y=140)
                e1=Entry(te2,font=('arial',18),textvariable=name,width=20)
                e1.place(x=410,y=140)

                Label(te2,text="ENROLL",font=("Arial italic",18)).place(x=700,y=140)
                e3=Entry(te2,font=('arial',18),width=10)
                e3.place(x=800,y=140)

                Label(te2,text="CLASS",font=("Arial italic",18)).place(x=140,y=200)
                cl=Entry(te2,font=('arial',18),textvariable=cla,width=10)
                cl.place(x=410,y=200)


                Label(te2,text="SECTION",font=("Arial italic",18)).place(x=600,y=200)
                #sect=OptionMenu(rc,sec,*options1)
                #sect.place(x=800,y=200)
                sect=Entry(te2,font=('arial',18),textvariable=sec,width=10)
                sect.place(x=800,y=200)

                Label(te2,text="GENDER",font=("Arial italic",18)).place(x=140,y=250)
                e2=Radiobutton(te2,text='Male',variable=r,value=1)
                e2.place(x=410,y=250)
                e2=Radiobutton(te2,text='Female',variable=r,value=2)
                e2.place(x=480,y=250)

                Label(te2,text="HOUSE",font=("Arial italic",18)).place(x=140,y=300)
                ho=OptionMenu(te2,house,*options2)
                ho.place(x=410,y=300)

                Label(te2,text="POST",font=("Arial italic",18)).place(x=600,y=300)
                po=OptionMenu(te2,post,*options3)
                po.place(x=800,y=300)

                    
                Button(te2,text="UPDATE",font=("Arial italic",18),command=update).place(x=300,y=400)
                Button(te2,text="DELETE",font=("Arial italic",18),command=delete).place(x=600,y=400)
                 

      Button(te,text="SUBMIT",font=("Arial italic",18),command=submit2).place(x=300,y=200)

      Button(te,text="BACK",font=("Arial italic",18)).place(x=100,y=200)
   
      Button(te,text="HOME",font=("Arial italic",18),command=HOME).place(x=520,y=200)


def poll():
    root=Tk()
    root.geometry('600x500')
    l=Label(root,text='enter enrollno',font=('Italic',20))
    l.pack(pady=10)
    txt=Entry(root,width=10)
    txt.pack(pady=10)
    lis=[]#create a list to upload contestants details into results file
    def givehouse(lm):#returns house of voter 
        t=''
        with open('vl.csv','r')as c:
            lit=list(csv.reader(c))
            for a in lit:
                if a[1]==lm:
                    t=a[5]
        return t
    def configcapts(t):#gives names of captain of the voters house
        l=['nota']
        with open('cl.csv','r')as v:
            li=list(csv.reader(v))
            for a in li:
                if a[5]==t and a[6]=='captain':
                    l.append(a[1])
        return l
    def configure(l):#gives names of headboy/girl
        l=[]
        with open('cl.csv','r')as v:
            li=list(csv.reader(v))
            for a in li:
                if a[5]=='EMERALD':
                    l.append(a[1])
        return l
    def cast(L,h):#appends the details of leaders and no.of votes in lis(global one)
        if L!='nota':
            for ap in range(len(lis)):#if already exists in lis
                if lis[ap][1]==L:
                    if lis[ap][1]==h:
                        lis[ap][7]+=1
                        break
            else:
                with open('cl.csv','r')as v:#adds the contestans to lis
                  li=list(csv.reader(v))
                  for a in li:
                      if a[1]==L:
                          c=li.count(a)
                          a.append(c)
                          lis.append(a)
    def final(k):#uses teachers code to submit response to result file
        with open('tl.csv','r')as t:
            l=list(csv.reader(t))
            for a in l:
                if a[0]==k:
                    messagebox.showinfo('Submission','Response Submitted')
                    with open('results.csv','w')as w:
                        k=csv.writer(w)
                        k.writerows(lis)                
                    root.quit()
                    break
                else:
                    messagebox.showinfo('WARNING','ERROR CODE')
    def start(l):
        p=l
        top=Toplevel()
        l1=Label(top,text='1.select captain',font=('Italic',20)) 
        l1.grid(column=1,row=2,pady=15,padx=10)
        combo=ttk.Combobox(top,width=30)
        combo['values']=configcapts('EMERALD')
        combo.grid(column=2,row=2,pady=15,padx=10)
        combo.bind('<<ComboboxSelected>>')
        def CASTCAPT():
            t=combo.get()
            print(t)
            cast(t,'captain')
        l2=Label(top,text='2.select headboy',font=('Italic',20))
        l2.grid(column=1,row=3,pady=15,padx=10)
        combo2=ttk.Combobox(top,width=30)
        combo2['values']=configure('headboy')
        combo2.grid(column=2,row=3,pady=15,padx=10)
        combo2.bind('<<ComboboxSelected>>')
        combo2=ttk.Combobox(top,width=30)
        def CASTHB():
            t=combo2.get()
            cast(t,'headboy')
        l3=Label(top,text='3.select headgirl',font=('Italic',20))
        l3.grid(column=1,row=4,pady=15,padx=10)
        combo3=ttk.Combobox(root,width=30)
        combo3['values']=configure('headgirl')
        def CASTHG():
            t=combo3.get()
            cast(t,'headgirl')
        btnc=Button(top,text='elect',command=CASTCAPT)
        btnc.grid(column=3,row=2,pady=15,padx=10)
        btnb=Button(top,text='elect',command=CASTHB)
        btnb.grid(column=3,row=3,pady=15,padx=10)
        btng=Button(top,text='elect',command=CASTHG)
        btng.grid(column=3,row=4,pady=15,padx=10)
        butd=Button(top,text='Done',command=top.destroy)
        butd.grid(column=3,row=5,pady=15,padx=10)
    def clicked():
        t=txt.get()
        p=int(t)
        l=str(p)
        with open('vl.csv','r')as v:
            lit=csv.reader(v)
            for a in lit:
                if a[0]==l:
                    global i#to use enroll in text in toplevel window
                    i=l
                    print(i)
                    start(i)
                    break
            else:
                messagebox.showinfo('WARNING','WRONG CREDENTIALS')
    but=Button(root,text='next',command=clicked)
    but.pack(pady=10)
    t2=Entry(root,width=10)
    t2.pack()
    def FINISH():
        y=t2.get()
        final(y)
        #butgl=Button(root,text='finish',command=FINISH)
        #butgl.pack()
    butgl=Button(root,text='finish',command=FINISH)
    butgl.pack()

def ri():
    ri = Toplevel()
    ri.title("REPORT ISSUES")
    ri.geometry("700x300")
    ri.iconbitmap("C:\\Users\\jpadv\\OneDrive\\Desktop\\election\\campaign.ico")
    Label(ri,text="REPORT ISSUES",font=("Arial italic",18)).pack()
    e5=Entry(ri,font=('arial',18),width=40).place(x=100,y=100)

    
    def submit3():
        if e5.get() =="":
            messagebox.showinfo("WARNING","Please complete the required field!")
        else:
            messagebox.showinfo("info","issues submitted!")


            
    Button(ri,text="SUBMIT",font=("Arial italic",18),command=submit3).place(x=300,y=180)

    Button(ri,text="BACK",font=("Arial italic",18)).place(x=100,y=180)

    Button(ri,text="HOME",font=("Arial italic",18),command=HOME).place(x=500,y=180)

def show_results():
    subprocess.run(["python", "results.py"])

def show_about_us():
    # Create a new window (Dialog Box)
    about_window = Toplevel()
    about_window.title("About Us")
    about_window.geometry("600x500")
    about_window.configure(bg="lightyellow")  # Background color

    # Title Label
    from tkinter import Label
    Label(about_window, text="About Our School", font=("Arial", 18, "bold"), fg="blue", bg="lightyellow").pack(pady=10)

    # Text Widget with Scrollbar
    text_area = Text(about_window, wrap="word", font=("Arial", 12), padx=10, pady=10, bg="white", fg="black")
    text_area.pack(expand=True, fill="both", padx=10, pady=10)

    scrollbar = Scrollbar(text_area, command=text_area.yview)
    text_area.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Read content from aboutus.txt and insert into text_area
    if os.path.exists("aboutus.txt"):
        with open("aboutus.txt", "r", encoding="utf-8") as file:
            text_area.insert(END, file.read())
    else:
        text_area.insert(END, "Error: 'aboutus.txt' file not found.")

    text_area.config(state="disabled")  # Make text read-only
    
    
bg=ImageTk.PhotoImage(Image.open("vote1.jpg"))
img= Label(root,image=bg)
img.place(x=10,y=0) 

 
root.geometry('1100x1000')
root.state('zoomed')

name = ""
cla = ""
sec = ""
post = ""
house = ""

img2=PhotoImage(file ="title2.png")
title=Label(root,image=img2)
title.place(x=400,y=0)

img3=PhotoImage(file ="title3.png")
title=Label(root,image=img3)
title.place(x=350,y=500)

img4=PhotoImage(file ="logo.png")
logo=Label(root,image=img4)
logo.place(x=10,y=0)

img5=PhotoImage(file ="stamped1.png")
reg=Button(root,image=img5,command=rc1)
reg.place(x=110,y=200)

img6=PhotoImage(file ="vote1.png")
vote=Button(root,image=img6,command=poll)    
vote.place(x=330,y=200)

img7=PhotoImage(file ="research1.png")
res=Button(root,image=img7,command=show_results)
res.place(x=550,y=200)

img8=PhotoImage(file ="cs.png")
rep=Button(root,image=img8,command=ri)
rep.place(x=770,y=200)

img9=PhotoImage(file ="info.png")
rep=Button(root,image=img9,command=show_about_us)
rep.place(x=990,y=200)

img10=PhotoImage(file ="logout.png")
quit_button=Button(root,image=img10,command=quit)
quit_button.place(x=980,y=500)

img12=PhotoImage(file ="user1.png")
tl=Button(root,image=img12,command=tl)
tl.place(x=1200,y=0)

root.mainloop()
 
