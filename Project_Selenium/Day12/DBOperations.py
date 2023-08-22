# insert ,update,delete

insert_query="insert into student value(101,'kim')"
update_query="update student set sname='Mary' where sid=101"
delete_query="delete from student where sid=101"

import mysql.connector

con =  mysql.connector.connect(host="localhost",port=3306,user="root",passwd="password",database="mydb")
curs=con.cursor()
curs.execute(insert_query)
con.commit()
con.close()

print("Finished")