from panos.firewall import Firewall
from panos.policies import Rulebase, SecurityRule
from panos.objects import CustomUrlCategory
from panos.objects import Edl


with open("../sensitive/ngfw1-azure.info", 'r') as f:
    ngfw1Azuree = f.read().splitlines()

fw = Firewall(ngfw1Azuree[0], ngfw1Azuree[1], ngfw1Azuree[2])
version = fw.refresh_system_info().version
print (version)

rulebase = fw.add(Rulebase())
rules = SecurityRule.refreshall(rulebase)




url_categories = CustomUrlCategory.refreshall(fw)

for url in url_categories:
    print(url.name)
    print(url.url_value)


    edl = Edl(
        name=url.name+'-EDL',
        edl_type="url",  # Can be 'ip', 'domain', or 'url'
        source="http://example.com/"+url.name+'.txt',  # Replace with your actual EDL URL
        repeat ="five-minute",
        description="List of IPS for "+url.name,
    )

    # Add and apply to the firewall
    fw.add(edl)
    edl.create()
    print(url.name+' worked')



