import csv
#create new files XML:eXtensible Markup Language
csvFile='kapcsv78.csv'
xmlFile='Xmlcsv78.xml'
# to read csv file
csvData=csv.reader(open(csvFile))
xmlData=open(xmlFile,'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
#there must be only one top level tag

xmlData.write('<college>'+"\n" )

rowNum = 0

for row in csvData:
#condition to check space
    if rowNum == 0:
        tags = row
        for i in range(len(tags)):
            tags[i]=tags[i].replace(' ','_')
    else:
        xmlData.write('<row>'+"\n")
        
        for i in range(len(tags)):
             xmlData.write(' '+'<'+tags[i]+'>'+row[i]+'</'+tags[i]+'>'+"\n")
             
        xmlData.write('</row>'+"\n")
    rowNum +=1
xmlData.write('</college>'+"\n")
xmlData.close()

             
