#!/usr/bin/env python2


import os
import time

def directoryData(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            if '.' in name:
                extn = name.split('.')
                if extn[1] in ['Jpeg', 'jpeg']:
                    if '_' in name:
                        id = name.split('_')
                        r.append({
                            'file': name,
                            'id': id[0]
                        })
                    else:
                        r.append({
                            'file': name,
                            'id': extn[0]
                        })
    return r


def copy(r):
    sort = []
    for i in r:
#        sort.append(i['id'])
        print(i['file'])
        os.system('rsync /home/{} /tmp/'.format(i['file']))
    return sort

if __name__ == '__main__':
    path='/home/'
#    path='/home/PDF/'
    dict_data = directoryData(path)
#    print(dict_data)
    variab = copy(dict_data)
    print(variab)
