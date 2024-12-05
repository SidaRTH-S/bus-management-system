

 
 

from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
db1=mysql.connector.connect(host="localhost",user="root",passwd="g00d_Uare",db="busmanagementsystem")
root=Tk()

c=db1.cursor(buffered=True)
i,j,k,z,p,o="",'','','','',''


def enter(m):
    global buto,z
    if m==1:
        z=0
        mw=Toplevel()
        mw.resizable(False,False)
        mw.configure(bg="purple")
        mw.title("main window")
        global img2
        mw.geometry("1000x750+0+0")
        img2=PhotoImage(file="myimg2.png")
        Label(mw,image=img2).place(x=0,y=0,width=1000,height=750)
        fr=Frame(mw)
        fr .place(relx=0.25,rely=0.2,width=500,height=400)
        la=Label(fr,text="Log In As...",width="30",fg="blue")
        fonts1=("Britannic Bold",25,"bold")
        la.configure(font=fonts1)
        la.place(relx=0,rely=0.1)
        buto=Button(fr,text="click after choosing ",cursor="hand2",width="20",state=DISABLED,command=rtm)
        x1=Radiobutton(fr,text="As an admin ",variable=m,cursor="hand2",value=1,width="20",command=switch1,bg="#d3d3d3")
        x2=Radiobutton(fr,text="As an existing user ",variable=m,cursor="hand2",value=2,width="20",command=switch,bg="#d3d3d3")
        x3=Radiobutton(fr,text="As a bus conductor ",variable=m,cursor="hand2",value=2,width="20",command=sumup,bg="#d3d3d3")
        buto.place(relx=0.4,rely=0.9)
        fonts1=("Broadway",20,"bold")
        x1.configure(font=fonts1)
        x2.configure(font=fonts1)
        x3.configure(font=fonts1)
        x1.place(relx=0.1,rely=0.3)
        x2.place(relx=0.1,rely=0.5)
        x3.place(relx=0.1,rely=0.7)
    elif m==2:
        m=1
        global img1
        img1=PhotoImage(file="main back.png")
        nw=Toplevel()
        nw.geometry("1000x750+0+0")
        nw.configure(bg="purple")
        nw.resizable(False,False)
        nw.title("signup")
        global i,j,k,i1,i2,i3
        fr=Frame(nw)

        fon=("Copperplate Gothic Bold",10,"bold")
        Label(nw,image=img1).place(x=0,y=0,relwidth=1,relheight=1)
        fr=Frame(nw,bd=10)
        fr .place(relx=0.25,rely=0.2,width=500,height=400)
        la=Label(fr,text="welcome new user",width="20",fg="blue")
        la.configure(font=fonts)
        la.place(relx=0.005,rely=0.1)
        i1=StringVar()
        i1.set(" unique username Limit is 30")
        i=Entry(fr,textvariable=i1,cursor="hand2",width="40")
        Label(fr,text="name",width="10",font=fon,fg="orange").place(relx=0.1,rely=0.3)
        Label(fr,text="password",width="10",font=fon,fg="orange").place(relx=0.1,rely=0.4)
        Label(fr,text="email id",width="10",font=fon,fg="orange").place(relx=0.1,rely=0.5)
        i.place(relx=0.4,rely=0.3)
        i2=StringVar()
        i2.set("strong password limit is 10")
        j=Entry(fr,text="limit=10",textvariable=i2,cursor="hand2",width="40")
        j.place(relx=0.4,rely=0.4)
        i3=StringVar()
        i3.set("email id limit=20")
        k=Entry(fr,text="limit=20",textvariable=i3,cursor="hand2",width="40")
        k.place(relx=0.4,rely=0.5)
        fonts1=("Broadway",10,"bold")
        buto=Button(nw,text="click after choosing ",cursor="hand2",width="20",fg="blue",height="3",command=rtx,bd=5)
        buto.configure(font=fonts1)
        buto.place(x=375,y=510)
    else:
        None
z=0
def sumup():
    global z,m
    m=99
    z=9
    if buto["state"]!=NORMAL:
        buto["state"]=NORMAL
    return

def rtx():
    global i1,i2,i3,i,j,k,c,db1
    i1=i.get()
    i2=j.get()
    i3=k.get()
    print(len(i1),len(i2),len(i3))
    if len(i1)==0 or len(i2)==0 or len(i3)==0 or len(i1)>=30 or len(i2)>=10 or len(i3)>=20:
        messagebox.showinfo('error','all fields are required and should be under limit pass<=10,userid<=30,email<=20')
    elif len(i1)!=0 and len(i2)!=0 and len(i3)!=0 or len(i1)<30 and len(i2)<10 and len(i3)<20 :
        sml="select userid from user where userid = %s"
        c.execute(sml,[i1])
        l=c.rowcount
        if l>0:
            messagebox.showinfo('failure',' user id is already registered')
        else:
            sql="insert into user values(%s,%s,%s)"
            c.execute(sql,(i1,i2,i3))
            db1.commit()
            messagebox.showinfo('success',' fields are entered in system')
    return




def  rtm():
     fon=("Showcard Gothic",10,"bold")
     fo1=("Britannic Bold",20,"bold")
     global p,o,y,x,m
     if m==1:
        global img4,z
        fon=("Britannic Bold",25,"bold")
        nw1=Toplevel()
        nw1.configure(bg="purple")
        nw1.title("Backend protector")
        nw1.geometry("1000x750+0+0")
        nw1.resizable(False,False)
        img4=PhotoImage(file="myimg2.png")
        Label(nw1,image=img4).place(x=0,y=0,relwidth=1,relheight=1)
        fr=Frame(nw1)
        fr .place(relx=0.25,rely=0.2,width=500,height=400)
        Label(fr,text="Security Check...",font=fon).place(x=100,y=100)
        Label(fr,text="Enter the Admin password:",height="3",width="25",font=fo1,fg="orange").place(x=80,y=150)
        fz=StringVar()
        fz.set('')
        z=Entry(fr,textvar=fz,cursor="hand2",width="30")
        z.place(x=100,y=250)
        b1=Button(fr,text="click after choosing ",cursor="hand2",width="20",fg="blue",height="3",command=adm,bd=5)
        b1.place(x=100,y=300)
     elif m==2:
        m=1
        global img912
        img912=PhotoImage(file="myimg1.png")
        nw=Toplevel()
        nw.title("login")
        nw.resizable(False,False)
        nw.geometry("1000x750+0+0")
        nw.configure(bg="purple")
        global i4,i5,i41,i51
        fr=Frame(nw)
        fon=("Copperplate Gothic Bold",10,"bold")
        Label(nw,image=img912).place(x=0,y=0,relwidth=1,relheight=1)
        fr=Frame(nw,bd=10)
        fr .place(relx=0.25,rely=0.2,width=500,height=400)
        la=Label(fr,text="Welcome User",width="20",fg="blue")
        la.configure(font=fonts)
        la.place(relx=0.005,rely=0.1)
        i41=StringVar()
        i41.set("  Limit is 30")
        i4=Entry(fr,textvariable=i41,cursor="hand2",width="40")
        Label(fr,text="name",width="10",font=fon,fg="orange").place(relx=0.1,rely=0.3)
        Label(fr,text="password",width="10",font=fon,fg="orange").place(relx=0.1,rely=0.4)
        #Label(fr,text="email id",width="10",font=fon,fg="orange").place(relx=0.1,rely=0.5)
        i4.place(relx=0.4,rely=0.3)
        i51=StringVar()
        i51.set("password limit is 10")
        i5=Entry(fr,text="limit=10",textvariable=i51,cursor="hand2",width="40")
        i5.place(relx=0.4,rely=0.4)
        #i3=StringVar()
        #i3.set("email id limit=10")
        #k=Entry(fr,text="limit=20",textvariable=i3,cursor="hand2",width="40")
        #k.place(relx=0.4,rely=0.5)
        fonts1=("Broadway",10,"bold")
        b1=Button(nw,text="click after choosing ",cursor="hand2",width="20",fg="blue",height="3",command=m1,bd=5)
        b1.configure(font=fonts1)
        b1.place(x=375,y=490)
     elif m==99 and z==9:
        m=1
        global img210,c,cz2
        img210=PhotoImage(file="Screenshot (95).png")
        nw=Toplevel()
        nw.title("conductor")
        nw.resizable(False,False)
        nw.geometry("1000x750+0+0")
        nw.configure(bg="purple")
        global i6,i7,i61,i71
        fr=Frame(nw)
        fon=("Copperplate Gothic Bold",10,"bold")
        Label(nw,image=img210).place(x=0,y=0,relwidth=1,relheight=1)
        fr=Frame(nw,bd=10)
        fr .place(relx=0.25,rely=0.2,width=500,height=400)
        la=Label(fr,text="Welcome conductor",width="20",fg="blue")
        la.configure(font=fonts)
        la.place(relx=0.005,rely=0.1)
        i61=StringVar()
        i61.set("  Limit is 30")
        i6=Entry(fr,textvariable=i61,cursor="hand2",width="40")
        Label(fr,text=" your id",width="15",font=fon,fg="orange").place(relx=0.1,rely=0.3)
        Label(fr,text="password",width="15",font=fon,fg="orange").place(relx=0.1,rely=0.4)
        i6.place(relx=0.5,rely=0.3)
        i71=StringVar()
        i71.set("password limit is 10")
        i7=Entry(fr,text="limit=10",textvariable=i71,cursor="hand2",width="40")
        i7.place(relx=0.5,rely=0.4)
        fonts1=("Broadway",10,"bold")
        Label(fr,text="bus issue no",width="15",font=fon,fg="orange").place(relx=0.1,rely=0.5)
        c.execute('select issueno from busses')
        option=c.fetchall()
        cz2=ttk.Combobox(fr,value=option)
        cz2.set(option[0])
        cz2.place(relx=0.5,rely=0.5)
        b1=Button(nw,text="click after choosing ",cursor="hand2",width="20",fg="blue",height="3",command=mx,bd=5)
        b1.configure(font=fonts1)
        b1.place(x=375,y=490)

def mx():
    global i6,i7,i61,i71,cz2,cmon
    i61=i6.get()
    i71=i7.get()
    cmon=cz2.get()
    if len(str(i61))!=0 and len(str(i61))!=0 and len(str(i71))<20 and len(str(i71))<10 :
        sml="select conductorid from busses where conductorid = %s"
        c.execute(sml,[i61])
        l=c.rowcount
        if l<=0:
            messagebox.showinfo('failure',' user id is not registered')
        else:
            sql="select conductorid from busses where conductorid = %s and conpass = %s and issueno = %s"
            c.execute(sql,(i61,i71,cmon))
            c.rowcount
            if c.rowcount==0:
                messagebox.showinfo('failure',' matching data not found incorrect password entered or bus choosen')
                m=1
            else:
                messagebox.showinfo('success',' fields are found in the system opening required page')
                xor()
    elif len(str(i61))==0 or len(str(i71))==0 or len(str(i61))>=20 or len(str(i71))>=10 or len(str(cmon))>=15 or len(str(cmon))==0 :
        messagebox.showinfo('error','all fields are required and limit of your id=20 and for password is 10 issue no must be less than 15')
    return




def xor():
    m=1
    global img72,i61,i71,cmon
    img72=PhotoImage(file="Screenshot (95).png")
    nw=Toplevel()
    nw.title("other window")
    nw.resizable(False,False)
    nw.geometry("1000x750+0+0")
    nw.configure(bg="purple")
    fr=Frame(nw)
    fon=("Britannic Bold",20,"bold")
    Label(nw,image=img72).place(x=0,y=0,relwidth=1,relheight=1)
    fr=Frame(nw,bd=10)
    fr .place(relx=0.2,rely=0.2,width=500,height=400)
    la=Label(fr,text= "Welcome: "+str(i61),width="25",fg="blue",font=fon).place(relx=0.1,rely=0.1)
    la=Label(fr,text= ' conductor of '+str(cmon),width="25",fg="blue",font=fon).place(relx=0.1,rely=0.2)
    fon=("Britannic Bold",45,"bold")
    on=("Britannic Bold",25,"bold")
    Button(fr,text='see bookings ',command=mor,font=on).place(relx=0.3,rely=0.4)
    Button(fr,text='decrease seats',command=dset,font=on).place(relx=0.3,rely=0.7)

def dset():
    global img72,i61,i71,cmon,c,czqw
    img72=PhotoImage(file="Screenshot (95).png")
    nw=Toplevel()
    nw.title("seats decrease window")
    nw.resizable(False,False)
    nw.geometry("1000x750+0+90")
    nw.configure(bg="purple")
    fr=Frame(nw)
    
    fon=("Britannic Bold",20,"bold")
    Label(nw,image=img72).place(x=0,y=0,relwidth=1,relheight=1)
    fr=Frame(nw,bd=10)

    fr .place(relx=0.2,rely=0.2,width=500,height=400)
    la=Label(fr,text= ' select seats to be decreased',width="25",fg="blue",font=fon).place(relx=0.1,rely=0.2)
    opt=[]
    c.execute("select seatsleft from busses where issueno = %s",[cmon])
    zq=c.fetchall()
    i=0
    while i < int(zq[0][0]):
        opt.append(i)
        i+=1
    czqw=ttk.Combobox(fr,value=opt)
    czqw.set(opt[0])
    czqw.bind('<<Comboboxselected>>',lother)
    czqw.place(relx=0.2,rely=0.3)
    Button(fr,text="click after slecting ",width="30",fg="orange",command=lother).place(relx=0.1,rely=0.6)
    


def lother():
    global c,czqw,cmon
    n=czqw.get()
    c.execute('select seatsleft from busses where issueno = %s',[cmon])
    b=c.fetchall()
    c.execute('update busses set seatsleft = %s -%s where issueno = %s ',[b[0][0],n,cmon])
    messagebox.showinfo('success','seats decreased for online booking')

    
def mor():
    m=1
    global img71,i61,i71,cmon,c,db1
    img71=PhotoImage(file="Screenshot (96).png")
    nw=Toplevel()
    nw.title("about bookings")
    nw.resizable(False,False)
    nw.geometry("1000x550+0+90")
    nw.configure(bg="purple")
    fr=Frame(nw)
    fon=("Britannic Bold",20,"bold")
    Label(nw,image=img71).place(x=0,y=0,relwidth=1,relheight=1)
    fr=Frame(nw,bd=10)
    fr .place(relx=0.005,rely=0.1,width=1000,height=400)
    #la=Label(fr,text="Welcome: "+str(i61),width="20",fg="blue",font=fon).place(relx=0.05,rely=0.1)
    fon=("Britannic Bold",25,"bold")
    Label(fr,text=str(cmon)+' \' s' +' Bookings are ...',font=fon,fg='blue').place(relx=0.1,rely=0.2)
    tab=ttk.Treeview(fr)
    tab['columns']=('r','n','p','e','f','g','h','q','w','z','y','a')
    tab.column("#0",anchor=E,width=1)
    tab.column("r",anchor=E,width=10)
    tab.column("n",anchor=E,width=90)
    tab.column("p",anchor=CENTER,width=70)
    tab.column("e",anchor=E,width=70)
    tab.column("f",anchor=E,width=70)
    tab.column("g",anchor=E,width=70)
    tab.column("h",anchor=E,width=70)
    tab.column("q",anchor=E,width=70)
    tab.column("w",anchor=E,width=70)
    tab.column("z",anchor=E,width=70)
    tab.column("y",anchor=E,width=70)
    tab.column("a",anchor=E,width=70)
    tab.heading("r",text="sr no",anchor=CENTER)
    tab.heading("n",text="user id",anchor=CENTER)
    tab.heading("p",text="issue no [bus]",anchor=CENTER)
    tab.heading("e",text="pickup location",anchor=CENTER)
    tab.heading("f",text="drop location",anchor=CENTER)
    tab.heading("g",text="pickup time",anchor=CENTER)
    tab.heading("h",text="drop time",anchor=CENTER)
    tab.heading("q",text="fare",anchor=CENTER)
    tab.heading("w",text="type Of bus",anchor=CENTER)
    tab.heading("z",text="date",anchor=CENTER)
    tab.heading("y",text="drivers name",anchor=CENTER)
    tab.heading("a",text="seats boooked",anchor=CENTER)
    tab.place(relx=0.02,rely=0.3,width=950)
    c.execute("select * from bookings where issueno = %s",[cmon])
    c.rowcount
    l=c.fetchall()
    global j
    j=0
    if c.rowcount==0:
        Label(fr,text='[ Note :'+' sorry '+str(cmon)+' have no booked seats :-0 ' +']',font="fon1",fg='red').place(relx=0.1,rely=0.2)
    else:
        for i in l:
            print(i)
            j+=1
            tab.insert(parent='',index='end',iid=j,text="srno",values=(j,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]))






def m1():
    global i4,i5,i41,i51
    i41=i4.get()
    i51=i5.get()
    if len(str(i41))!=0 and len(str(i51))!=0 and len(str(i41))<30 and len(str(i51))<10 :
        sml="select userid from user where userid = %s"
        c.execute(sml,[i41])
        l=c.rowcount
        if l<=0:
            messagebox.showinfo('failure',' user id is not registered')
        else:
            sql="select userid from user where userid = %s and password= %s"
            c.execute(sql,(i41,i51))
            c.rowcount
            if c.rowcount==0:
                messagebox.showinfo('failure',' user not found incorrect username or password entered')
                m=1
                enter()
            else:
                messagebox.showinfo('success',' fields are found in the system opening required page')
                m2()
    elif len(str(i41))==0 or len(str(i51))==0 or len(str(i41))>=30 or len(str(i51))>=10:
        messagebox.showinfo('error','all fields are required and limit of user id=30 and for password is 10')
    return

def m2():
        m=1
        global img7,i41
        img7=PhotoImage(file="Screenshot (96).png")
        nw=Toplevel()
        nw.title("user window")
        nw.resizable(False,False)
        nw.geometry("1000x550+0+90")
        nw.configure(bg="purple")
        global i4,i5,i41,i51
        fr=Frame(nw)
        fon=("Britannic Bold",20,"bold")
        Label(nw,image=img7).place(x=0,y=0,relwidth=1,relheight=1)
        fr=Frame(nw,bd=10)
        fr .place(relx=0.005,rely=0.1,width=500,height=400)
        la=Label(fr,text="Welcome:"+str(i41),width="20",fg="blue")
        la.configure(font=fonts)
        la.place(relx=0.005,rely=0.1)
        Button(fr,text="To check you current bookings",width="30",font=fon,fg="orange",command=m3).place(relx=0.1,rely=0.3)
        Button(fr,text="To create book new journey",width="30",font=fon,fg="orange",command=m10).place(relx=0.1,rely=0.6)
        Button(fr,text="To delete an existing journey ",width="30",font=fon,fg="orange",command=mnm).place(relx=0.1,rely=0.9)

def mnm():
    global ima,c,c13,i41
    fon=("Britannic Bold",25,"bold")
    rw1=Tk()
    rw1.title("bookings")
    rw1.configure(bg="purple")
    rw1.resizable(False,False)
    rw1.geometry("1000x750")
    ima=PhotoImage(file="myimg1.png")
    #Label(rw1,image=ima).place(x=0,y=0,width=1000,height=750)
    fr=Frame(rw1)
    fr .place(relx=0.001,rely=0.2,width=1000,height=400)
    Label(fr,text='Bookings for '+ str(i41)+' are ...',font=fon,fg='blue').place(relx=0.1,rely=0.1)
    tab=ttk.Treeview(fr)
    tab['columns']=('r','n','p','e','f','g','h','q','w','z','y','a')
    tab.column("#0",anchor=E,width=1)
    tab.column("r",anchor=E,width=10)
    tab.column("n",anchor=E,width=90)
    tab.column("p",anchor=CENTER,width=70)
    tab.column("e",anchor=E,width=70)
    tab.column("f",anchor=E,width=70)
    tab.column("g",anchor=E,width=70)
    tab.column("h",anchor=E,width=70)
    tab.column("q",anchor=E,width=70)
    tab.column("w",anchor=E,width=70)
    tab.column("z",anchor=E,width=70)
    tab.column("y",anchor=E,width=70)
    tab.column("a",anchor=E,width=70)
    tab.heading("r",text="sr no",anchor=CENTER)
    tab.heading("n",text="user id",anchor=CENTER)
    tab.heading("p",text="issue no [bus]",anchor=CENTER)
    tab.heading("e",text="pickup location",anchor=CENTER)
    tab.heading("f",text="drop location",anchor=CENTER)
    tab.heading("g",text="pickup time",anchor=CENTER)
    tab.heading("h",text="drop time",anchor=CENTER)
    tab.heading("q",text="fare",anchor=CENTER)
    tab.heading("w",text="type Of bus",anchor=CENTER)
    tab.heading("z",text="date",anchor=CENTER)
    tab.heading("y",text="drivers name",anchor=CENTER)
    tab.heading("a",text="seats boooked",anchor=CENTER)
    tab.place(relx=0.02,rely=0.3,width=950)
    c.execute("select * from bookings where userid = %s ",[i41])
    l=c.fetchall()
    global j
    j=0
    for i in l:
        j+=1
        tab.insert(parent='',index='end',iid=j,text="srno",values=(j,i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10])) 
    srl="select issueno from bookings where userid = %s"
    c.execute(srl,[i41])
    st=c.rowcount
    if st==0:
            Label(fr,text="[Note : sorry no bookings available for you ]",font="fon1",fg='red').place(relx=0.1,rely=0.2)
    else:
        Label(fr,text="[Note : the data will be deleted ones you close this window ]",font="fon1",fg='red').place(relx=0.1,rely=0.2)
        Label(fr,text="select issue no",font="fon1",fg='black').place(relx=0.3,rely=0.7)
        OPTo=c.fetchall()  
        c13=ttk.Combobox(fr,value=OPTo)
        c13.current(0)
        c13.bind("<<ComboboxSelected>>")
        c13.place(relx=0.4,rely=0.8)
        Button(fr,text="delete  selected booking",bd=5,height="3",width="20",command= crmt).place(relx=0.6,rely=0.9)



def crmt():
    global c,db1,c12,i41,db1
    cm=c13.get()
    c.execute('select seatsleft from busses where issueno = %s',[cm])
    mb=c.fetchone()
    c.execute('select seats_booked from bookings where userid = %s and issueno = %s ',(i41,cm))
    smtp=c.fetchone()
    if smtp[0]==0:
        c.execute('DELETE FROM BOOKINGS WHERE ISSUENO =%s AND USERID = %s and seats_booked = 1 ',(cm,i41))
    else:
        c.execute('update bookings set seats_booked = %s -1 where issueno = %s and userid = %s and seats_booked = %s',(smtp[0],cm,i41,smtp[0]))
        r=c.rowcount
    c.execute('update busses set seats_left = %s +%s where issueno = %s ',(mb[0],r,cm))
    db1.commit()
    messagebox.showinfo('success','booking is deleted')




def m10():
        m=1
        global img8,i41,ca,cb,cc,cd,ce,cf,cg,ch,ci1
        img8=PhotoImage(file="Screenshot (97).png")
        nw=Toplevel()
        nw.title("busses window")
        nw.resizable(False,False)
        nw.geometry("1000x750+0+90")
        nw.configure(bg="purple")
        global i4,i5,i41,i51
        fr=Frame(nw)
        fon=("Britannic Bold",20,"bold")
        Label(nw,image=img8).place(x=0,y=0,relwidth=1,relheight=1)
        fr=Frame(nw,bd=10)
        fr .place(relx=0.005,rely=0.1,width=500,height=400)
        la=Label(fr,text="Welcome:"+str(i41),width="20",fg="blue")
        la.configure(font=fonts)
        la.place(relx=0.005,rely=0.1)
        OPT=(1,2,3,4,5,6,7,8)
        print(OPT[0])
        #opt1
        Label(fr,text="pickup location:",width="20",fg="blue").place(relx=0.2,rely=0.2)
        c.execute('select distinct pickup from busses')
        OPT1=c.fetchall()  
        print(OPT1)
        comb=StringVar()
        #comb.set(OPT1[0])
        ca=ttk.Combobox(fr,value=OPT1)
        ca.current(0)
        ca.bind("<<ComboboxSelected>>")
        ca.place(relx=0.4,rely=0.2)
        #opt2
        Label(fr,text="drop location:",width="20",fg="blue").place(relx=0.2,rely=0.25)
        c.execute('select distinct dropl from busses')
        OPT2=c.fetchall()  
        print(OPT2)
        comb=StringVar()
        comb.set(OPT2[0])
        cb=ttk.Combobox(fr,value=OPT2)
        cb.current(0)
        cb.bind("<<ComboboxSelected>>")
        cb.place(relx=0.4,rely=0.25)
        #opt3
        c.execute('select distinct pickti from busses')
        Label(fr,text="pickup time:",width="20",fg="blue").place(relx=0.2,rely=0.3)
        OPT3=c.fetchall()  
        print(OPT3)
        comb=StringVar()
        comb.set(OPT3[0])
        cc=ttk.Combobox(fr,value=OPT3)
        cc.current(0)
        cc.bind("<<ComboboxSelected>>")
        cc.place(relx=0.4,rely=0.3)
        #opt4
        c.execute('select distinct dropti from busses')
        OPT4=c.fetchall()
        Label(fr,text="drop time:",width="20",fg="blue").place(relx=0.2,rely=0.35)
        print(OPT4)
        comb=StringVar()
        comb.set(OPT4[0])
        cd=ttk.Combobox(fr,value=OPT4)
        cd.current(0)
        cd.bind("<<ComboboxSelected>>")
        cd.place(relx=0.4,rely=0.35)
        #opt5
        Label(fr,text="Fare :",width="20",fg="blue").place(relx=0.2,rely=0.4)
        c.execute('select distinct fare from busses')
        OPT5=c.fetchall()  
        print(OPT5)
        comb=StringVar()
        comb.set(OPT5[0])
        ce=ttk.Combobox(fr,value=OPT5)
        ce.current(0)
        ce.bind("<<ComboboxSelected>>")
        ce.place(relx=0.4,rely=0.4)
        #opt6
        Label(fr,text="Type of bus:",width="20",fg="blue").place(relx=0.2,rely=0.45)
        c.execute('select distinct type from busses')
        OPT6=c.fetchall()  
        print(OPT6)
        comb=StringVar()
        comb.set(OPT6[0])
        cf=ttk.Combobox(fr,value=OPT6)
        cf.current(0)
        cf.bind("<<ComboboxSelected>>")
        cf.place(relx=0.4,rely=0.45)
        #opt7
        Label(fr,text="year of travel:",width="20",fg="blue").place(relx=0.2,rely=0.5)
        #year
        OPT7=[2022]
        ih=10
        jh=2022
        while ih>0:
            jh+=1
            ih-=1
            OPT7.append(jh)
        print(OPT7)
        comb=IntVar()
        comb.set(OPT7[0])
        cg=ttk.Combobox(fr,value=OPT7)
        cg.current(0)
        cg.bind("<<ComboboxSelected>>")
        cg.place(relx=0.4,rely=0.5)
        #opt8
        Label(fr,text="month of travel:",width="20",fg="blue").place(relx=0.2,rely=0.55)
        OPT8=['01','02','03','04','05','06','07','08','09','10','11','12']
        print(OPT8)
        comb=StringVar()
        comb.set(OPT8[0])
        ch=ttk.Combobox(fr,value=OPT8)
        ch.current(0)
        ch.bind("<<ComboboxSelected>>")
        ch.place(relx=0.4,rely=0.55)
        Button(fr,text='click after entering choice',command=reb).place(relx=0.6,rely=0.65)
        lc=[]
        hc=0
        Label(fr,text="no of seats:",width="20",fg="blue").place(relx=0.2,rely=0.6)
        while hc<30:
            hc+=1
            lc.append(hc)
        ci1=ttk.Combobox(fr,value=OPT8)
        ci1.current(0)
        ci1.place(relx=0.4,rely=0.6)



def reb():
    global img9,ca,cb,cc,cd,ce,cf,cg,ch,c1,c2,c3,c4,c5,c6,c7,c8,crt,ci,mr,v
    c1=ca.get()#pickupl
    c2=cb.get()#dropl
    c3=cc.get()#pickti
    c4=cd.get()#Dropti
    c5=ce.get() #fare
    c6=cf.get() #type
    c7=cg.get()
    c8=ch.get()
    c9=ci1.get()
    img9=PhotoImage(file="Screenshot (288).png")
    nw=Toplevel()
    nw.title("bookings")
    nw.resizable(False,False)
    nw.geometry("1000x750+0+90")
    nw.configure(bg="purple")
    global i4,i5,i41,i51
    fr=Frame(nw)
    Label(nw,image=img9).place(x=0,y=0,relwidth=1,relheight=1)
    fr=Frame(nw,bd=10)
    fr .place(relx=0.001,rely=0.2,width=1000,height=400)
    #la=Label(fr,text="Welcome:"+str(i41),width="20",fg="blue")
    #la.configure(font=fonts)
    #la.place(relx=0.005,rely=0.1)
    #i41=StringVar()
    #i41.set("  Limit is 30")
    fon=("Britannic Bold",25,"bold")
    #i4=Entry(fr,textvariable=i41,cursor="hand2",width="40")
    Label(fr,text=str(i41)+' \' s' +' we found this based on your search.',font=fon,fg='blue').place(relx=0.1,rely=0.1)
    tab=ttk.Treeview(fr)
    tab['columns']=('r','p','e','f','g','h','q','w','y')
    tab.column("#0",anchor=E,width=1)
    tab.column("r",anchor=E,width=10)
    #tab.column("n",anchor=E,width=100)
    tab.column("p",anchor=CENTER,width=90)
    tab.column("e",anchor=E,width=90)
    tab.column("f",anchor=E,width=90)
    tab.column("g",anchor=E,width=90)
    tab.column("h",anchor=E,width=90)
    tab.column("q",anchor=E,width=90)
    tab.column("w",anchor=E,width=90)
    #tab.column("z",anchor=E,width=90)
    tab.column("y",anchor=E,width=90)
    tab.heading("r",text="sr no",anchor=CENTER)
    #tab.heading("n",text="user id",anchor=CENTER)
    tab.heading("p",text="issue no [bus]",anchor=CENTER)
    tab.heading("e",text="pickup location",anchor=CENTER)
    tab.heading("f",text="drop location",anchor=CENTER)
    tab.heading("g",text="pickup time",anchor=CENTER)
    tab.heading("h",text="drop time",anchor=CENTER)
    tab.heading("q",text="fare",anchor=CENTER)
    tab.heading("w",text="type",anchor=CENTER)
    tab.heading("y",text="seats left",anchor=CENTER)
    tab.place(relx=0.05,rely=0.3)
    #c.execute("use busmanagementsystem")
    c.execute("select issueno,pickup,dropl,pickti,dropti,fare,type,seatsleft,drivrname from busses where pickup = %s and dropl = %s and seatsleft >= %s",[c1,c2,c9])
    c.rowcount
    v=c.fetchall()
    print(v)
    if c. rowcount== 0:
        Label(fr,text='[ Note :'+' sorry '+str(i41)+' we dont have any bus from ' +str(c1)+' to '+str(c2)+' ]',font="fon1",fg='red').place(relx=0.1,rely=0.2)
    else:
        c.execute("select  issueno from busses where pickup = %s and dropl = %s ",[c1,c2])
        b=c.fetchall()
        crt=StringVar()
        crt.set(b[0])
        mr=ttk.Combobox(fr,value=b)
        mr.current(0)
        mr.bind("<<ComboboxSelected>>")
        mr.place(relx=0.2,rely=0.9)
        j=0
        Label(fr,text='select bus:',font='fon').place(relx=0.2,rely=0.8)
        for i in v:
                j+=1
                tab.insert(parent='',index='end',iid=j,text="srno",values=(j,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
        Button(fr,text='click after choosing bus from menu ',command=booked,font='fon',width='34').place(relx=0.7,rely=0.9)
        OPT9=[]
        if int(c7)%4==0:
            if c8 in ['01','03','05','07','08','10','12']:
                OPT9= ['01','03','05','07','08','10','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
            elif c8 == '02':
                 OPT9=['01','03','05','07','08','10','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29']
            else:
                OPT9= ['01','03','05','07','08','10','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
        else:
            if c8 in ['01','03','05','07','08','10','12']:
                OPT9= ['01','03','05','07','08','10','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
            elif c8 == '02':
                 OPT9=['01','03','05','07','08','10','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28']
            else:
                OPT9= ['01','03','05','07','08','10','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']

        print(OPT9)
        comb=StringVar()
        comb.set(OPT9[0])
        ci=ttk.Combobox(fr,value=OPT9)
        ci.current(0)
        ci.bind("<<ComboboxSelected>>")
        Label(fr,text='select date of travel:',font='fon').place(relx=0.4,rely=0.8)
        ci.place(relx=0.4,rely=0.9)
    
def booked():
    messagebox.showinfo('succes','journey booked and ticket is generated [PLZ TAKE IT\'S SCREENSHOT]')
    global img10,c1,c2,c3,c4,c5,c6,c7,c8,crt,ci,i4,i5,i41,i51,mr,c,db,ci1
    crt=mr.get()
    mvc=ci1.get()
    c.execute('select drivrname from busses where issueno = %s',[crt])
    r=c.fetchall()
    mdf=r[0]
    c.execute('select seatsleft from busses where issueno = %s',[crt])
    z=c.fetchall()
    c.execute('select pickup,dropl,pickti,dropti,fare,type,drivrname from busses where issueno = %s',[crt])
    mz=c.fetchall()
    cv=mz[0]
    print(cv)
    nrt=z[0]
    nrt=nrt[0]
    c9=ci.get()
    img10=PhotoImage(file="Screenshot (288).png")
    nw=Toplevel()
    nw1.title("ticket")
    nw.resizable(False,False)
    nw.geometry("1000x750+0+90")
    nw.configure(bg="purple")
    global i4,i5,i41,i51
    fr=Frame(nw)
    fon=("Britannic Bold",25,"bold")
    fir=("Bradley Hand ITC",15,"bold")
    Label(nw,image=img10).place(x=0,y=0,relwidth=1,relheight=1)
    fr=Frame(nw,bd=10)
    fr .place(relx=0.001,rely=0.2,width=1000,height=400)
    Label(fr,text='JOURNEY BOOKED :-) ENJOY',font=fon,fg='blue').place(relx=0.2,rely=0.1)
    Label(fr,text='Ticket',font=fon,fg='blue').place(relx=0.4,rely=0.2)
    Label(fr,text='[Note : take a screenshot to show to the conductor ]',fg='red').place(relx=0.4,rely=0.6)
    Label(fr,text='Issue no of booked bus : '+str(crt),font=fon,fg='blue').place(relx=0.4,rely=0.4)
    Label(fr,text='FROM:'+str(cv[0]),font=fir).place(relx=0.2,rely=0.3)
    Label(fr,text='TO: '+str(cv[1]),font=fir).place(relx=0.2,rely=0.4)
    Label(fr,text='PICKUP TIME: '+str(cv[2]),font=fir).place(relx=0.2,rely=0.5)
    Label(fr,text='DROP TIME: '+str(cv[3]),font=fir).place(relx=0.2,rely=0.6)
    Label(fr,text='FARE: '+str(cv[4]),font=fir).place(relx=0.2,rely=0.7)
    Label(fr,text='TYPE OF BUS: '+str(cv[5]),font=fir).place(relx=0.2,rely=0.8)
    Label(fr,text='SEATS BOOKED: '+str(mvc),font=fir).place(relx=0.2,rely=0.8)
    date=str(c7)+'/'+str(c8)+'/'+str(c9)
    Label(fr,text='DAY: '+date,font=fir).place(relx=0.2,rely=0.9)
    sql="insert into bookings values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    print((i41,crt,cv[0],cv[1],int(cv[2]),int(cv[3]),cv[4],cv[5],date,mdf[0],int(mvc)))
    c.execute(sql,(i41,crt,cv[0],cv[1],int(cv[2]),int(cv[3]),cv[4],cv[5],date,mdf[0],mvc))
    db1.commit()
    c.execute('update busses set seatsleft = %s-%s where issueno = %s',[nrt,mvc,crt])
    
        
def m3():
    m=1
    global img5,i41
    img5=PhotoImage(file="Screenshot (95).png")
    nw=Toplevel()
    nw.resizable(False,False)
    nw.geometry("1000x750+0+90")
    nw.configure(bg="purple")
    global i4,i5,i41,i51
    fr=Frame(nw)
    Label(nw,image=img5).place(x=0,y=0,relwidth=1,relheight=1)
    fr=Frame(nw,bd=10)
    fr .place(relx=0.001,rely=0.2,width=1000,height=400)
    #la=Label(fr,text="Welcome:"+str(i41),width="20",fg="blue")
    #la.configure(font=fonts)
    #la.place(relx=0.005,rely=0.1)
    #i41=StringVar()
    #i41.set("  Limit is 30")
    fon=("Britannic Bold",25,"bold")
    #i4=Entry(fr,textvariable=i41,cursor="hand2",width="40")
    Label(fr,text=str(i41)+' s' +' Bookings are ...',font=fon,fg='blue').place(relx=0.1,rely=0.1)
    tab=ttk.Treeview(fr)
    tab['columns']=('r','n','p','e','f','g','h','q','w','z','y','a')
    tab.column("#0",anchor=E,width=1)
    tab.column("r",anchor=E,width=10)
    tab.column("n",anchor=E,width=90)
    tab.column("p",anchor=CENTER,width=70)
    tab.column("e",anchor=E,width=70)
    tab.column("f",anchor=E,width=70)
    tab.column("g",anchor=E,width=70)
    tab.column("h",anchor=E,width=70)
    tab.column("q",anchor=E,width=70)
    tab.column("w",anchor=E,width=70)
    tab.column("z",anchor=E,width=70)
    tab.column("y",anchor=E,width=70)
    tab.column("a",anchor=E,width=70)
    tab.heading("r",text="sr no",anchor=CENTER)
    tab.heading("n",text="user id",anchor=CENTER)
    tab.heading("p",text="issue no [bus]",anchor=CENTER)
    tab.heading("e",text="pickup location",anchor=CENTER)
    tab.heading("f",text="drop location",anchor=CENTER)
    tab.heading("g",text="pickup time",anchor=CENTER)
    tab.heading("h",text="drop time",anchor=CENTER)
    tab.heading("q",text="fare",anchor=CENTER)
    tab.heading("w",text="type Of bus",anchor=CENTER)
    tab.heading("z",text="date",anchor=CENTER)
    tab.heading("y",text="drivers name",anchor=CENTER)
    tab.heading("a",text="seats boooked",anchor=CENTER)
    tab.place(relx=0.02,rely=0.3,width=950)
    #c.execute("use busmanagementsystem")
    c.execute("select * from bookings where userid = %s",[i41])
    c.rowcount
    if c.rowcount==0:
        Label(fr,text='[ Note :'+' sorry '+str(i41)+' you have no journeys booked ' +']',font="fon1",fg='red').place(relx=0.1,rely=0.2)
    l=c.fetchall()
    global j
    j=0
    for i in l:
        j+=1
        tab.insert(parent='',index='end',iid=j,text="srno",values=(j,i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10])) 


#faltu
def m4():
        m=1
        global img5,i41
        img5=PhotoImage(file="myimg1.png")
        nw=Toplevel()
        nw.title("check your journey ")
        nw.resizable(False,False)
        nw.geometry("1000x750+0+90")
        nw.configure(bg="purple")
        global i4,i5,i41,i51
        fr=Frame(nw)
        fon=("Copperplate Gothic Bold",10,"bold")
        Label(nw,image=img5).place(x=0,y=0,relwidth=1,relheight=1)
        fr=Frame(nw,bd=10)
        fr .place(relx=0.25,rely=0.2,width=500,height=400)
        la=Label(fr,text="Welcome:"+str(i41),width="20",fg="blue")
        la.configure(font=fonts)
        la.place(relx=0.005,rely=0.1)
        i4=Entry(fr,textvariable=i41,cursor="hand2",width="40")
        Button(fr,text="To check you current bookings",width="30",font=fon,fg="orange",command=m3).place(relx=0.1,rely=0.3)
        Button(fr,text="To plan a new journey",width="30",font=fon,fg="orange",command=m10).place(relx=0.1,rely=0.4)




def sau():
    global  c,db1,img201,cra
    img201=PhotoImage(file="Screenshot (95).png")
    nw=Toplevel()
    nw.resizable(False,False)
    nw.geometry("1000x750+0+90")
    nw.configure(bg="purple")
    nw.title("user info.")
    global i4,i5,i41,i51
    fr=Frame(nw)
    fon=("Britannic Bold",20,"bold")
    Label(nw,image=img201).place(x=0,y=0,relwidth=1,relheight=1)
    fr=Frame(nw,bd=10)
    fr .place(relx=0.3,rely=0.3,width=500,height=400)
    Label(fr,text='Users Are ...',font=fon,fg='blue').place(relx=0.1,rely=0.1)
    tab=ttk.Treeview(fr)
    tab['columns']=('r','n','p','e')
    tab.column("#0",anchor=E,width=1)
    tab.column("r",anchor=E,width=10)
    tab.column("n",anchor=E,width=100)
    tab.column("p",anchor=CENTER,width=100)
    tab.column("e",anchor=E,width=100)
    tab.heading("r",text="sr no",anchor=CENTER)
    tab.heading("n",text="user id",anchor=CENTER)
    tab.heading("p",text="password",anchor=CENTER)
    tab.heading("e",text="email id",anchor=CENTER)
    tab.place(relx=0.2,rely=0.3)
    #c.execute("use busmanagementsystem")
    c.execute("select * from user ")
    l=c.fetchall()
    global j
    j=0
    for i in l:
        j+=1
        tab.insert(parent='',index='end',iid=j,text="srno",values=(j,i[0],i[1],i[2]))    

def sucb():
    global  c,db1,img202,cra
    img202=PhotoImage(file="Screenshot (95).png")
    nw=Toplevel()
    nw.resizable(False,False)
    nw.geometry("1000x750+0+90")
    nw.configure(bg="purple")
    nw.title("bookings")
    global i4,i5,i41,i51
    fr=Frame(nw)
    fon=("Britannic Bold",20,"bold")
    Label(nw,image=img202).place(x=0,y=0,relwidth=1,relheight=1)
    fr=Frame(nw,bd=10)
    fr .place(relx=0.005,rely=0.2,width=1000,height=400)
    Label(fr,text='Bookings are ...',font=fon,fg='blue').place(relx=0.1,rely=0.1)
    tab=ttk.Treeview(fr)
    tab['columns']=('r','n','p','e','f','g','h','q','w','z','y','a')
    tab.column("#0",anchor=E,width=1)
    tab.column("r",anchor=E,width=10)
    tab.column("n",anchor=E,width=90)
    tab.column("p",anchor=CENTER,width=70)
    tab.column("e",anchor=E,width=70)
    tab.column("f",anchor=E,width=70)
    tab.column("g",anchor=E,width=70)
    tab.column("h",anchor=E,width=70)
    tab.column("q",anchor=E,width=70)
    tab.column("w",anchor=E,width=70)
    tab.column("z",anchor=E,width=70)
    tab.column("y",anchor=E,width=70)
    tab.column("a",anchor=E,width=70)
    tab.heading("r",text="sr no",anchor=CENTER)
    tab.heading("n",text="user id",anchor=CENTER)
    tab.heading("p",text="issue no [bus]",anchor=CENTER)
    tab.heading("e",text="pickup location",anchor=CENTER)
    tab.heading("f",text="drop location",anchor=CENTER)
    tab.heading("g",text="pickup time",anchor=CENTER)
    tab.heading("h",text="drop time",anchor=CENTER)
    tab.heading("q",text="fare",anchor=CENTER)
    tab.heading("w",text="type Of bus",anchor=CENTER)
    tab.heading("z",text="date",anchor=CENTER)
    tab.heading("y",text="drivers name",anchor=CENTER)
    tab.heading("a",text="seats boooked",anchor=CENTER)
    tab.place(relx=0.02,rely=0.3,width=950)
    #c.execute("use busmanagementsystem")
    c.execute("select * from bookings ")
    l=c.fetchall()
    if c.rowcount == 0:
            Label(fr,text='[sorry we don\'t have any bookings]',fg='red').place(relx=0.2,rely=0.2)
    global j
    j=0
    for i in l:
        j+=1
        tab.insert(parent='',index='end',iid=j,text="srno",values=(j,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]))    

    return




def sab():
    global c
    global  c,db1,img204,cra
    img204=PhotoImage(file="Screenshot (95).png")
    nw=Toplevel()
    nw.resizable(False,False)
    nw.geometry("1000x750+0+90")
    nw.configure(bg="purple")
    nw.title("busses")
    global i4,i5,i41,i51
    fr=Frame(nw)
    fon=("Britannic Bold",20,"bold")
    Label(nw,image=img204).place(x=0,y=0,relwidth=1,relheight=1)
    fr=Frame(nw,bd=10)
    fr .place(relx=0.001,rely=0.2,width=1000,height=400)
    Label(fr,text='Busses Are []==[]=======/...',font=fon,fg='blue').place(relx=0.1,rely=0.1)
    tab=ttk.Treeview(fr)
    tab['columns']=('r','n','p','e','f','g','h','q','w','z','y')
    tab.column("#0",anchor=E,width=1)
    tab.column("r",anchor=E,width=10)
    tab.column("n",anchor=E,width=100)
    tab.column("p",anchor=CENTER,width=90)
    tab.column("e",anchor=E,width=90)
    tab.column("f",anchor=E,width=90)
    tab.column("g",anchor=E,width=90)
    tab.column("h",anchor=E,width=90)
    tab.column("q",anchor=E,width=90)
    tab.column("w",anchor=E,width=90)
    tab.column("z",anchor=E,width=90)
    tab.column("y",anchor=E,width=90)
    tab.heading("r",text="sr no",anchor=CENTER)
    tab.heading("n",text="Issue no.",anchor=CENTER)
    tab.heading("p",text="Driver Name",anchor=CENTER)
    tab.heading("e",text="pickup location",anchor=CENTER)
    tab.heading("f",text="drop location",anchor=CENTER)
    tab.heading("g",text="pickup time",anchor=CENTER)
    tab.heading("h",text="drop time",anchor=CENTER)
    tab.heading("q",text="total seats",anchor=CENTER)
    tab.heading("w",text="seats left",anchor=CENTER)
    tab.heading("z",text="Fare",anchor=CENTER)
    tab.heading("y",text="Type",anchor=CENTER)
    tab.place(relx=0.05,rely=0.3)
    #c.execute("use busmanagementsystem")
    c.execute("select * from busses ")
    l=c.fetchall()
    global j
    j=0
    for i in l:
        j+=1
        tab.insert(parent='',index='end',iid=j,text="srno",values=(j,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))    







def switch():    
    global m,buto
    global n
    m=2
    print(m)
    if buto["state"]!=NORMAL:
        buto["state"]=NORMAL

x,y,mq,mw="","","",""
def adm():
    global img4,z
    z1=z.get()
    if len(z1)==0:
        messagebox.showinfo('error','all fields are required')
    elif len(z1)!=0:
        if z1=="Admin":
            global img5
            fon=("Britannic Bold",25,"bold")
            nw1=Toplevel()
            nw1.configure(bg="purple")
            nw1.resizable(False,False)
            nw1.title('admin window')
            nw1.geometry("1000x750")
            img5=PhotoImage(file="imd1.png")
            Label(nw1,image=img5,width="3840",height="2160").place(x=-1400,y=-1000,width="3840",height="2160")
            fr=Frame(nw1)
            fr .place(relx=0.25,rely=0.2,width=500,height=400)
            Label(fr,text="Admin Dashboard",height="3",font=fon,fg="orange").place(x=100,rely=0.01)
            Button(fr,text="See Current Bookings",bd=5,height="3",width="15",command=sucb).place(relx=0.2,rely=0.25)
            Button(fr,text="See All Users",bd=5,height="3",width="15",command=sau).place(relx=0.6,rely=0.25)
            Button(fr,text="See All Busses",bd=5,height="3",width="15",command=sab).place(relx=0.2,rely=0.4)
            Button(fr,text="Delete Bus",bd=5,height="3",width="15",command=db).place(relx=0.6,rely=0.4)
            Button(fr,text="Add More Busses",bd=5,height="3",width="15",command=ab).place(relx=0.2,rely=0.55)
            Button(fr,text="Delete Users",bd=5,height="3",width="15",command=du).place(relx=0.6,rely=0.55) 
            Button(fr,text="add seats to a buss",bd=5,height="3",width="15",command=xms).place(relx=0.2,rely=0.7)
            Button(fr,text="see conductors",bd=5,height="3",width="15",command=sc).place(relx=0.6,rely=0.7)
            Button(fr,text="Delete bookings",bd=5,height="3",width="15",command=drtb).place(relx=0.2,rely=0.85)
        else:
            messagebox.showinfo('incorrect','incorrect password try again')


def sc():
    global  c,db1,img21,cra
    img21=PhotoImage(file="Screenshot (97).png")
    nw=Toplevel()
    nw.title("conductor\'s info")
    nw.resizable(False,False)
    nw.geometry("1000x750+0+90")
    nw.configure(bg="purple")
    global i4,i5,i41,i51
    fr=Frame(nw)
    fon=("Britannic Bold",20,"bold")
    Label(nw,image=img21).place(x=0,y=0,relwidth=1,relheight=1)
    fr=Frame(nw,bd=10)
    fr .place(relx=0.005,rely=0.1,width=500,height=400)
    Label(fr,text='Conductors Are ...',font=fon,fg='blue').place(relx=0.1,rely=0.1)
    tab=ttk.Treeview(fr)
    tab['columns']=('r','n','p','z')
    tab.column("#0",anchor=E,width=1)
    tab.column("r",anchor=E,width=10)
    tab.column("n",anchor=E,width=100)
    tab.column("p",anchor=CENTER,width=100)
    tab.column("z",anchor=CENTER,width=100)
    tab.heading("r",text="sr no",anchor=CENTER)
    tab.heading("n",text="conductor id",anchor=CENTER)
    tab.heading("p",text="password",anchor=CENTER)
    tab.heading("z",text="Bus issue no",anchor=CENTER)
    tab.place(relx=0.2,rely=0.3)
    #c.execute("use busmanagementsystem")
    c.execute("select conductorid, conpass,issueno from busses ")
    l=c.fetchall()
    global j
    j=0
    for i in l:
        j+=1
        tab.insert(parent='',index='end',iid=j,text="srno",values=(j,i[0],i[1],i[2]))

     
def xms():
    global  c,db1,img31,cra
    img31=PhotoImage(file="Screenshot (97).png")
    nw=Toplevel()
    nw.resizable(False,False)
    nw.geometry("1000x750+0+90")
    nw.configure(bg="purple")
    nw.title("busses")
    global i4,i5,i41,i51
    fr=Frame(nw)
    fon=("Britannic Bold",20,"bold")
    Label(nw,image=img31).place(x=0,y=0,relwidth=1,relheight=1)
    fr=Frame(nw,bd=10)
    fr .place(relx=0.005,rely=0.1,width=500,height=400)
    la=Label(fr,text="Welcome: admin",width="20",fg="blue")
    la.configure(font=fonts)
    la.place(relx=0.005,rely=0.1)
    opt=[]
    c.execute('select issueno from busses')
    opt=c.fetchall()
    cra=ttk.Combobox(fr,values=opt)
    cra.current(0)
    cra.bind("<<ComboboxSelected>>",nopt)
    Label(fr,text='select bus',font=("Britannic Bold",10,"bold")).place(relx=0.2,rely=0.3)
    cra.place(relx=0.4,rely=0.4)


def nopt(r):
    global  c,db1,img21,cra,crs,ct
    md=cra.get()
    img21=PhotoImage(file="Screenshot (97).png")
    nw=Toplevel()
    nw.resizable(False,False)
    nw.geometry("1000x750+0+90")
    nw.title("add seats")
    nw.configure(bg="purple")
    global i4,i5,i41,i51
    fr=Frame(nw)
    fon=("Britannic Bold",20,"bold")
    Label(nw,image=img21).place(x=0,y=0,relwidth=1,relheight=1)
    fr=Frame(nw,bd=10)
    fr .place(relx=0.005,rely=0.1,width=500,height=400)
    la=Label(fr,text="Welcome: admin",width="20",fg="blue")
    la.configure(font=fonts)
    la.place(relx=0.005,rely=0.1)
    opt=[]
    c.execute('select seatsleft from busses where issueno = %s',[md])
    mn=c.fetchall()
    c.execute('select totalseats from busses where issueno = %s',[md])
    nm=c.fetchall()
    c.execute('select * from bookings where issueno = %s',[md])
    z=c.rowcount
    print(nm,mn)
    ct=nm[0][0]-mn[0][0]-z
    i=0
    while ct>0:
        opt.append(i)
        ct-=1
        i+=1
    crs=ttk.Combobox(fr,values=opt)
    crs.current(0)
    crs.bind("<<ComboboxSelected>>",nopb)
    Label(fr,text='select no of seats to be added',font=("Britannic Bold",10,"bold")).place(relx=0.2,rely=0.3)
    crs.place(relx=0.4,rely=0.4)
    #Button(fr,text="click after electing seats",bd=5,height="3",width="20",command= nopb).place(relx=0.6,rely=0.9)

def nopb(r):
    global crs,cra,c,db1,ct
    s=cra.get()
    c.execute('select seatsleft from busses where issueno = %s',[s])
    mn=c.fetchall()
    #c.execute('select * from bookings where issueno = %s',[s])
    #z=c.rowcount
    d=crs.get()
    c.execute('update busses set seatsleft = %s +%s where issueno = %s',(d,mn[0][0],s))
    db1.commit()
    messagebox.showinfo('done','seats are added')

def drtb():
    global c,c12,c121
    global  c,db1,img204,cra
    img204=PhotoImage(file="Screenshot (95).png")
    nw=Toplevel()
    nw.title("delete bookings")
    nw.resizable(False,False)
    nw.geometry("1000x750+0+90")
    nw.configure(bg="purple")
    global i4,i5,i41,i51
    fr=Frame(nw)
    fon=("Britannic Bold",20,"bold")
    Label(nw,image=img204).place(x=0,y=0,relwidth=1,relheight=1)
    fr=Frame(nw,bd=10)
    fr .place(relx=0.005,rely=0.2,width=1000,height=400)
    Label(fr,text='Bookings are ...',font=fon,fg='blue').place(relx=0.1,rely=0.1)
    tab=ttk.Treeview(fr)
    tab['columns']=('r','n','p','e','f','g','h','q','w','z','y','a')
    tab.column("#0",anchor=E,width=1)
    tab.column("r",anchor=E,width=10)
    tab.column("n",anchor=E,width=90)
    tab.column("p",anchor=CENTER,width=70)
    tab.column("e",anchor=E,width=70)
    tab.column("f",anchor=E,width=70)
    tab.column("g",anchor=E,width=70)
    tab.column("h",anchor=E,width=70)
    tab.column("q",anchor=E,width=70)
    tab.column("w",anchor=E,width=70)
    tab.column("z",anchor=E,width=70)
    tab.column("y",anchor=E,width=70)
    tab.column("a",anchor=E,width=70)
    tab.heading("r",text="sr no",anchor=CENTER)
    tab.heading("n",text="user id",anchor=CENTER)
    tab.heading("p",text="issue no [bus]",anchor=CENTER)
    tab.heading("e",text="pickup location",anchor=CENTER)
    tab.heading("f",text="drop location",anchor=CENTER)
    tab.heading("g",text="pickup time",anchor=CENTER)
    tab.heading("h",text="drop time",anchor=CENTER)
    tab.heading("q",text="fare",anchor=CENTER)
    tab.heading("w",text="type Of bus",anchor=CENTER)
    tab.heading("z",text="date",anchor=CENTER)
    tab.heading("y",text="drivers name",anchor=CENTER)
    tab.heading("a",text="seats boooked",anchor=CENTER)
    tab.place(relx=0.02,rely=0.3,width=950)
    #c.execute("use busmanagementsystem")
    c.execute("select * from bookings ")
    l=c.fetchall()
    global j
    j=0
    for i in l:
        j+=1
        tab.insert(parent='',index='end',iid=j,text="srno",values=(j,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]))
    srl="select issueno from bookings "
    c.execute(srl)
    OPTo=c.fetchall()
    if len(OPTo)!=0:
        Label(fr,text="[Note : the data will be deleted ones you close this window ]",font="fon1",fg='red').place(relx=0.1,rely=0.2)
        Label(fr,text="select issue no",font="fon1",fg='black').place(relx=0.3,rely=0.7)
        comb=StringVar()
        c12=ttk.Combobox(fr,value=OPTo)
        c12.current(0)
        c12.bind("<<ComboboxSelected>>")
        c12.place(relx=0.4,rely=0.8)
        Label(fr,text="select user",font="fon1",fg='black').place(relx=0.5,rely=0.7)
        srl="select userid from bookings "
        c.execute(srl)
        OPTo1=c.fetchall()  
        comb=StringVar()
        comb.set(OPTo1[0])
        c121=ttk.Combobox(fr,value=OPTo1)
        c121.current(0)
        c121.bind("<<ComboboxSelected>>")
        c121.place(relx=0.6,rely=0.8)
        Button(fr,text="delete  selected booking",bd=5,height="3",width="20",command= crm).place(relx=0.6,rely=0.9)
    else:
        Label(fr,text='sorry we dont have any journeys booked :-0 :-((',fg='red').place(relx=0.2,rely=0.2)


    
def crm():
    global c,db1,c12,c121
    cm=c12.get()
    cr=c121.get()
    c.execute('select seatsleft from busses where issueno = %s',[cm])
    mb=c.fetchall()
    
    print(cm,cr)
    c.execute('DELETE FROM BOOKINGS WHERE ISSUENO =%s AND USERID = %s',(cm,cr))
    r=c.rowcount
    c.execute('update busses set seatsleft = %s +%s where issueno = %s',(mb[0][0],r,cm))
    db1.commit()
    messagebox.showinfo('success','booking is deleted')


    
def db():
    global img8,c,c2
    global  c,db1,img204,cra
    img204=PhotoImage(file="Screenshot (95).png")
    nw=Toplevel()
    nw.resizable(False,False)
    nw.geometry("1000x750+0+90")
    nw.configure(bg="purple")
    nw.title("busses")
    global i4,i5,i41,i51
    fr=Frame(nw)
    fon=("Britannic Bold",20,"bold")
    Label(nw,image=img204).place(x=0,y=0,relwidth=1,relheight=1)
    fr=Frame(nw,bd=10)
    Label(fr,text="[Note : the data will be deleted ones you close this window the bookings associated will also vanish]",font="fon1",fg='red').place(relx=0.1,rely=0.2)
    fr .place(relx=0.001,rely=0.1,width=1000,height=550)
    Label(fr,text='Busses Are []==[]=======/...',font=fon,fg='blue').place(relx=0.1,rely=0.1)
    tab=ttk.Treeview(fr)
    tab['columns']=('r','n','p','e','f','g','h','q','w','z','y')
    tab.column("#0",anchor=E,width=1)
    tab.column("r",anchor=E,width=10)
    tab.column("n",anchor=E,width=100)
    tab.column("p",anchor=CENTER,width=90)
    tab.column("e",anchor=E,width=90)
    tab.column("f",anchor=E,width=90)
    tab.column("g",anchor=E,width=90)
    tab.column("h",anchor=E,width=90)
    tab.column("q",anchor=E,width=90)
    tab.column("w",anchor=E,width=90)
    tab.column("z",anchor=E,width=90)
    tab.column("y",anchor=E,width=90)
    tab.heading("r",text="sr no",anchor=CENTER)
    tab.heading("n",text="Issue no",anchor=CENTER)
    tab.heading("p",text="Driver Name",anchor=CENTER)
    tab.heading("e",text="pickup location",anchor=CENTER)
    tab.heading("f",text="drop location",anchor=CENTER)
    tab.heading("g",text="pickup time",anchor=CENTER)
    tab.heading("h",text="drop time",anchor=CENTER)
    tab.heading("q",text="total seats",anchor=CENTER)
    tab.heading("w",text="seats left",anchor=CENTER)
    tab.heading("z",text="Fare",anchor=CENTER)
    tab.heading("y",text="Type",anchor=CENTER)
    tab.place(relx=0.05,rely=0.4)
    #c.execute("use busmanagementsystem")
    c.execute("select * from busses ")
    l=c.fetchall()
    global j
    j=0
    for i in l:
        j+=1
        tab.insert(parent='',index='end',iid=j,text="srno",values=(j,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
    Label(fr,text="select bus",font="fon1",fg='black').place(relx=0.3,rely=0.3)
    srl="select issueno from busses "
    c.execute(srl)
    OPT=c.fetchall()  
    c2=ttk.Combobox(fr,value=OPT)
    c2.current(0)
    c2.bind("<<ComboboxSelected>>")
    c2.place(relx=0.4,rely=0.3)
    Button(fr,text="delete  selected bus",bd=5,height="3",width="15",command= cr).place(relx=0.6,rely=0.25)

def cr():
    global c2,c,db1
    m=c2.get()
    print(m)
    sql="Delete from busses where issueno = %s"
    spl="Delete from bookings where issueno = %s"
    c.execute(sql,(m,))
    c.execute(spl,(m,))
    db1.commit()
    messagebox.showinfo('deleted', 'deleted bus with issue no.'+str(m))
    return



def ab():
        m=1
        global img1
        img1=PhotoImage(file="main back.png")
        nw=Toplevel()
        nw.title("isssue bus")
        nw.geometry("1000x750+0+90")
        nw.configure(bg="purple")
        nw.resizable(False,False)
        global aa,a1,bb,b1,kk,kz,ka,kb,kc,kd,ke,kf,kg,kh,ki,ka1,kb1,kc1,kd1,ke1,kf1,kg1,kh1,ki1
        fr=Frame(nw)
        fon=("Copperplate Gothic Bold",10,"bold")
        Label(nw,image=img1).place(x=0,y=0,relwidth=1,relheight=1)
        fr=Frame(nw,bd=10)
        fr .place(relx=0.25,rely=0,width=1000,height=750)
        la=Label(fr,text="Welcome Admin",width="20",fg="blue")
        la.configure(font=fonts)
        la.place(relx=0.000005,rely=0.1)
        a1=StringVar()
        a1.set(" Limit  15")
        aa=Entry(fr,textvariable=a1,cursor="hand2",width="40")
        Label(fr,text="issue no",width="10",font=fon,fg="orange").place(relx=0.1,rely=0.2)
        Label(fr,text="Driver Name",width="10",font=fon,fg="orange").place(relx=0.1,rely=0.25)
        Label(fr,text="Pickup location",width="10",font=fon,fg="orange").place(relx=0.1,rely=0.3)
        aa.place(relx=0.3,rely=0.2)
        b1=StringVar()
        b1.set("limit 15")
        bb=Entry(fr,text="limit=10",textvariable=b1,cursor="hand2",width="40")
        bb.place(relx=0.3,rely=0.25)
        kz=StringVar()
        kz.set("limit=15")
        kk=Entry(fr,text="limit=20",textvariable=kz,cursor="hand2",width="40")
        kk.place(relx=0.3,rely=0.3)
        fonts1=("Broadway",10,"bold")
        ka1=StringVar()
        ka1.set("limit=15")
        Label(fr,text="Drop Location",width="10",font=fon,fg="orange").place(relx=0.1,rely=0.35)
        ka=Entry(fr,text="limit=20",textvariable=ka1,cursor="hand2",width="40")
        ka.place(relx=0.3,rely=0.35)
        kb1=StringVar()
        kb1.set("limit=15")
        Label(fr,text="Pickup time",width="10",font=fon,fg="orange").place(relx=0.1,rely=0.4)
        kb=Entry(fr,text="limit=20",textvariable=kb1,cursor="hand2",width="40")
        kb.place(relx=0.3,rely=0.4)
        kc1=StringVar()
        kc1.set("limit=15")
        Label(fr,text="Drop time",width="10",font=fon,fg="orange").place(relx=0.1,rely=0.45)
        kc=Entry(fr,text="limit=20",textvariable=kc1,cursor="hand2",width="40")
        kc.place(relx=0.3,rely=0.45)
        kd1=IntVar()
        kd1.set("limit=11")
        Label(fr,text="total seats",width="10",font=fon,fg="orange").place(relx=0.1,rely=0.5)
        kd=Entry(fr,text="limit=20",textvariable=kd1,cursor="hand2",width="40")
        kd.place(relx=0.3,rely=0.5)
        ke1=IntVar()
        ke1.set("limit=11")
        Label(fr,text="Seats Left",width="10",font=fon,fg="orange").place(relx=0.1,rely=0.55)
        ke=Entry(fr,text="limit=20",textvariable=ke1,cursor="hand2",width="40")
        ke.place(relx=0.3,rely=0.55)
        kf1=IntVar()
        kf1.set("limit=10")
        Label(fr,text="Fare",width="10",font=fon,fg="orange").place(relx=0.1,rely=0.6)
        kf=Entry(fr,text="limit=20",textvariable=kf1,cursor="hand2",width="40")
        kf.place(relx=0.3,rely=0.6)
        kg1=StringVar()
        kg1.set("limit=10")
        Label(fr,text="Type",width="10",font=fon,fg="orange").place(relx=0.1,rely=0.65)
        kg=Entry(fr,text="limit=20",textvariable=kg1,cursor="hand2",width="40")
        kg.place(relx=0.3,rely=0.65)
        Label(fr,text="conductor name ",width="20",font=fon,fg="orange").place(relx=0.1,rely=0.7)
        Label(fr,text="his/her passwd. ",width="20",font=fon,fg="orange").place(relx=0.1,rely=0.75)
        kh1=StringVar()
        kh1.set('limit is 20')
        kh=Entry(fr,textvariable=kh1,cursor='hand2',width='40')
        kh.place(relx=0.3,rely=0.7)
        ki1=StringVar()
        ki1.set('limit is 20')
        ki=Entry(fr,textvariable=ki1,cursor='hand2',width='40')
        ki.place(relx=0.3,rely=0.75)
        bbtn=Button(nw,text="click after choosing ",cursor="hand2",width="20",fg="blue",height="3",command=rtb,bd=5)
        bbtn.configure(font=fonts1)
        bbtn.place(x=375,y=610)





def rtb():
    global aa,a1,bb,b1,kk,kz,ka,kb,kc,kd,ke,kf,kgkh,ki,ka1,kb1,kc1,kd1,ke1,kf1,kg1,kh1,ki1
    a1=aa.get()
    b1=bb.get()
    kz=kk.get()
    ka1=ka.get()
    kb1=kb.get()
    kc1=kc.get()
    kd1=kd.get()
    ke1=ke.get()
    kf1=kf.get()
    kg1=kg.get()
    kh1=kh.get()
    ki1=ki.get()
    print(a1,b1,kz,ka1,kb1,kc1,kd1,ke1,kf1,kg1)
    #if len(a1)==0 or len(b1)==0 or len(kz)==0 or len(ka1)==0 or len(kb1)==0 or len(str(kc1))==0 or len(str(kd1))==0 or len(str(ke1))==0 or len(kf1)==0 or len(kg)==0 or len(a1)>=15 or len(b1)>=15 or len(kz)>=15 or len(ka1)>=15 or len(kb1)>=15 or len(str(kc1))>=11 or len(str(kd1))>=11 or len(str(ke1))>=11 or len(kf1)>=10 or len(kg1)>=10: 
 #       messagebox.showinfo('error','all fields are required and should be under given limits')
   # else:'''
    sql="insert into busses values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    c.execute(sql,(a1,b1,kz,ka1,kb1,kc1,kd1,ke1,kf1,kg1,kh1,ki1))
    db1.commit()
    messagebox.showinfo('success',' fields are entered in system')






def du():
    global img2,c,c3
    global  c,db1,img204,cra
    img204=PhotoImage(file="Screenshot (95).png")
    nw=Toplevel()
    nw.title("users info")
    nw.resizable(False,False)
    nw.geometry("1000x750+0+90")
    nw.configure(bg="purple")
    global i4,i5,i41,i51
    fr=Frame(nw)
    fon=("Britannic Bold",20,"bold")
    Label(nw,image=img204).place(x=0,y=0,relwidth=1,relheight=1)
    fr=Frame(nw,bd=10)
    fr .place(relx=0.25,rely=0.2,width=500,height=550)
    Label(fr,text='Users Are ...',font=fon,fg='blue').place(relx=0.1,rely=0.1)
    Label(fr,text="[Note : the data will be deleted ones you clase this window]",font="fon1",fg='red').place(relx=0.1,rely=0.2)
    tab=ttk.Treeview(fr)
    tab['columns']=('r','n','p','e')
    tab.column("#0",anchor=E,width=1)
    tab.column("r",anchor=E,width=10)
    tab.column("n",anchor=E,width=100)
    tab.column("p",anchor=CENTER,width=100)
    tab.column("e",anchor=E,width=100)
    tab.heading("r",text="sr no",anchor=CENTER)
    tab.heading("n",text="user id",anchor=CENTER)
    tab.heading("p",text="password",anchor=CENTER)
    tab.heading("e",text="email id",anchor=CENTER)
    tab.place(relx=0.1,rely=0.3)
    #c.execute("use busmanagementsystem")
    c.execute("select * from user ")
    l=c.fetchall()
    global j
    j=0
    for i in l:
        j+=1
        tab.insert(parent='',index='end',iid=j,text="srno",values=(j,i[0],i[1],i[2]))
    Label(fr,text="select bus",font="fon1",fg='black').place(relx=0.2,rely=0.9)
    sql="select userid from user "
    c.execute(sql)
    OPT=c.fetchall()  
    print(OPT)
    comb=StringVar()
    comb.set(OPT[0])
    c3=ttk.Combobox(fr,value=OPT)
    c3.current(0)
    c3.bind("<<ComboboxSelected>>")
    c3.place(relx=0.4,rely=0.9)
    Button(fr,text="delete  selected user",bd=5,height="3",width="15",command= cs).place(relx=0.7,rely=0.9)

def cs():
    global c3,c,db1
    m=c3.get()
    sql="delete from user where userid = %s"
    spl="Delete from bookings where userid = %s"
    c.execute(sql,(m,))
    c.execute(spl,(m,))
    db1.commit()
    messagebox.showinfo('deleted', 'deleted user with user id'+str(m))
    return





def switch1():   
    global m
    m=1
    if buto["state"]!=NORMAL:
        buto["state"]=NORMAL
root.configure(bg="purple")
root.resizable(False,False)





img=PhotoImage(file="loginimg.png")
Label(root,image=img).place(x=0,y=0,relwidth=1,relheight=1)
fr=Frame(root)
 

root.geometry("1000x750+100+0")
root.title("opening window")
la=Label(fr,text="Bus Management Apk",width="25",fg="blue")
fonts=("Britannic Bold",25,"bold")
la.configure(font=fonts)
la.place(relx=0.001,rely=0.1)


m=IntVar()
m.current=1
mn=Radiobutton(fr,text="log in ",variable=m,cursor="hand2",value=1,width="10",height="2",command=lambda:enter(1),bg="#d3d3d3",fg="orange")
ln=Radiobutton(fr,text="sign up ",variable=m,cursor="hand2",value=2,width="10",height="2",command=lambda:enter(2),bg="#d3d3d3",fg="orange")
fonts1=("Broadway",20,"bold")
ln.configure(font=fonts1)
mn.configure(font=fonts1)
ln.place(relx=0.3,rely=0.4)
mn.place(relx=0.3,rely=0.6)
buto=Button(fr,text="click after choosing ",cursor="hand2",width="20",state=DISABLED,command=enter)
#.place(relx=0.37,rely=0.9)
fr .place(relx=0.25,rely=0.2,width=500,height=400)
root.mainloop()

