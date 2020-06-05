#!/usr/bin/python3

def main():
    vendordict = {'cisco': True, 'juniper': False, 'arista': True, 'netgear': True}
    custlist = ['acme', 'globex corporation', 'soylent green', 'initech', 'umbrella corporation']

    ## display all of the dictionary methods
    ## dict is a special word that Python treats as a dictionary
    ## FYI -- dict would be a terrible variable name
    print(dir(dict))
    # ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', \
    # 'update', 'values']

    ## display all of the list methods
    ## list is a special word that Python treats as a list
    ## FYI -- list would be a terrible variable name
    print(dir(list))
    # ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', \
    # 'reverse', 'sort']

    # Some of the code below this line works, and some does not.
    # Uncomment the code that works
    # ----------------------------------------------------------
    # custlist.keys()
    # vendordict.get('juniper')
    # custlist.get('umbrella corporation')
    # custlist.update('nsx')
    # vendordict.update({'cisco': False})
    # vendordict.sort()

if __name__ == "__main__":
    main()   

