
from skpy import Skype
from getpass import getpass
from extractor import allgchistory, singlegchistory
import re

def main():
    sk = Skype(input("Enter Email add: "), getpass())
    sentinel = input("Press 1 to proceed, 0 to exit: ")
    
    if sk.conn.connected:
        gcid = sk.chats.recent()
        groupid(gcid)        
        
        while sentinel != '0':
            param = input("Enter GC ID, or Press Enter to Generate all GC History: ")            

            if param:                
                singlegchistory(sk, gcid, param)
                del gcid[param]
            elif not param:
                allgchistory(sk, gcid)
        # print(sk.conn)
            
            sentinel = input("Press 1 to continue, 0 to exit: ")

            groupid(gcid)


def groupid(gcid):
    for x in gcid:
            if re.findall("19", x):
                print("Group Name: ", gcid[x].topic,"Group ID: ", x)
    print("\n")

main()