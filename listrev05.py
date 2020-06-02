#!/usr/bin/python3
 
def main():
     ## a list of Alta3 classes
     alta3classes = ['python_basics', 'python_api_design', 'python_for_networking', 'kubernetes', \
       'sip', 'ims', '5g', '4g', 'avaya', 'ansible', 'python_and_ansible_for_network_automation']
       
     ## display the list
     print(alta3classes)
 
     ## how long is the list? use the built in len function
     ## THEN print (display) the results
     print(len(alta3classes))
 
     # display python_basics
     print(alta3classes[0])
 
     # display SIP
     print(alta3classes[4])
 
     # display Ansible
     print(alta3classes[9])
 
     ##Uncomment to see a list index out of range error
     #print(alta3classes[99])
 
     print(alta3classes[0:3])
 
     print(alta3classes[2:5])
 
     print(alta3classes[-1])
 
if __name__ == "__main__":
     main()
