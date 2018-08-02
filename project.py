import sqlite3


def main():
	try:
		con= sqlite3.connect('test.db')
		cur= con.cursor()
                choice=input("1:Add customer 2:add item 3:delete 4:modify item details item 5:view database contents`")
		if choice==1:
                	toadd=input("Enter the no:of customers  to add")
                	for i in range(0,toadd):
				Id=raw_input("Enter the cus id:  ")
				Name=raw_input("Enter the name:  ")
				Phno=input("enter the phone no:  ")
				Bno=raw_input("Enter the billno: ")
				sql=("INSERT INTO customer (Id,Name,Phno,Bno) VALUES(?,?,?,?)")
				cur.execute(sql,(Id,Name,Phno,Bno))
				con.commit()
                		h="SELECT * FROM CUSTOMER"
				cur.execute(h)
				data=cur.fetchall()
				l=len(data)
                                print "customer id\t customername\t customer phno:\tcustomer billno"
			for i in range(0,l):
                		print "\t ",data[i][0],"\t  ",data[i][1],"\t  ",data[i][2],"      \t",data[i][3]
		elif choice==2:
			toadd=input("Enter the no:of items  to add")
                	for i in range(0,toadd):	
				Item_id=raw_input("Enter the item id (eg:1,2...) : ")
				Item_name=raw_input("Enter the item name: ")
				Item_price=raw_input("Enter the item price:  ")
				Item_quantity=input("enter the quantity:  ")
				Item_tax=raw_input("Enter the tax: ")
				Perishable=raw_input("Enter 0 for perishable and 1 for non-perishable: ")
				Exp_date=raw_input("Enter the expiry date for perishable items otherwise... put 0/0/0 as expiry date")
				sql=("INSERT INTO stock_details (Item_id,Item_name,Item_price,Item_quantity,Item_tax,Perishable,Exp_date) VALUES(?,?,?,?,?,?,?)")
				cur.execute(sql,(Item_id,Item_name,Item_price,Item_quantity,Item_tax,Perishable,Exp_date))
				con.commit()
                		h="SELECT * FROM stock_details"
				cur.execute(h)
				data=cur.fetchall()
				l=len(data)
                        	print "Item_id\tItem_name\tItem_price\tItem_quantity\tItem_tax\tPerishable\tExp_date"
				print "==================================================================================================="
				for i in range(0,l):
                			print data[i][0],'\t',data[i][1],'\t''\t',data[i][2],'\t''\t',data[i][3],'\t''\t',data[i][4],'\t''\t',data[i][5],'\t''\t',data[i][6]
					print "---------------------------------------------------------------------------------------------"
		elif choice==3:
			f=0
			toadd=input("Enter the no:of items to delete")
                        h="SELECT * FROM stock_details"
	        	cur.execute(h)
			data=cur.fetchall()
			l=len(data)
                	print "Item_id\tItem_name\tItem_price\tItem_quantity\tItem_tax\tPerishable\tExp_date"
			print "==================================================================================================="
			for i in range(0,l):
             			print data[i][0],'\t',data[i][1],'\t''\t',data[i][2],'\t''\t',data[i][3],'\t''\t',data[i][4],'\t''\t',data[i][5],'\t''\t',data[i][6]
				print "---------------------------------------------------------------------------------------------"
			for i in range(0,toadd):
				Id=raw_input("Enter the item id")
				print Id
				sql=("DELETE FROM stock_details where Item_id=?")
				f=1
				cur.execute(sql,(Id))
				con.commit()
				print Id,"deleted"
				#print "ERROR!!!item not found cannot delete...\n"
		elif choice==5:
			h="SELECT * FROM stock_details"
	        	cur.execute(h)
			data=cur.fetchall()
			l=len(data)
                	print "Item_id\tItem_name\tItem_price\tItem_quantity\tItem_tax\tPerishable\tExp_date"
			print "==================================================================================================="
			for i in range(0,l):
             			print data[i][0],'\t',data[i][1],'\t''\t',data[i][2],'\t''\t',data[i][3],'\t''\t',data[i][4],'\t''\t',data[i][5],'\t''\t',data[i][6]
				print "---------------------------------------------------------------------------------------------"
		
	except sqlite3.Error,e:
		if con:
			con.rollback()
			print e
	finally:
		if con: 
			con.close()



if __name__ == "__main__":
	main()



