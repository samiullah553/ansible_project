import netmiko
from netmiko import ConnectHandler
from pprint import pprint

R1 ={
        "device_type":"cisco_ios",
        "ip":"9.1.1.2",
        "password":"cisco12",
        "username":"admin",
        "secret":"cisco12"
        }

net_connect =ConnectHandler(**R1)
print(net_connect.send_command("show ip interface brief"))

net_connect.disconnect()
