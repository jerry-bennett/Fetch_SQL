SELECT b.name AS brand_name, COUNT(r.receipt_id) AS receipts_scanned
FROM receipt r
JOIN brands b ON r.barcode = b.barcode
WHERE FROM_UNIXTIME(r.purchase_date / 1000) BETWEEN '2021-01-01 00:00:00' AND '2021-02-26 23:59:59'
GROUP BY b.name
ORDER BY receipts_scanned DESC
LIMIT 5;

/* Top 5 Brands by Receipts Scanned:
    1. Tostitos - 20
    2. Swanson - 10
    3. Cracker Barrel Cheese - 7
    4. Diet Chris Cola - 7
    5. Prego - 7
*/
    