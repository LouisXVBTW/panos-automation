from panos.firewall import Firewall
from panos.policies import Rulebase, SecurityRule

with open("../sensitive/ngfw1-azure.info", 'r') as f:
    ngfw1Azuree = f.read().splitlines()

fw = Firewall(ngfw1Azuree[0], ngfw1Azuree[1], ngfw1Azuree[2])
version = fw.refresh_system_info().version
print (version)

rulebase = fw.add(Rulebase())
rule = rulebase.add(SecurityRule("site to site 2"))

rule.refresh()
print(rule)