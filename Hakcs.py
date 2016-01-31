import subprocess
import re
from test.warning_tests import outer
import os
import sys
import time
while True:
    com = 'ipconfig'
    
    p = subprocess.Popen([com], stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
    
    out, error = p.communicate()
    ip =  re.findall( r'[0-9]+(?:\.[0-9]+){3}', (re.search('\s+Default Gateway.*: ([\d\.]+)', out)).group(0))[0]
    ip =  re.findall( r'[0-9]+(?:\.[0-9]+){3}', (re.search('\s+IPv4 Address.*: ([\d\.]+)', out)).group(0))[0]
    subnet = re.findall( r'[0-9]+(?:\.[0-9]+){3}', (re.search('\s+Subnet Mask.*: ([\d\.]+)', out)).group(0))[0]
    p.terminate()
    
    low = ''
    high = ''
    y =0
    for x in subnet.split('.'):
        
        
        
        w = int (ip.split('.')[y])
        q = int (subnet.split('.')[y])
        u = w & q
        
        low = low  +str(u) 
        t = ((int)(low.split('.')[y]))|(255-q)
        high = high + str(t)
        if y < 3:
            low = low + '.'
            high = high + '.'
            
        y+=1
    
    
    
    bin_ip = '.'.join([bin(int(x)+256)[3:] for x in ip.split('.')])
    bin_subnet = '.'.join([bin(int(x)+256)[3:] for x in subnet.split('.')])
    current_ip = low.split('.')[0] + '.'+low.split('.')[1]+ '.'
    file = open('NMAP.txt', 'w+')
    file1 = open('NMAP1.txt', 'a')
    if  ((int)(high.split('.')[3]) - (int)(low.split('.')[3])) == 255:     
        file1.write(time.strftime("%Y-%m-%d %H:%M")+"\n")
        for x in range((int)(low.split('.')[2]), (int)(high.split('.')[2])+1):
            sys.stdout = file
            print os.popen('C:/Nmap/nmap.exe -sn '+ current_ip+(str)(x) +'.1/24').read()
        file.close()
    
    
    stream = open('NMAP.txt', 'r')   
    macs= []
    for brandon in stream:
        if "MAC" in brandon:
            macs.append(brandon[13:len(brandon)-1])
    file1.write((str)(len(macs))+'\n')
    file1.close()




    