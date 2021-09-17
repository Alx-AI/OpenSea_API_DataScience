def parse_savages_data(savages_dict):
    
    savage_id = savages_dict['token_id']
    
    try:
        creator_username = savages_dict['creator']['user']['username']
    except:
        creator_username = None
    try:
        creator_address = savages_dict['creator']['address']
    except:
        creator_address = None
    
    try:
        owner_username = savages_dict['owner']['user']['username']
    except:
        owner_username = None
    
    owner_address = savages_dict['owner']['address']
    
    traits = savages_dict['traits']
    num_sales = int(savages_dict['num_sales'])
        
    result = {'savage_id': savage_id,
              'creator_username': creator_username,
              'creator_address': creator_address,
              'owner_username': owner_username,
              'owner_address': owner_address,
              'traits': traits,
              'num_sales': num_sales}
    
    return result


def parse_sale_data(sale_dict):
    
    is_bundle = False

    if sale_dict['asset'] != None:
        BAYCs_id = sale_dict['asset']['token_id']
    elif sale_dict['asset_bundle'] != None:
        BAYCs_id = [asset['token_id'] for asset in sale_dict['asset_bundle']['assets']]
        is_bundle = True
    
    
    seller_address = sale_dict['seller']['address']
    buyer_address = sale_dict['winner_account']['address']
    
    try:
        seller_username = sale_dict['seller']['user']['username']
    except:
        seller_username = None    
    try:
        buyer_username = sale_dict['winner_account']['user']['username']
    except:
        buyer_username = None
    
    timestamp = sale_dict['transaction']['timestamp']
    total_price = float(sale_dict['total_price'])
    payment_token = sale_dict['payment_token']['symbol']
    usd_price = float(sale_dict['payment_token']['usd_price'])
    transaction_hash = sale_dict['transaction']['transaction_hash']
    

    result = {'is_bundle': is_bundle,
              'BAYC_id': BAYCs_id,
              'seller_address': seller_address,
              'buyer_address': buyer_address,
              'buyer_username': buyer_username,
              'seller_username':seller_username,
              'timestamp': timestamp,
              'total_price': total_price, 
              'payment_token': payment_token,
              'usd_price': usd_price,
              'transaction_hash': transaction_hash}
    
    return result

def parse_listing_data(listing_dict):
    
    is_bundle = False

    if listing_dict['asset'] != None:
        BAYCs_id = listing_dict['asset']['token_id']
    elif listing_dict['asset_bundle'] != None:
        BAYCs_id = [asset['token_id'] for asset in listing_dict['asset_bundle']['assets']]
        is_bundle = True
    
    
    seller_address = listing_dict['seller']['address']
    
    try:
        seller_username = listing_dict['seller']['user']['username']
    except:
        seller_username = None    
    
    created_date = listing_dict['created_date']
    starting_price = float(listing_dict['starting_price'])
    payment_token = listing_dict['payment_token']['symbol']
    usd_price = float(listing_dict['payment_token']['usd_price'])
    

    result = {'is_bundle': is_bundle,
              'BAYC_id': BAYCs_id,
              'seller_address': seller_address,
              'seller_username':seller_username,
              'created_date': created_date,
              'starting_price': starting_price, 
              'payment_token': payment_token,
              'usd_price': usd_price}
    
    return result