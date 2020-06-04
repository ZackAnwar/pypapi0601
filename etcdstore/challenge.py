#!/usr/bin/python3
"""Russell Zachary Feeser Using etcd to design a RESTful ticket server"""

import requests

ETCD = "http://127.0.0.1:2379/v2/keys/poems"

## Read all poems## Read all poemsdef getpoems():

def getpoems():
    resp = requests.get(ETCD)
    resp = resp.json()
    # if the resp dict contains an errorCode
    if resp.get("errorCode"):
        return False
    # if no errorCode assume there are poems in system
    else:
        poemlist = []
        ## if someone manually deletes all entries from the directory /poemss/
        ## then it will still test true (no errorCode), but won't have entry for "nodes"
        if resp.get("node").get("nodes"):
        ## after studying resp dict, resp["node"]["nodes"] appears to be a list
        ## of ticket entries. We cycle through this
            for poems in resp.get("node").get("nodes"):
                ## add a poem name to poemlist
                poemlist.append(poem.get("key").lstrip("/poems/"))
            return poemlist
        else:
            return False

## get a specific ticket
## pass in the ticket to GET
def getpoemname(poemname):
    resp = requests.get(f"{ETCD}/{poemname}")
    resp = resp.json()
    ## if a key called errorCode is returned in the JSON
    if resp.get("errorCode"):
        # return false
        return False
    else:
        # return the VALUE assocaited with they KEY called 'value'
        return resp.get("node").get("value")


## create a ticket
## use a POST to create a new resource
def createpoem(descofpoem):
   ## sending a POST to the base URL will create a new /tickets/{ID}
   resp = requests.post(ETCD, data={'value': descofpoem })
   resp = resp.json()
   ## take resp["node"]["key"].lstrip("/tickets/") which is the ticketID
   resp = resp.get("node").get("key").lstrip("/poems/")
   return resp

def main():

    ## Enter a while true loop (run until a break condition)
    while True:

        ## pop up a menu
        print("""
        1) Read all available Poem names
        2) Get Poem name
        3) Create Poem Name
        4) Update Poem Name
        5) Delete Poem Name
        6) Exit
        99) DANGER! Delete all Poem Names
        """)

        ## collect input from user
        userinput = ""
        while userinput == "":
            userinput = input("> ")

        ## user wants ALL available poem names
        if userinput == "1":
            ## getpoems() returns a list or FALSE
            poemlist = getpoems()
            ## Test what was poemlist?
            if poemlist:
                print()
                for poems in poemlist:
                    print(f"Poem Name - {poems}")
            else:  ## if poemlist() returned FALSE
                print("There are no Poem names entered")
            
        ## user wants info on a single ticket
        elif userinput == "2":
            poemid = input("What is the poem name? ")
            onename = (getpoemname)
            em
            # if oneticket returns a string or FALSE
            if onename:
                print(f"\nFor {poemname}:")
                print(f"    Poem Description - {onename}")
            ## handles condition where FALSE is returned
            else: 
                print("That Poem name does not exist within the system.")

        ## user wants to create a poem namet
        elif userinput == "3":
            descofpoem = input("Give a short 140 char description of the issue: ")
            createdpoem = createpoem(descofpoem)
            print(f"\nPoem {createdpoem} has been created.")

        ## user wants to update a poem name
        elif userinput == "4":
            poemname = input("Update what oem Name? ")
            descofpoem = input("What is the updated 140 char description of the Name: ")
            ## updated name returns a two-tuple, or FALSE
            updatedname = updatename(poemname, descofpoem)
            if updatedpoem:
                print(f"\nFor {poemname}:")
                print(f"    Updated Poem  Description - {updatedpoem[0]}")
                print(f"    Old Poem Description - {updatedpoem[1]}")
            else: ## if updatedpoem() returned FALSE
                print("That Poemticket does not exist within the system.")

        ## user wants to delete a Poem Namet
        elif userinput == "5":
            poemname = input("What is the Poem Name? ")
            deletepoem(poemname)
            print(f"\nPoem {poemname} has been removed from the system")

        ## user wants to exit
        elif userinput == "6":
            ## end the while True loop
            break

        elif userinput == "99":
            deleteallpoems()
            print("All Poem  have been removed from the system")

        ## user inputs a non valid option
        else:
            print("That is not a valid option")

    print("Thanks for using the Alta3 RESTful Poem Name systeme")

if __name__ == "__main__":
    main()
