import csv

with open('Indomaret/data.csv', 'r') as infile:
    csvfile = csv.reader(infile)

    with open('Database/source_indomaret.csv', 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC )
        for line in csvfile:
            writer.writerow(line)
    
with open('BliBli/data.csv', 'r') as infile:
    csvfile = csv.reader(infile)

    with open('Database/source_blibli.csv', 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC )
        for line in csvfile:
            writer.writerow(line)

with open('Tokopedia/data.csv', 'r') as infile:
    csvfile = csv.reader(infile)

    with open('Database/source_tokopedia.csv', 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC )
        for line in csvfile:
            writer.writerow(line)