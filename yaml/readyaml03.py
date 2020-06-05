#!/usr/bin/python3

# YAML is NOT part of the standard library
# python3 -m pip install pyyaml
import yaml

def main():
    ## Open a blob of YAML data
    with open("myYAML.yml", "r") as yf:
        ## convert YAML into Python data structures (lists and dictionaries)
        pyyammy = yaml.load(yf)
    # display our new Python data
    print(pyyammy)

if __name__ == "__main__":
    main()

