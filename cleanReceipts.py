import json
import csv

# Load the JSON data
with open('receipts_wrapped.json', 'r') as f:
    receipts_data = json.load(f)

# Prepare the CSV output file
with open('receipts_cleaned(update).csv', 'w', newline='') as csvfile:
    fieldnames = ['receipt_id', 'purchase_date', 'rewards_product_partner_id', 'barcode', 
                  'description', 'quantity_purchased', 'final_price', 'rewardsReceiptStatus',
                  'bonusPointsEarnedReason', 'pointsEarned', 'totalSpent']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write the header row
    writer.writeheader()

    # Process each receipt in the JSON data
    for receipt in receipts_data:
        receipt_id = receipt['_id']['$oid']  # Assuming the receipt id is stored in '_id' as an OID
        purchase_date = receipt.get('purchaseDate', {}).get('$date', 0) / 1000  # Default to 0 if 'purchaseDate' or '$date' is missing
        quantity_purchased = sum(item.get('quantityPurchased', 0) for item in receipt.get('rewardsReceiptItemList', []))  # Default to 0 if 'quantityPurchased' or 'rewardsReceiptItemList' is missing

        rewards_product_partner_id = receipt['rewardsReceiptItemList'][0].get('rewardsProductPartnerId', '')
        barcode = receipt['rewardsReceiptItemList'][0].get('barcode', '')
        description = receipt['rewardsReceiptItemList'][0].get('description', '')
        
        # # Sum quantity_purchased with a check for the presence of the field
        # quantity_purchased = sum(item.get('quantityPurchased', 0) for item in receipt['rewardsReceiptItemList'])
        
        # Sum final_price with a check for the presence of the field
        final_price = sum(float(item.get('finalPrice', 0)) for item in receipt['rewardsReceiptItemList'])
        
        rewardsReceiptStatus = receipt.get('rewardsReceiptStatus', '')
        
        # Additional fields
        bonusPointsEarnedReason = receipt.get('bonusPointsEarnedReason', '')
        pointsEarned = receipt.get('pointsEarned', 0.0)
        totalSpent = receipt.get('totalSpent', 0.0)

        # Write the cleaned data row to the CSV
        writer.writerow({
            'receipt_id': receipt_id,
            'purchase_date': purchase_date,
            'rewards_product_partner_id': rewards_product_partner_id,
            'barcode': barcode,
            'description': description,
            'quantity_purchased': quantity_purchased,
            'final_price': final_price,
            'rewardsReceiptStatus': rewardsReceiptStatus,
            'bonusPointsEarnedReason': bonusPointsEarnedReason,
            'pointsEarned': pointsEarned,
            'totalSpent': totalSpent
        })
