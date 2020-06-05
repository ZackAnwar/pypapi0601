#!/usr/bin/python3

def main():
    vendordict = {'cisco': True, 'juniper': False, 'arista': True, 'netgear': True}
    custlist = ['acme', 'globex corporation', 'soylent green', 'initech', 'umbrella corporation']

    ## Display the current state of our dictionary
    print(vendordict)

    ## display all of the dictionary methods
    ## focus on the ones without underscores
    ## dict is a special word that Python treats as a dicttionary
    ## FYI -- dict would be a terrible variable name
    print(dir(dict))
    # ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', \
    # 'update', 'values']

    ## use a few dictionary methods
    print(vendordict.keys())
    print(vendordict.values())
    print(vendordict.get('juniper'))
    ## remove the key:value pair for netgear
    vendordict.pop('netgear')
    ## notice that 'netgear' no longer returns a value (the key:value pair is gone)
    print(vendordict.get('netgear'))

    ## display all of the list methods-- focus on the ones without underscores
    ## list is a special word that Python treats as a list
    ## FYI -- list would be a terrible variable name
    print(dir(list))
    # ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', \
    # 'reverse', 'sort']
    custlist.append('cyberdyne')

    ## cyberdyne should now be part of the list
    print(custlist)

if __name__ == "__main__":
    main()

