from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector as conn
import smtplib
import random


def validation(request):
    return render(request,'login.html')
    
    
def check(request):
    c_info={}
    mybd=conn.connect(host='localhost',user='root',passwd='1234',database='data_info')
    cur=mybd.cursor()
    cur.execute('select* from cust_info')
    res=cur.fetchall()
    username=request.GET.get('usr','no input')
    psd=request.GET.get('pswd','no input')
    for i in res:
        if i[0]==username and i[1]==psd:
            global email
            email=username
            global food_1,food_2,food_3,food_4,food_5,food_6,food_7,food_8,food_9,food_10,food_11,food_12,food_13,food_14,food_15,food_16,food_17,food_18,food_19,food_20
            food_1=food_2=food_3=food_4=food_5=food_6=food_7=food_8=food_9=food_10=food_11=food_12=food_13=food_14=food_15=food_16=food_17=food_18=food_19=food_20=[]
            c_info['name']=i[2]
            return render(request,'foods.html',c_info)
            break
            
            
    else:
        dic={'wusr':'Enter valid username & password'}
        return render(request,'login.html',dic)
        
def signup(request):
    return render(request,'signup.html')


def foods(request):
    
            
           
    return render(request , 'foods.html')

def sent_otp(request):
    try:
        reciver_email=request.GET.get('email','no input')
        mybd=conn.connect(host='localhost',user='root',passwd='1234',database='data_info')
        cur=mybd.cursor()
        cur.execute('select* from cust_info')
        res=cur.fetchall()
        count=0
        for i in res:
            if i[0]==reciver_email:
                count+=1
        if count == 0:
            name=request.GET.get('name','no input')
            phone=request.GET.get('phno','no input')
            addr=request.GET.get('address','no input')
            password=request.GET.get('password','no input')
            global rec_email , naam , mobile ,address,pwd 
            naam = name
            mobile = phone
            address = addr
            pwd = password 
            rec_email = reciver_email          
            senter_email='pymato212@gmail.com'
            password = 'abhiskehpriyanshu'
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(senter_email,password)
            otp = random.randint(1000,9999)
            global actual_otp
            actual_otp = otp 
            server.sendmail(senter_email,reciver_email,str(otp))
            return render(request,'otp.html')
        else:
            d={"err":"This account alredy exist.."}
            return render(request,'signup.html',d)
    except:
        dic={'msger':"Enter valid email....."}
        return render(request,'signup.html',dic)
    

def verify(request):
    entered_otp = request.GET.get('otp' , 'no input')
    global actual_otp #changed...........................................changed
    if entered_otp == str(actual_otp):
        mybd = conn.connect(host='localhost',user='root',passwd='1234',database='data_info')
        cur = mybd.cursor()
        val=(rec_email,pwd)
        sql='insert into login_info values(%s,%s)'
        cur.execute(sql,val)
        mybd.commit()
        mybd = conn.connect(host='localhost',user='root',passwd='1234',database='data_info')
        cur = mybd.cursor()
        val=(rec_email,pwd,naam,mobile,address)
        sql='insert into cust_info(email,password,name,phone,address) values(%s,%s,%s,%s,%s)'
        cur.execute(sql,val)
        mybd.commit()
        dc = conn.connect(host='localhost',user='root',passwd='1234',database='order_history')
        cur=dc.cursor()
        tab_name=rec_email.split('@')
        co = "CREATE TABLE "+tab_name[0]+" (food_id integer,food_name varchar(20) not null,rate decimal,quantity integer,date datetime);"
        cur.execute(co)
        d={"msger1":"Singin sucessfully......."}
        return render(request,'login.html',d)
    else:
        return render(request,'otp.html')                                                                                                                      


def cart(request):
    total=0
    dic={}
    data_lst2=[]
    global data_lst
    data_lst=[food_1,food_2,food_3,food_4,food_5,food_6,food_7,food_8,food_9,food_10,food_11,
                food_12,food_13,food_14,food_15,food_16,food_17,food_18,food_19,food_20]
    for food_info in  data_lst:
        if bool(food_info)==True and int(food_info[2])>0:
            data_lst2.append(food_info)
        else:
            pass
    global data_lst3
    data_lst3 = data_lst2
    dic['cart_lst'] =data_lst3
    for food_info in  dic['cart_lst']:
        if bool(food_info)==True and int(food_info[2])>0:
            total+=(int(food_info[2])*food_info[3])
        else:
            pass
    dic['total']=total
    return render(request, 'cart.html' , dic)

 
def profile(request):
    c_info={}
    mybd2=conn.connect(host='localhost',user='root',passwd='1234',database='data_info')
    cur2=mybd2.cursor()
    cur2.execute('select* from cust_info')
    custs=cur2.fetchall()
    for cust in custs:
        if cust[0]==email:
            c_info['email']=cust[0]
            c_info['name']=cust[2]
            c_info['phone']=cust[3]
            c_info['address']=cust[4]
    return render(request,'profile.html' , c_info)



def add1(request):
    quan = request.GET.get('quan','no input')
    global food_1
    food_1=[1,'Lemon Chicken',quan,120]
    return render(request , 'foods.html')

    

def add2(request):
    quan = request.GET.get('quan','no input')
    global food_2
    food_2=[2,'Chettinad Fish Fry',quan,150]
    
    
    
    
    
    return render(request , 'foods.html')


def add3(request):
    quan = request.GET.get('quan','no input')
    global food_3
    food_3=[3,'Dum Aloo Lakhnawi',quan,80]
    
    
    
    
    return render(request , 'foods.html')


def add4(request):
    quan = request.GET.get('quan','no input')
    global food_4
    food_4=[4,'Keema Biryani',quan,99]
    
            
            
    
    
    
    return render(request , 'foods.html')


def add5(request):
    quan = request.GET.get('quan','no input')
    global food_5
    food_5=[5,'Butter Chicken',quan,46]
    return render(request , 'foods.html')


def add6(request):
    quan = request.GET.get('quan','no input')
    global food_6
    food_6=[6,'Vegetable dalia',quan,120]
    return render(request , 'foods.html')


def add7(request):
    quan = request.GET.get('quan','no input')
    global food_7
    food_7=[7,'Upma',quan,150]
    return render(request , 'foods.html')


def add8(request):
    quan = request.GET.get('quan','no input')
    global food_8
    food_8=[8,'Thepla',quan,80]
    return render(request , 'foods.html')


def add9(request):
    quan = request.GET.get('quan','no input')
    global food_9
    food_9=[9,'Sprouts salad',quan,99]
    return render(request , 'foods.html')


def add10(request):
    quan = request.GET.get('quan','no input')
    global food_10
    food_10=[10,'Poha',quan,46]
    return render(request , 'foods.html')


def add11(request):
    quan = request.GET.get('quan','no input')
    global food_11
    food_11=[11,'Peas pulao',quan,150]
    return render(request , 'foods.html')


def add12(request):
    quan = request.GET.get('quan','no input')
    global food_12
    food_12=[12,'Carrot raita',quan,90]
    return render(request , 'foods.html')

def add13(request):
    quan = request.GET.get('quan','no input')
    global food_13
    food_13=[13,'Moong dal khichdi',quan,149]
    return render(request , 'foods.html')


def add14(request):
    quan = request.GET.get('quan','no input')
    global food_14
    food_14=[14,'Dal Fry',quan,88]
    return render(request , 'foods.html')


def add15(request):
    quan = request.GET.get('quan','no input')
    global food_15
    food_15=[15,'Lemon rice',quan,156]
    return render(request , 'foods.html')


def add16(request):
    quan = request.GET.get('quan','no input')
    global food_16
    food_16=[16,'Baked Ragi Chakli',quan,150]
    return render(request , 'foods.html')


def add17(request):
    quan = request.GET.get('quan','no input')
    global food_17
    food_17=[17,'Bedmi Puri With Raseele Aloo',quan,90]
    return render(request , 'foods.html')


def add18(request):
    quan = request.GET.get('quan','no input')
    global food_18
    food_18=[18,'Dahi Kebabs',quan,150]
    return render(request , 'foods.html')


def add19(request):
    quan = request.GET.get('quan','no input')
    global food_19
    food_19=[19,'Cashewnut And Cauliflower Pakoda',quan,88]
    return render(request , 'foods.html')


def add20(request):
    quan = request.GET.get('quan','no input')
    global food_20
    food_20=[20,'Paneer Shashlik',quan,156]
    return render(request , 'foods.html')


def order(request):
    if len(data_lst3) >= 1:
        for data in data_lst3:
            if bool(data)==True:
                dc = conn.connect(host='localhost',user='root',passwd='1234',database='order_history')
                cur=dc.cursor()
                tab_name=email.split('@')
                co = "INSERT INTO {} VALUES({},'{}',{},{},now());".format(tab_name[0],data[0],data[1],data[3],data[2])
                cur.execute(co)
                dc.commit()
            else:
                pass
        return HttpResponse("<script>alert('Order will be soon delivered to your address');</script>")
    elif len(data_lst3) == 0:
        return HttpResponse('<html><body><h1>Your haven t add anything to cart . Please go back to food page and add foods to cart then order</h1></body></html>')




def order_history(request):
    dc = conn.connect(host='localhost',user='root',passwd='1234',database='order_history')
    cur=dc.cursor()
    tab_name=email.split('@')
    co = "SELECT * FROM {};".format(tab_name[0])
    cur.execute(co)
    his = cur.fetchall()
    dic={'history_lst':his}
    return render(request,"history.html",dic)
    



def changing(request):
    return render(request,'address.html')

def address(request):
    newaddress = request.GET.get('nadr','no input')
    query = 'update cust_info set address ="'+newaddress+'" where email ="'+email+'";'
    dbco = conn.connect(host='localhost',user='root',passwd='1234',database='data_info')
    cur=dbco.cursor()
    cur.execute(query)
    dbco.commit()
    return HttpResponse('<html><body><h1>Address changed sucessfully</h1><br><a href="http://127.0.0.1:8000/"><button>Login page</button></a></body></html>')


    