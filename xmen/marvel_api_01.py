#!/usr/bin/python3
import argparse
import time
import hashlib

import requests

## Define the API here
XAVIER = 'http://gateway.marvel.com/v1/public/characters'

## Calculate a hash to pass through to our MARVEL API call
## Marvel API wants md5 calc md5(ts+privateKey+publicKey)
def hashbuilder(timeywimey, pvkee, pubkee):
    return hashlib.md5((timeywimey+pvkee+pubkee).encode('utf-8')).hexdigest()

## Perform a call to MARVEL Character API
## http://gateway.marvel.com/v1/public/characters
## ?name=Spider-Man&ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150
def marvelcharcall(stampystamp, hashyhash, pkeyz, lookmeup):
    r = requests.get(XAVIER+"?name="+lookmeup+"&ts="+stampystamp+"&apikey="+pkeyz+"&hash="+hashyhash)

    print(XAVIER+"?name="+lookmeup+"&ts="+stampystamp+"&apikey="+pkeyz+"&hash="+hashyhash)
    return r.json()

    
def main():
    
    ## harvest private key
    with open(args.dev) as mccoy:
        beast = mccoy.read().rstrip('\n')
    
    ## harvest public key
    with open(args.pub) as munroe:
        storm = munroe.read().rstrip('\n')
    
    ## create an integer from a float timestamp (for our RAND)
    nightcrawler = str(time.time()).rstrip('.')
    
    ## build hash with hashbuilder(timestamp, privatekey, publickey)
    cerebro = hashbuilder(nightcrawler, beast, storm)

    ## call the API with marvelcharcall(timestamp, hash, publickey, character)
    uncannyxmen = marvelcharcall(nightcrawler, cerebro, storm, "Wolverine")
    
    ## display results
    print(uncannyxmen)

## Define arguments to collect
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev', \
      help='Provide the /path/to/file.priv containing Marvel private developer key')
    parser.add_argument('--pub', \
      help='Provide the /path/to/file.pub containing Marvel public developer key')
    args = parser.parse_args()
    main()
