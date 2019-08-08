# XMLParser

This is an XML Parser that reads DHCP files that are downloaded. It takes a directory as an input and reads all the .xml files in that specific directory. After reading them, it creates a temp .xml file and then stores the following attributes into a .csv file:
   * Name
   [ ] Start Range
   [ ] End Range
   [ ] Scope ID
   [ ] Subnet Mask
   [ ] Lease Duration
   [ ] State
   [ ] Type
   [ ] Nap Enabled
   [ ] Description
   
When printing in the .csv file, it creates two more columns under the following names:
    New Name
    New Description.
    
The .csv file, named as ParsedXML.csv will have the following attributes in this order:
    Name	
    Scope ID	
    New Name	
    Subnet Mask	
    Start Range	
    End Range	
    Lease Duration	
    State	
    Type	
    Nap Enabled	
    Description	
    New Description
