LOAD DATA LOCAL INFILE '/Users/Jerry Benenett/Documents/Programming Stuff/Fetch_SQL/receipts_cleaned.csv'
INTO TABLE receipt
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'  -- or '\n' depending on your file
IGNORE 1 ROWS
(receipt_id, purchase_date, rewards_product_partner_id, barcode, description, quantity_purchased, final_price);

TRUNCATE TABLE receipt