import sqlite3


def main():
	try:
		con= sqlite3.connect('test.db')
		cur= con.cursor()
                choice=input(" 1:Add customer \n 2:add item \n 3:delete \n 4:modify item details item \n 5:view database contents \n Enter the choice")
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
		elif choice==4:
			toadd=input("Enter no:of items to update/moify")
			for i in range(0,toadd):
				h="SELECT * FROM stock_details"
	        		cur.execute(h)
				data=cur.fetchall()
				l=len(data)
                		print "Item_id\tItem_name\tItem_price\tItem_quantity\tItem_tax\tPerishable\tExp_date"
				print "==================================================================================================="
				for i in range(0,l):
             				print data[i][0],'\t',data[i][1],'\t''\t',data[i][2],'\t''\t',data[i][3],'\t''\t',data[i][4],'\t''\t',data[i][5],'\t''\t',data[i][6]
					print "---------------------------------------------------------------------------------------------"
				Id=raw_input("Enter the id of item")
				ch=input("\n 1:modify price \n 2:modify tax \n 3:modify quantity \n Enter a choice (eg: 1,2..)  ")
				if ch == 1:
					price=input("Enter the value to be updated")
					sql=("update stock_details set Item_price=? where Item_id=?")
					cur.execute(sql,(price,Id))
					con.commit()
					print "price updated to",price
				if ch == 2:
					tax=input("Enter the tax to be updated  for the commodity ")
					sql=("update stock_details set Item_tax=? where Item_id=?")	
					cur.execute(sql,(tax,Id))
					con.commit()
					print "tax updated to",tax	
				if ch ==3:
					quantity=input("Enter the quantity to be updated the commodity ")
					sql=("update stock_details set Item_quantity=? where Item_id=?")	
					cur.execute(sql,(quantity,Id))
					con.commit()
					print "quantity updated to",quantity
				else:
					print "ERROR!!! Enter a valid choice"
			
		elif choice==5:
			print "1:customer database\n2:stock database"
			c=input("Enter the choice")
			if c == 1:
				n="SELECT * FROM customer"
	        		cur.execute(n)
				data=cur.fetchall()
				l=len(data)
                		print "customer_id\tcustomer_name\t\tcustomer_phone\t\tcustomer_bill no"
				print "==================================================================================================="
				for i in range(0,l):
             				print data[i][0],'\t''\t',data[i][1],'    \t ''  \t',data[i][2],'  \t''  \t',data[i][3]
					print "---------------------------------------------------------------------------------------------"
			elif c == 2:
				h="SELECT * FROM stock_details"
	        		cur.execute(h)
				data=cur.fetchall()
				l=len(data)
                		print "Item_id\tItem_name\tItem_price\tItem_quantity\tItem_tax\tPerishable\tExp_date"
				print "==================================================================================================="
				for i in range(0,l):
             				print data[i][0],'\t',data[i][1],'\t''\t',data[i][2],'\t''\t',data[i][3],'\t''\t',data[i][4],'\t''\t',data[i][5],'\t''\t',data[i][6]
					print "---------------------------------------------------------------------------------------------"
			else:
				print "ERROR!!!!! Invalid choice"
		
	except sqlite3.Error,e:
		if con:
			con.rollback()
			print e
	finally:
		if con: 
			con.close()



if __name__ == "__main__":
	main()



