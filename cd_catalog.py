import xml.etree.ElementTree as ET 
root = ET.parse(source = 'cd_catalog.xml') 
#Part1 total price of CD;s
#Part2 min, max, avg price of CD;s
#Part3 total number released during 1990
#Part4 names of artists from USA
#Part4 List comprehension to minimize code

price_count = 0 
total_count = 0



disks = root.getiterator() 

#find the price
for disk in disks:     
  if disk.tag == 'CD':         
    print count         
    price = disk.find('PRICE').text        
    print price *= count  for disk in disks:     
    
#find the name   
for disk in disks:
  if disk.tag == 'CD':         
  country = disk.find('COUNTRY")        
    if country == 'USA':    
      name = disk.find('NAME').text
      print name 
      
    
    


