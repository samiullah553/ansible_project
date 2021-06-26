#This is aboute how to get enable and config mode in python.
#modification are done only on config mode so if you want to modify the device configuration
#so how to get it.
#Author Samiullah
#Email: sameullah553@gmail.com

import netmiko
from netmiko import ConnectHandler
from pprint import pprint
import genie

R1 ={
        "device_type":"cisco_ios",
        "ip":"x.x.x.x",
        "username":"admin",
        "password":"cisco12",
        "secret":"cisco12"
        }
net_connect =ConnectHandler(**R1)
#enable_mode just use enable() function.
net_connect.enable()
#For configuration mode we use config_mode() function.
net_connect.config_mode()
#Here now you can send Configuration commnad. use list for a bunch of commands 
#for example
interface_config =[
        "interface fastethernet0/0",
        "ip address x.x.x.x/24",
        "no shutdown"
        ]
#To send a bunch of commands we will use "send_config_set()" function
net_connect.send_config_set(interface_config)
net_connect.disconnect()
