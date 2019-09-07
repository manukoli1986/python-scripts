import time
import subprocess
import select

f = subprocess.Popen(['tail','-F','message.txt'],\
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
p = select.poll()
p.register(f.stdout)



while True:
    if p.poll(1):
        print f.stdout.readline()
#    time.sleep(1)
