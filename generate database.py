import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',passwd='g00d_Uare')

crs=db.cursor()

crs.execute('create database busmanagementsystem')
db.commit()


crs.execute('use busmanagementsystem')

crs.execute('create table busses (issueno varchar(15) primary key , drivername varchar(15) not null, pickup varchar(15) not null, dropl varchar(15) not null, pickti int(11) not null, dropti int(11) not null, totalseats int(11) not null,seatsleft int(11) not null, fare varchar(10) not null, type varchar(10) not null,conductorid varchar(30) unique,conpass varchar(10) not null)')
db.commit()


crs.execute('create table user (userid varchar(30) primary key , password varchar(10) not null, emailid varchar(30) not null)')
db.commit()



crs.execute('create table bookings (userid varchar(30) not null, issueno varchar(15) not null , pickupl varchar(15) not null, dropl varchar(15) not null, pickti int(11) not null, dropti int(11) not null, fare varchar(10) not null, type varchar(10) not null, day varchar(10) not null, driver varchar(20) not null)')

db.commit() 
print('task completed')
