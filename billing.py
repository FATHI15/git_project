import sqlite3
def main():
	try:
		con= sqlite3.connect('test.db')
		cur= con.cursor()
		f=0
		t1=[]
		print "\t\t**************************CASH BILL*******************************"
		no_of_item=input("Enter the no of items :")
				
		for i in range(0,no_of_item):
			Id=raw_input("Enter the item id    :")
			#qu=raw_input("Enter the item quantity   : ")
			sql=("SELECT Item_id,Item_name,Item_price,Item_quantity,Item_tax,Perishable,Exp_date FROM stock_details where Item_id=?")
			cur.execute(sql,(Id))
			data=cur.fetchall()
			l=len(data)
			f=1
			
			print "Item_id\tItem_name\tItem_price\tItem_quantity\tItem_tax\tPerishable\tExp_date\t\tTotal"
			print "====================================================================================================================="
			for i in range(0,l):
				t=data[i][2]+data[i][4]
				t1.append(t)
				print data[i][0],'\t',data[i][1],'\t''\t',data[i][2],'\t''\t',data[i][3],'\t''\t',data[i][4],'\t''\t',data[i][5],'\t''\t',data[i][6],'\t''\t\t',t
				print "---------------------------------------------------------------------------------------------------------------------------"	
				print ('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tGrand total:'),sum(t1)






















	except sqlite3.Error,e:
		if con:
			con.rollback()
			print e
	finally:
		if con: 
			con.close()



if __name__ == "__main__":
	main()

