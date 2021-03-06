# cat copy.py
import os, multiprocessing
import time

def directoryData(dir, phone_number_dict):
    print("Searching in Images directory")
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            if '.' in name:
                extn = name.split('.')
                if extn[1].lower() == 'jpeg':
                    if '_' in name:
                        id = name.split('_')[0]
                    else:
                        id = extn[0]

                    if id in phone_number_dict:
                        r.append({
                                'file': name,
                                'id': id
                        })
    print("Images Found")
    return r


def copy(r):
    print("copy started")
    sort = []
    for i in r:
#        sort.append(i['id'])
        print(i['file'])
        os.system('rsync /BACKUP/ONBOARDING_DATA/CustomerImages/{} /ONBOARDING_DATA/PDF-JUNE-2019/'.format(i['file']))
    print("copy completed")
    return sort

def get_phone_numbers_dict(path):
    print("get phone number")
    r = []
    ids_dict = {}
    fileHandler = open (path, "r")
    while True:
        line = fileHandler.readline().strip()
        if not line:
            break;
        ids_dict[line] = ''
    fileHandler.close()
    print("Got phone number")
    return ids_dict

if __name__ == '__main__':
    path='/tmp/mayank_data.txt'
#   dir ='/opt/PDF/'
    phone_number_dict = get_phone_numbers_dict(path)
    path2 ='/BACKUP/ONBOARDING_DATA/CustomerImages/'

    dict_data = directoryData(path2, phone_number_dict)
    variab = copy(dict_data)
    print(variab)
