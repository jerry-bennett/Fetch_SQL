import json
import pandas as pd

# Initialize list for cleaned data
cleaned_data = []

# Open the JSON file and load it
with open('receipts_wrapped.json', 'r') as f:
    receipts_data = json.load(f)  # Now it should be a list of JSON objects

    # Iterate over each receipt in the JSON data
    for receipt in receipts_data:
        receipt_id = receipt["_id"]["$oid"]
        purchase_date = receipt["purchaseDate"]["$date"] if "purchaseDate" in receipt else None
        rewards_items = receipt.get("rewardsReceiptItemList", [])

        for item in rewards_items:
            rewards_product_partner_id = item.get("rewardsProductPartnerId", None)
            barcode = item.get("barcode", None)
            description = item.get("description", "Unknown")
            quantity_purchased = item.get("quantityPurchased", 0)
            final_price = item.get("finalPrice", 0.0)
            
            # Only include valid entries with a product partner ID
            if rewards_product_partner_id:
                cleaned_data.append({
                    "receipt_id": receipt_id,
                    "purchase_date": purchase_date,
                    "rewards_product_partner_id": rewards_product_partner_id,
                    "barcode": barcode,
                    "description": description,
                    "quantity_purchased": quantity_purchased,
                    "final_price": final_price
                })

# Convert the cleaned data into a DataFrame
df = pd.DataFrame(cleaned_data)

# Save to CSV
df.to_csv('receipts_cleaned.csv', index=False)

print("Data cleaned and saved to CSV.")
