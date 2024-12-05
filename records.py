import mysql.connector

db=mysql.connector.connect(host='localhost',user='root',passwd='g00d_Uare',database='busmanagementsystem')


cr=db.cursor()


l=[('MH45QW7889','Robert','Lucknow','Delhi',900,1300,40,20,'$10','AC_type','quincy100','yipppee'),('MH32QW7889','Rico','Lucknow','Delhi',1300,1800,35,15,'$5','NON_AC','laurence','peace'),('PR45QW7889','Lensord','Lucknow','Delhi',900,1300,40,20,'$15','AC_type','weasel','winita'),('RJ56QW7889','Claud','Lucknow','Kolkata',600,1700,30,20,'$20','AC_type','Enchos','yipppee'),('RJ65QM7689','Edith','Lucknow','Kolkata',900,1900,35,10,'$19','NON_AC','@Eddy','seemore'),('FR45QW0889','Ronald','Sri Nagar','Kanyakumari',100,2400,40,7,'$35','NON_AC','Tom','yipppee'),('MX15QE7049','Robert','Chandigarh','Delhi',900,1100,30,20,'$30','NON_AC','Larry','inhurry'),('FG89JS4558','Lou','Secundrabad','Nagpur',900,1900,40,20,'$30','NON_AC','Mike','yipppee'),('VR45RW7876','Ernst','Indore','Dehradun',500,1900,30,10,'$15','NON_AC','Collete','yipp'),('UP47EW9001','Jannet','Mumbai','Gangtok',700,2200,30,25,'$15','NON_AC','Jarrod','wekill'),('MS45QW7889','Frank','Gurgaon','Mumbai',1300,2300,30,10,'$25','AC_type','Anitti','rebel'),('MH45QS5677','Enrico','Gurgaon','Mumbai',900,2000,30,10,'$20','NON_AC','Shelly','hello'),('MS34TY7099','Ripper','Goa','Indore',1300,1800,50,20,'$20','AC_type','Jason','yellito'),('KY67MS7779','Bonnie','Goa','Indore',700,1200,35,14,'$!5','NON_AC','Rosa','gitgud'),('UP432OP6798','Belle','Delhi','Daman',1300,2000,30,10,'$20','AC_type','Ezabelle','yup')]


for i in l:
    cr.execute('insert into busses values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]))
    db.commit()
    print('inserted:',i)

l1=[('Rosa@2001','56:-)','myemail@gmail.com'),('Bella123','i_am---','email14@gmail.com'),('I_am_a_bolt',':-):=()','yours890@hotmail.com'),('Stephan001','456:-)','rtx@gmail.com'),('Teestan','1234567','ail@hotmail.com'),('Rozorty','my_hope','bookme@gmail.com'),('demolisher','mercy','loveme32@gmail.com'),('botttt','hello','itsme@gmail.com'),('Rosa',':-)','myemail@gmail.com'),('noone--','456','gutgud@hotmail.com'),('claud_01','56:-)','Claudisbest@gmailmail.com')]
for i in l1:
    cr.execute('insert into user values(%s,%s,%s)',(i[0],i[1],i[2]))
    db.commit()
    print('inserted:',i)
