from panos.firewall import Firewall

with open("../sensitive/ngfw1-azure.info", 'r') as f:
    ngfw1Azuree = f.read().splitlines()

fw = Firewall(ngfw1Azuree[0], ngfw1Azuree[1], ngfw1Azuree[2])



