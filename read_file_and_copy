#!/usr/bin/env python2
import os, multiprocessing
import time
def fileData(path):
    r = []
    fileHandler = open (path, "r")
    while True:
        line = fileHandler.readline().strip()
        if not line:
            break;
        #print('find /home/ -name "*'+line+'*.jpeg" -type f  -exec rsync -aPr {} /tmp/ \;')
        os.system('find /home/ -name "*'+line+'*.jpeg" -type f  -exec rsync -aPr {} /tmp/ \;')
    fileHandler.close()
    return r


#def copy(r):
#    sort = []
#    for i in r:
#        print(i['file'])
#        os.system('rsync /opt/PDF/{} /tmp/'.format(i['file']))
#    return sort

if __name__ == '__main__':
     path='/tmp/may_data.txt'
#     dir ='/opt/PDF/'
     list1 = fileData(path)
     print(list1)
