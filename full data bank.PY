import mysql.connector
import xlrd

#import xls file using xlrd

book = xlrd.open_workbook("datanew.xls")
sheet = book.sheet_by_name("datenbank")

#establishing connection between mysql database with credentials
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database= "toki"
)

#create the cursor which will traverse db line by line
mycursor = db.cursor()

#creating a table
st = "CREATE TABLE newcalc1 ("
for i in range(0,29):
    st= st+ "I" + str(i) + " VARCHAR(200) , " 
st = st[:-3]
st = st+")"

mycursor.execute(st)

#importing values in row and column
for i in range(1, sheet.nrows):
    val = "Insert into newcalc1 values ("
    for j in range(0, 29):
        if j < sheet.ncols:
            val = val + "'"+ str(sheet.cell_value(i, j))+"', "
        else:
             val = val + "'', "
    val = val[:-2] + ");"
    mycursor.execute(val)

mycursor.close()
db.commit()
db.close()

