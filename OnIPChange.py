import os

def GetIP():
  os.system("touch oldip.txt currentip.txt")
  os.system("rm oldip.txt")
  os.system("mv currentip.txt oldip.txt")
  os.system("curl ifconfig.me > currentip.txt")

def DidItChange():
  old = open("oldip.txt", "r")
  current = open("currentip.txt", "r")
  oldip = old.readline()
  currentip = current.readline()
  old.close()
  current.close()
  return oldip != currentip

def Notify():
  os.system("touch config.txt")
  config = open("config.txt")
  new = open("currentip.txt")
  phonenumber = config.read(10).strip('\n')
  emailaddr = config.read().strip('\n')
  newip = new.read().strip('\n')
  #send an email
  sms = 'curl -X POST http://textbelt.com/text -d number=%s -d "message=Your IP address has changed to %s"' % (phonenumber, newip)
  os.system(sms)
  config.close()

def main():
  GetIP()
  if(DidItChange()):
    Notify()

if __name__ == "__main__":
  main()
