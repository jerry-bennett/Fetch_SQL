# Sum quantity_purchased with a check for the presence of the field
        # quantity_purchased = sum(item.get('quantityPurchased', 0) for item in receipt['rewardsReceiptItemList'])