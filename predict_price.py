from shillelagh.backends.apsw.db import connect
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import warnings
import os
import csv

connection = connect(":memory:")
cursor = connection.cursor()

try:
    os.remove("Database/productrecommendation.csv")
except:
    pass

querylist = []
query = '''
    select distinct 
        cast(x.id as int),
        x.type,
        x.name,
        x.detail,
        cast(replace(y.price, '.', '') as int)
    from "Database/productmaster.csv" x
    inner join "Database/product.csv" y on x.id = y.productmasterid
'''

for row in cursor.execute(query):
    querylist.append(row)
    
df = pd.DataFrame(querylist, columns =['id', 'type', 'brand', 'detail', 'price'])
df2 = pd.get_dummies(df, dtype=np.int64).set_index('id')

X = df2.drop('price', axis=1)
y = df2['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=25, random_state = 101)

model = RandomForestRegressor(n_estimators = 10, max_depth = 10, random_state = 101)
model.fit(X_train, y_train.values.ravel())

warnings.filterwarnings('ignore')

pred = model.predict(X_test)
result = X_test
result['price'] = y_test
result['prediction'] = pred.tolist()
result.reset_index(inplace=True)

productrecommendation = '''
    select distinct
        id,
        cast(prediction as int),
        DATE('now')
    from result
'''

if not os.path.exists('Database/productrecommendation.csv') or os.stat('Database/productrecommendation.csv').st_size == 0:
    with open('Database/productrecommendation.csv', 'w', newline='', encoding='utf-8') as outf:
        data = csv.writer(outf, quoting=csv.QUOTE_NONNUMERIC)
        data.writerow(['id', 'price', 'date'])              

with open('Database/productrecommendation.csv', 'a', newline='', encoding='utf-8') as outf:
    data = csv.writer(outf, quoting=csv.QUOTE_NONNUMERIC)
    for row in cursor.execute(productrecommendation):
        data.writerow(row)