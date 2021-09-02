tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
    colWidths= [0] * len(table)
    n=0 #numerator
        for i in table:
           m=0 #holder
           for j in i:
               #print(len(j)) #prints out length of each word
               if len(j) >= m:
                   m= len(j)
               else:
                   continue
           colWidths[n]=m
           n+=1
    for y in range (len(table[0])):
        for x in range(len(table)):         
            print(table[x][y].rjust(8, ' '),end='')
        print()
               


    



printTable(tableData)
