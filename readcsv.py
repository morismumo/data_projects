import csv


with open('data.csv','r') as f:
    myreader=csv.DictReader(f)
    headers=next(myreader)
    count = 0 
    for row in myreader:
        print(row['name'])
        count +=1

        if count == 10:
            break
