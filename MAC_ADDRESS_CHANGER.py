import subprocess
import optparse
import re 


def get_arguments() :
    parser = optparse.OptionParser()
    parser.add_option("-i" , "--interface" , dest="interface" , help="This is for network interface ")
    parser.add_option("-m" , "--New_mac" , dest="New_MAC_Address" , help="This is for MAC Address") 
    options , arguments = parser.parse_args()
    
    if not options.interface :
        parser.error("[-] Specify an Interface please | use -h to get helped")
    if not options.New_MAC_Address :
        parser.error("[-] Specify a MAC Address | use -h to get helped ")
    
    return options 

def mac_changer(interface , New_MAC_Address):
    subprocess.call(f"ifconfig {interface} down",shell=True)
    subprocess.call(f"ifconfig {interface} hw ether {New_MAC_Address}" , shell=True)
    subprocess.call(f"ifconfig {interface} up", shell=True )
    print(f"[+] Changing MAC Address for {interface} to {New_MAC_Address}")
    

def get_mac(interface):
    ifconfig_result = subprocess.check_output(f"ifconfig {interface}" , shell=True).decode("UTF-8")
    MAC_Address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result )
    return MAC_Address[0]

options = get_arguments()
mac_changer(options.interface , options.New_MAC_Address)
mac_address = get_mac(options.interface)

if mac_address == options.New_MAC_Address :
    print(f"[+] MAC Address changed successfully {options.New_MAC_Address}")
else:
    print("Something went Wrong ;) !")