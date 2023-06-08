#!/usr/bin/python

import json, time
from eve_ng import eve_ng

def main():
    with open('environment.json') as e:
        environ = json.load(e)
        e.close()
   
    eve=eve_ng()
    eve.start_lab_nodes(environ['lab']['name'])

if __name__ == '__main__':
    main()