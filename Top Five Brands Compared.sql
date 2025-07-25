WITH RecentMonth AS (
    SELECT 
        b.name AS brand_name, 
        COUNT(r.receipt_id) AS receipts_scanned
    FROM receipt r
    JOIN brands b ON r.barcode = b.barcode
    WHERE FROM_UNIXTIME(r.purchase_date / 1000) BETWEEN '2021-01-01 00:00:00' AND '2021-02-26 23:59:59'
    GROUP BY b.name
),
PreviousMonth AS (
    SELECT 
        b.name AS brand_name, 
        COUNT(r.receipt_id) AS receipts_scanned
    FROM receipt r
    JOIN brands b ON r.barcode = b.barcode
    WHERE FROM_UNIXTIME(r.purchase_date / 1000) BETWEEN '2021-01-01 00:00:00' AND '2021-01-31 23:59:59'
    GROUP BY b.name
)
-- Emulating FULL OUTER JOIN with no LIMIT in individual queries
SELECT 
    COALESCE(rm.brand_name, pm.brand_name) AS brand_name,
    COALESCE(rm.receipts_scanned, 0) AS recent_month_receipts,
    COALESCE(pm.receipts_scanned, 0) AS previous_month_receipts
FROM RecentMonth rm
LEFT JOIN PreviousMonth pm
ON rm.brand_name = pm.brand_name
UNION ALL
SELECT 
    COALESCE(rm.brand_name, pm.brand_name) AS brand_name,
    COALESCE(rm.receipts_scanned, 0) AS recent_month_receipts,
    COALESCE(pm.receipts_scanned, 0) AS previous_month_receipts
FROM PreviousMonth pm
LEFT JOIN RecentMonth rm
ON pm.brand_name = rm.brand_name
WHERE rm.brand_name IS NULL
-- Filter for the top 5 combined brands
ORDER BY (recent_month_receipts + previous_month_receipts) DESC
LIMIT 5;

-- Seems to be the same result when compared to the previous month. No massive change.