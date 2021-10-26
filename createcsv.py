import csv
this = 1234.3

with open ('mydoc.csv', 'w' ) as f:
    fieldnames = ['one', 'two']
    thewriter = csv.DictWriter(f, fieldnames = fieldnames)
    thewriter.writeheader()

    for i in range (1,100):
        thewriter.writerow({'one' : str(this), 'two' : 'text2'})