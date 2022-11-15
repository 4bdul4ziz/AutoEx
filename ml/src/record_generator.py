import csv
def generating_csv():
    with open('/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/records.csv','r') as inp, open('/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/judgement.csv', 'a') as out:
        reader = csv.reader(inp)
        writer = csv.writer(out, delimiter=',')
        #writer.writerow(['StudentID'] + next(reader))
        writer.writerows([i] + row for i, row in enumerate(reader, 1))
    
    return "csv file succesfully generated!"
