#!/usr/bin/env python

import os, shlex, subprocess, pexpect, sys, re, socket

__PWD__ = 'canesys?'

def buildTunnel(host,ip,port,lport):
    print('ssh -C -Nfg -L%s:%s:%s canerec@%s' % (lport,ip,port,host))
    child = pexpect.spawn('ssh -C -Nfg -L%s:%s:%s canerec@%s' % (lport,ip,port,host))
    child.expect('password:')
    child.sendline(__PWD__)
    child.expect(pexpect.EOF, timeout=10)
    print('Please click the following link to open the device:\n')
    print('http://'+os.uname()[1]+":"+str(lport))

def readConfig(plantCode):
    from xml.etree import ElementTree
    
    isFoundConfig = 0
    
    with open('clientsDevices.xml', 'rt') as f:
        tree = ElementTree.parse(f)

    for site in tree.getiterator('site'):
        if site.attrib.get('code') == plantCode:
            isFoundConfig = 1
            aList=[]
            print("Devices at " + site.attrib.get('name') + "\n")
            counter = 1
            host = site.attrib.get('host')
            for device in site.getchildren():
                dhost = device.attrib.get('dhost')
                desc = device.attrib.get('desc')
                ip = device.attrib.get('ip')
                port = device.attrib.get('port')
                aDict = {'dhost':dhost,'ip':ip,'port':port,'host':host}
                aList.append(aDict)
                print("\t("+str(counter)+"). Desc:"+desc+" IP:["+ip+"]")
                counter=counter+1
            print("\t(E). Exit")
    if isFoundConfig == 1:
        return aList
    else:
        print("No config found for plant code: "+plantCode)
        exit()
       
def findAPort():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
    port = 8880
    while port < 9000:
        try:
            serversocket.bind(('localhost', port))
            # You may want: serversocket.bind((socket.gethostname(), port))
        except socket.error as e:
            if e.errno==98:
                port = port+1
            else:
                raise
        else:
            break
    serversocket.close()
    print "Found port", port  
    return port

if __name__ == '__main__':
    if len(sys.argv) == 2 :
        if re.match("^[a-z]{3}$", sys.argv[1]):
            aList = readConfig(sys.argv[1])
            print('Please choose a number from above:')
            inp = sys.stdin.readline()
            if re.match("^[0-9]$", inp):
                aDict = aList[int(inp)-1]
            else:
                print("exiting...")
                exit()
            (host,port,ip) = (aDict['host'],aDict['port'],aDict['ip'])
            lport = findAPort()
            buildTunnel(host,ip,port,lport)
        else:
            print("Invalid plant code, exiting...")
            exit()
    else:
        print("Invalid input, exiting...")
        exit()
