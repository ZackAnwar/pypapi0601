#!/usr/bin/python3
 
def main():
     ## create a list already containing IP addresses (strings)
     iplist = ['10.0.0.1', '10.0.1.1', '10.3.2.1']
 
     ## create a list of ports (strings)
     iplist2 = ['5060', '80', '22']
 
     ## display list
     print(iplist)
 
     ## Use the append method on iplist, our list object
     ## append takes whatever it is passed and adds it to the list object (iplist)
     ## this will create a list within a list
     iplist.append(iplist2)
 
     ## show how iplist has changed
     print(iplist)
 
     ## just like extend, append expects exactly one item to be passed.
     ## If you'd like, uncomment the code below and see the error caused
     # iplist.append('aa:bb:cc:dd:ee:ff', '00:11:22:33:44:55')
 
if __name__ == "__main__":
     main() 
