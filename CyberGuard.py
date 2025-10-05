import nmap
import requests
import json
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2

def avail_host (ip):

    nm=nmap.PortScanner()
    print("Searching For Live Host.......")
    nm.scan(hosts=ip, arguments='-sn')
    live_host=[]
    for host in nm.all_hosts():
        if nm[host].state() == "up" :
            live_host.append(host)

    if not live_host:
       print("No Live Host Found")
    else:
      print("Live Host Found:")        
      for live in live_host:
         print(live)

def port_scanning (ip):
    nm=nmap.PortScanner()
    print("Searching For Ports.......")
    nm.scan(ip,'1-1024')

    for host in nm.all_hosts():
        print(f"Host : {host}")
        print(f"State : {nm[host].state()}")
        if nm[host].all_protocols():
         for proto in nm[host].all_protocols():
             print(f"Protocol : {proto}  {nm[host][proto].keys()}")
        else :
            print("Port Details Not Available")  

def os_scanning(ip):
    nm=nmap.PortScanner()
    print("Detecting OS Info......")
    nm.scan(hosts=ip, arguments='-O --osscan-guess')

    for host in nm.all_hosts():
        print(f"Host : {host}")
        print(f"State : {nm[host].state()}")

        if 'osmatch' in nm[host]:
            if nm[host]['osmatch']:
              for os in nm[host]['osmatch']: 
                 print(f"OS Name : {os['name']}")
                 print(f"Accuracy : {os['accuracy']}%")    
                 print(f"OS Type: {os.get('osclass', [{}])[0].get('type', 'Unknown')}\n") 

            else :
                print("OS Details Not Found")     

        else :
            print("OS Detection Not Available")   

            print("Trace Not Available") 


def encrypt_text(plain_text):

    password=input("Enter Your Password : ")

    salt =get_random_bytes(16)

    key=PBKDF2(password,salt,dkLen=32,count=100000)

    iv=get_random_bytes(16)

    cypher=AES.new(key,AES.MODE_CBC,iv)
    
    padded_text=pad(plain_text.encode(),AES.block_size)

    encrypt_text=cypher.encrypt(padded_text)

    with open("Encrypted DATA.bin","wb") as f:
       f.write(salt + iv + key + encrypt_text)

    print(f"Encrypted Data is Saved as 'Encrypted Data.bin' In The Directory")    



def decrypt_text(file_name): 
    with open(file_name,"rb") as f:
        f_data=f.read()
    
    salt =f_data[:16]
    iv= f_data[16:32]
    okey =f_data[32:64]
    cyphertext= f_data[64:]
    password=input("Enter the Password : ") 
    key=PBKDF2(password,salt,dkLen=32,count=100000) 
    
    if(key==okey):
        cypher=AES.new(key,AES.MODE_CBC,iv)
        decrypted_text=cypher.decrypt(cyphertext)
        plain_text=unpad(decrypted_text,AES.block_size)
        print(f"Decrypted Text : {plain_text}\n") 
    else:
        print("Invalid Password")  



while True:     
    inp=input("Choose The Service : \n1: IP Details\n2: Encryption And Decryption \n")
    if inp == '1':
        while True:
            inp2=input("\n1: Port Details\n2: Host Status\n3: OS Details")
            ip=input("Enter The IP :\n")
            if inp2=='1':
             port_scanning (ip)
             break
            elif inp2 =='2' : 
             avail_host (ip)
             break
            elif inp2 =='3' : 
             os_scanning(ip) 
             break
            else:
             print("Invalid Input\n")   
     
        break        
    elif inp == '2':
        while True:
            inp2=input("1: Encryption\nOR\n2: Decryption\n")
            if inp2=='1':
               plain_text=input("Enter The  Text :\n") 
               encrypt_text(plain_text)
               break
            elif inp2=='2': 
              file_name=input("Enter File Name :\n")
              decrypt_text(file_name)
              break
            else:
                print("Invalid Input\n")  
     
        break 
                   
    else:
        print("Invalid Input\n Please Try Again")
                    
