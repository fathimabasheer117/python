import csv 
dict_value = [
{"name":"fathima","age":19,"course":"mca"},
{"name":"gopika","age":19,"course":"mca"},
{"name":"manya","age":19,"course":"mca"},
]

fields = ["name","age","course"]

with open('dict.csv','r+') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=fields)
    writer.writeheader()
    writer.writerows(dict_value)
    csvfile.close()

with open('dict.csv','r') as csvfiles:
    readerobj = csv.reader(csvfiles)
    for rows in readerobj:
        print(rows)
