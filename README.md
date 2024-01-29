# BFIInterview
BFI Interview Data Engineer E2E

REQUIRED DEPENDECIES as listed on requirement.txt:
1. selenium
2. bs4
3. csv
4. requests
5. fake-useraget
6. json
7. shillelagh
8. pandas
9. numpy
10. scikit-learn

The program runs multiple times in the following stages:
1. Data Crawling
2. Data Processing
3. Prediction

DATA CRAWLING

Open the Folder for the website that you want to scrape and run the code in the following order:
\n*X is the vendor name
1. python page_crawl_X.py
   - desc: Scrape the html or API for vendor pages
   - parameter: None
   - output: page html or json file in the folder page_html or page_json
2. python product_crawl_X.py yyyy-mm-dd
   - desc: Scrape the html or API for each product listed on page_html or page_json. Will loop for every html extension and same date as parameter on the folder
   - parameter: date
   - output: product html or json file in the folder product_html or product_json
3. python data_crawl.py yyyy-mm-dd
   - desc: Scrape the tagging on the product html or json based on needs. Will loop for every html extension and same date as parameter on the folder
   - parameter: date
   - output: data.csv
  
DATA PROCESSING

Due to hardware limition, using localhost database is prohibited; therefore, shillelagh library is used to treat CSV as local database.
\nRun the code in the following order:
1. python data_converting.py
   - desc: the program is to convert the CSV in all vendor folder into a suitable database in Database folder
   - parameter: None
   - output: source_X.csv file in Database folder
2. python make_product_table.py
   - desc: Using the source_X.csv in the Database folder to create thesaurus and ontology.
   - parameter: None
   - output: temp_product.csv, product.csv, map_brand.csv, map_detail.csv, map_category.csv (Database Folder)
3. python make_productmaster.py
   - desc: Create productmaster table with sample suitable for ML
   - parameter: None
   - output: productmaster.csv (Database Folder)
  
PREDICTION

Using Random Forest Regressor to predict price based on 2 days data.
\nRun the code in the following order:
1. python predict_price.py
   - desc: predict the price using Machine Learning. Applying one hot encoder to categorical sample.
   - parameter: None
   - output: productrecommendation.csv (Database Folder)

FUTURE IMPROVEMENT

The project is done in less than 24 hours. Most of the time used to find an alternative solution due to inability to install apps.
- Add Flagging in file name for data scraping to divide which file has been processed or not. This will also included in an additional parameter to fasten the process of scraping
- If possible, finding the backend API for scraping data to make the progress faster instead of using selenium
- Implement localhost database
- Create a real and accurate relational database structure
