

import nmap
import optparse


def nmapscan(tgthost,tgtport):
    nmscan=nmap.PortScanner()
    nmscan.scan(tgthost,tgtport)
    state=nmscan[tgthost]['tcp'][int(tgtport)]['state']
    print"**"+tgthost+"tcp:"+tgtport+""+state

def main():


    li=raw_input('ratgethost:')
    yue=raw_input('targetport:')
    tgthost=li
    tgtports=str(yue).split(',')
    if(tgthost==None)|(tgtports[0]==None):
        print 'fuck'
        exit(0)
    for tgtport in tgtports:
        nmapscan(tgthost,tgtport)
if __name__=='__main__':
    main()


