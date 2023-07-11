import xml.dom.minidom
from ncclient import manager


m = manager.connect(
    host="192.168.56.103", #tu ip de la maquina router
    port=830,
    username="cisco", #User de tu router
    password="cisco123!", #password de tu router
    hostkey_verify=False
    )


'''
print("#Supported Capabilities (YANG models):") #Enlaces comentandos paso1
for capability in m.server_capabilities:
    print(capability)
'''


netconf_reply = m.get_config(source="running")  #informacion del router paso 2
#print(netconf_reply)


netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""
netconf_reply = m.get_config(source="running", filter=netconf_filter)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()) #filtro de datos 3 y 4


#paso 5
#cambio nombre hostname
'''
netconf_hostname = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">  
     <hostname>Alcaino-Alcaino</hostname> 
  </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_hostname)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
'''
#paso 6
#creacion de loopback
#cambiar por datos solicitados
netconf_loopback = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>1</name> 
    <description>Mi primer loopback ncclient</description>
    <ip>
     <address>
      <primary>
       <address>1.1.1.1</address> 
       <mask>255.255.255.255</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_loopback)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
