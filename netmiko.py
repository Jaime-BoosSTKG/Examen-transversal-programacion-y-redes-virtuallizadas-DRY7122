import requests
import netmiko
import json 
from netmiko import ConnectHandler 

cisco1 = { "ip": "192.168.56.115", 
"device_type": "cisco_ios", 
"username": "cisco", 
"password": "cisco123!", 
}
 # Show command that we execute.
command = "show run"
with ConnectHandler(**cisco1) as net_connect: 
    output = net_connect.send_command(command)
    print() 
    print(output) 
    print()
# Automatically cleans-up the output so that only the show output is returned
 