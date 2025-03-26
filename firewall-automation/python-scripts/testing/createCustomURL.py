from panos.firewall import Firewall
from panos.policies import Rulebase, SecurityRule
from panos.objects import CustomUrlCategory
import random

randomCustomURL = []

for i in range(0,61):
    tmplist = []
    tmplist.append('service'+str(i))
    for i in range(0,5):
        randomIP = str(random.randint(0,255))+'.'+str(random.randint(0,255))+'.'+str(random.randint(0,255))+'.'+str(random.randint(0,255))
        tmplist.append(randomIP)
    randomCustomURL.append(tmplist)

with open("../sensitive/ngfw1-azure.info", 'r') as f:
    ngfw1Azuree = f.read().splitlines()

fw = Firewall(ngfw1Azuree[0], ngfw1Azuree[1], ngfw1Azuree[2])

#print(randomCustomURL[59][0])
for i in randomCustomURL:
    try:

    
        custom_category = CustomUrlCategory(
            name=i[0],
            type="URL List",  # Options: 'URL List' (default) or 'Category Match'
            url_value=i[1:],  # List of URLs
            description="Custom block for "+i[0],
        )

        # Add and create the custom URL category on the firewall
        fw.add(custom_category)
        custom_category.create()
        print(i[0]+' worked')
    except:
        print ('already exists')
