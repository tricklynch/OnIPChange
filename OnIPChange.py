import os
import subprocess

def GetIP():
    TODO 
    #touch oldip.txt currentip.txt
    #rm oldip.txt
    #mv currentip.txt oldip.txt
    #curl ifconfig.me > currentip.txt

def DidItChange():
    TODO
    #open oldip.txt
    #open currentip.txt
    #compare the 2 files
    #return true if there was change
    #false otherwise

def Notify():
    TODO
    #touch config.txt
    #open config.txt to get the email address and phone number
    #open currentip.txt
    #send an email
    #curl -X POST http://textbelt.com/text -d number=phonenumber -d "message=Your IP address has changed to newip"

def main():
    GetIP()
    if(DidItChange()):
        Notify()

if __name__ == "__main__":
    main()