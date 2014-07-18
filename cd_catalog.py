import xml.etree.ElementTree as ET 
root = ET.parse(source = 'cd_catalog.xml') 
count = 0 disks = root.getiterator() 

#find the price
for disk in disks:     
  if disk.tag == 'CD':         
    print count         
    price = disk.find('PRICE').text        
    print price *= count  for disk in disks:     
    
#find the country  
if disk.tag == 'CD':         
country = disk.find('COUNTRY")        
  if country == 'USA':             
    print country.text    
