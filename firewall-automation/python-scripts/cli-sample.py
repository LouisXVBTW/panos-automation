from panos.firewall import Firewall
import xml.etree.ElementTree as ET
import xml.dom.minidom
def pprint(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

with open("../sensitive/ngfw1-local.info", 'r') as f:
    ngfw1Azuree = f.read().splitlines()

fw = Firewall(ngfw1Azuree[0], ngfw1Azuree[1], ngfw1Azuree[2])
print ('----------- CONNECTED -----------')
system_info = fw.op('show interface "ethernet1/1"')

print(type(system_info))
print (pprint(system_info).split("<name>")[1].split('</name>')[0])



