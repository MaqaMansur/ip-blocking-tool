import subprocess
import nmap, socket


print("""\n1 - Block IP for incoming traffic
2 - Block IP for outgoing traffic
3 - Allow IP for incoming traffic
4 - Allow IP for outgoing traffic\n
""")

choice = str(input('Choose one from the list above (1),(2),(3),(4) : '))

if __name__ == '__main__':
    
    subprocess.run(["service","iptables","start"])

    IP = str(input('Enter the IP : '))
    scanner = nmap.PortScanner()
    host = socket.gethostbyname(IP)
    scanner.scan(host,'1','-v')

    if choice == "3":
        subprocess.run(["iptables","-D","INPUT","-s",IP+'/32',"-j","DROP"])
        #subprocess.run(["service", "iptables", "save"])
        print("\nThe IP allowed successfully for incoming traffic !")
    
    elif choice == "4":
        subprocess.run(["iptables","-D","OUTPUT","-d",IP,"-j","DROP"])
        #subprocess.run(["service", "iptables", "save"])
        print("\nThe IP allowed successfully for outgoing traffic !")

    elif scanner[host].state() == "up":

        if choice == "1":
            subprocess.run(["iptables","-I","INPUT","-s",IP,"-j","DROP"])
            """
            if subprocess.run(block_ip_in_command).returncode != 0:
                print("An error occured : '", subprocess.run(block_ip_in_command).stderr,".'")
            """
            #else:
            #subprocess.run(["service", "iptables", "save"])
            print("\nThe IP blocked successfully for incoming traffic !")

        elif choice == "2":
            subprocess.run(["iptables","-I","OUTPUT","-d",IP,"-j","DROP"])
            """
            if subprocess.run(block_ip_in_command).returncode != 0:
                print("An error occured : '", subprocess.run(block_ip_out_command).stderr,".'")
            """
            #else:
            #subprocess.run(["service", "iptables", "save"])
            print("\nThe IP blocked successfully for outgoing traffic !")
    
        else:
            print("\nPlease, enter an available choice")

    elif scanner[host].state() == "down":
        print("\nThe IP is down, so you don't need to block it :)")

    else:
        print("\nPlease, enter the correct IP")
