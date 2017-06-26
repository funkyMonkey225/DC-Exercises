max_height = 3

height = 0
while height < max_height:
    #print "*"
    height = height + 1
    
    width = 0
    row = ""
    while width < max_height:
        #print "*"
        row = row + "*"
        width = width + 1
    
    print row
    
print "done!"