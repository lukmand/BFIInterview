from shillelagh.backends.apsw.db import connect
import csv
import os

connection = connect(":memory:")
cursor = connection.cursor()

try:
    os.remove("Database/product.csv")
except:
    pass
 
try:
    os.remove("Database/temp_product.csv")
except:
    pass 
 
try:
    os.remove("Database/map_category.csv")
except:
    pass 
    
try:
    os.remove("Database/detail.csv")
except:
    pass 
    
try:
    os.remove("Database/brand.csv")
except:
    pass 
    
try:
    os.remove("Database/productmaster.csv")
except:
    pass 
    
temp_product_query = '''
    select distinct *
    from "Database/source_blibli.csv"
    union
    select distinct *
    from "Database/source_tokopedia.csv"
    union
    select distinct *
    from "Database/source_indomaret.csv"
'''

map_cat_query = '''
    select distinct 
        category,
        case when upper(category) like '%GIGI%' or upper(category) like '%TOOTH%' or upper(category) like '%MULUT%' then 'ORAL HYGIENE' 
             when upper(category) like '%BAYI%' or upper(category) like '%BABY%' then 'BABY CARE'
             when upper(category) like '%FACIAL%' or upper(category) like '%FACE%' or upper(category) like '%WAJAH%' then 'FACIAL TREATMENT'
             when upper(category) like '%SHAMPOO%' or upper(category) like '%CONDITIONER%' or upper(category) like '%HAIR%' or upper(category) like '%RAMBUT%' then 'HAIR PRODUCT'
             when upper(category) like '%SABUN%' or upper(category) like '%SOAP%' or upper(category) like '%BODY%' or upper(category) like '%DEODORANT%' or upper(category) like '%PERFUME%' or upper(category) like '%COLOGNE%' then 'BODY WASH'
             when upper(category) like '%KECAP%' or upper(category) like '%KRIM%' or upper(category) like '%JUS%' or upper(category) like '%TEH%' or upper(category) like '%SUP%' or upper(category) like '%BUMBU%' then 'FOOD'
             when upper(category) like '%DETEJEN%' or upper(category) like '%PAKAIAN%' or upper(category) like '%PEMBERSIH%' then 'PEMBERSIH PERALATAN'
             else 'OTHERS'
        end 
    from "Database/temp_product.csv"
'''

detail_query = '''
    select distinct 
        detail,
        case when upper(detail) like '%ML' and cast(substr(detail, 1, 3) as int) between 100 and 249 then '100-249ml'
             when upper(detail) like '%ML' and cast(substr(detail, 1, 3) as int) between 250 and 499 then '250-499ml'
             when upper(detail) like '%ML' and cast(substr(detail, 1, 3) as int) between 500 and 749 then '500-749ml'
             when upper(detail) like '%ML' and cast(substr(detail, 1, 3) as int) between 749 and 999 then '749-999ml'
             when upper(detail) like '%ML' and cast(substr(detail, 1, 2) as int) between 1 and 99 then '1-99ml'
             when substr(upper(detail), -2, 2) <> 'ML' and substr(upper(detail), -1, 1) = 'L' then '1L+'
             when upper(detail) like '%GR' and cast(substr(detail, 1, 3) as int) between 100 and 249 then '100-249gr'
             when upper(detail) like '%GR' and cast(substr(detail, 1, 3) as int) between 250 and 499 then '250-499gr'
             when upper(detail) like '%GR' and cast(substr(detail, 1, 3) as int) between 500 and 749 then '500-749gr'
             when upper(detail) like '%GR' and cast(substr(detail, 1, 3) as int) between 749 and 999 then '749-999gr'
             when upper(detail) like '%GR' and cast(substr(detail, 1, 2) as int) between 1 and 99 then '1-99gr'
             when substr(upper(detail), -2, 2) = 'KG' and substr(upper(detail), -1, 1) <> 'G' then '1Kg+'
             else 'OTHERS'
        end         
    from "Database/temp_product.csv"
'''

brand_query = '''
    select distinct 
        name,
        upper(substr(name, 1, instr(name, ' ') - 1))
    from "Database/temp_product.csv"
'''

product_query = '''
    select distinct 
        a.*,
        "", 
        b.fixed_category,
        c.fixed_detail,
        d.brand
    from "Database/temp_product.csv" a
    inner join "Database/map_category.csv" b on a.category = b.category
    inner join "Database/detail.csv" c on a.detail = c.detail
    inner join "Database/brand.csv" d on a.name = d.name
'''

if not os.path.exists('Database/temp_product.csv') or os.stat('Database/temp_product.csv').st_size == 0:
    with open('Database/temp_product.csv', 'w', newline='', encoding='utf-8') as outf:
        data = csv.writer(outf, quoting=csv.QUOTE_NONNUMERIC)
        data.writerow(['id', 'name', 'price', 'originalprice', 'discountPercentage', 'detail', 'platform', 'category', 'scrapedate', 'seller'])  

if not os.path.exists('Database/map_category.csv') or os.stat('Database/map_category.csv').st_size == 0:
    with open('Database/map_category.csv', 'w', newline='', encoding='utf-8') as outf:
        data = csv.writer(outf, quoting=csv.QUOTE_NONNUMERIC)
        data.writerow(['category', 'fixed_category'])

if not os.path.exists('Database/detail.csv') or os.stat('Database/detail.csv').st_size == 0:
    with open('Database/detail.csv', 'w', newline='', encoding='utf-8') as outf:
        data = csv.writer(outf, quoting=csv.QUOTE_NONNUMERIC)
        data.writerow(['detail', 'fixed_detail'])  

if not os.path.exists('Database/brand.csv') or os.stat('Database/brand.csv').st_size == 0:
    with open('Database/brand.csv', 'w', newline='', encoding='utf-8') as outf:
        data = csv.writer(outf, quoting=csv.QUOTE_NONNUMERIC)
        data.writerow(['name', 'brand'])

if not os.path.exists('Database/product.csv') or os.stat('Database/product.csv').st_size == 0:
    with open('Database/product.csv', 'w', newline='', encoding='utf-8') as outf:
        data = csv.writer(outf, quoting=csv.QUOTE_NONNUMERIC)
        data.writerow(['id', 'name', 'price', 'originalprice', 'discountPercentage', 'detail', 'platform', 'category', 'scrapedate', 'seller', 'productmasterid', 'fixed_category', 'fixed_detail', 'brand'])          

with open('Database/temp_product.csv', 'a', newline='', encoding='utf-8') as outf:
    data = csv.writer(outf, quoting=csv.QUOTE_NONNUMERIC)
    for row in cursor.execute(temp_product_query):
        data.writerow(row)
        
with open('Database/map_category.csv', 'a', newline='', encoding='utf-8') as outf:
    data = csv.writer(outf, quoting=csv.QUOTE_NONNUMERIC)
    for row in cursor.execute(map_cat_query):
        data.writerow(row) 
        
with open('Database/detail.csv', 'a', newline='', encoding='utf-8') as outf:
    data = csv.writer(outf, quoting=csv.QUOTE_NONNUMERIC)
    for row in cursor.execute(detail_query):
        data.writerow(row) 
        
with open('Database/brand.csv', 'a', newline='', encoding='utf-8') as outf:
    data = csv.writer(outf, quoting=csv.QUOTE_NONNUMERIC)
    for row in cursor.execute(brand_query):
        data.writerow(row) 

with open('Database/product.csv', 'a', newline='', encoding='utf-8') as outf:
    data = csv.writer(outf, quoting=csv.QUOTE_NONNUMERIC)
    for row in cursor.execute(product_query):
        data.writerow(row)

