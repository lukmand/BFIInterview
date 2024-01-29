from shillelagh.backends.apsw.db import connect
import csv
import os

try:
    os.remove("Database/productmaster.csv")
except:
    pass

connection = connect(":memory:")
cursor = connection.cursor()

productmaster_query = '''
    select distinct 
        dense_rank() over(order by fixed_category, brand, fixed_detail),
        fixed_category,
        brand,
        fixed_detail
    from "Database/product.csv"
'''

if not os.path.exists('Database/productmaster.csv') or os.stat('Database/productmaster.csv').st_size == 0:
    with open('Database/productmaster.csv', 'w', newline='', encoding='utf-8') as outf:
        data = csv.writer(outf, quoting=csv.QUOTE_NONNUMERIC)
        data.writerow(['id', 'type', 'name', 'detail'])              

with open('Database/productmaster.csv', 'a', newline='', encoding='utf-8') as outf:
    data = csv.writer(outf, quoting=csv.QUOTE_NONNUMERIC)
    for row in cursor.execute(productmaster_query):
        data.writerow(row)
        
update_id_query = '''
    update "Database/product.csv"
    set productmasterid = cast(x.id as int)
    from "Database/productmaster.csv" x
    where x.type = "Database/product.csv".fixed_category
        and x.detail = "Database/product.csv".fixed_detail
        and x.name = "Database/product.csv".brand
'''

cursor.execute(update_id_query)