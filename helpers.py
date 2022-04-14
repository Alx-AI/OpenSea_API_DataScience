# Parse asset data retrieved from OpenSea, reference https://docs.opensea.io/reference/
# Additional info on data sources https://www.figma.com/file/mIN2XA1vSH2HktxQ0dDH7z/TheOracle_Data?node-id=0%3A1

def parse_assets_data(assets_dict):
    asset_id = assets_dict['token_id']

    try:
        creator_username = assets_dict['creator']['user']['username']
    except:
        creator_username = None

    try:
        creator_address = assets_dict['creator']['address']
    except:
        creator_address = None

    try:
        owner_username = assets_dict['owner']['user']['username']
    except:
        owner_username = None

    owner_address = assets_dict['owner']['address']

    traits = assets_dict['traits']
    num_sales = int(assets_dict['num_sales'])

    result = {'asset_id': asset_id,
              'creator_username': creator_username,
              'creator_address': creator_address,
              'owner_username': owner_username,
              'owner_address': owner_address,
              'traits': traits,
              'num_sales': num_sales}

    return result

# Parse event data, there are 7 types of events each with different populated fields but the same fields all the same
# Event types to use: 'successful' (sale), 'created' (listing), ' cancelled' , 'bid_entered', 'bid_withdrawn'
# Event types not in use:'transfer', 'approve'

def parse_events_data(event_dict):
    is_bundle = False

    if event_dict['asset'] != None:
        assets_id = event_dict['asset']['token_id']
    elif event_dict['asset_bundle'] != None:
        assets_id = [asset['token_id'] for asset in event_dict['asset_bundle']['assets']]
        is_bundle = True

    asset = event_dict['asset']
    seller_address = event_dict['seller']['address']
    buyer_address = event_dict['winner_account']['address']

    try:
        seller_username = event_dict['seller']['user']['username']
    except:
        seller_username = None
    try:
        buyer_username = event_dict['winner_account']['user']['username']
    except:
        buyer_username = None
    try:
        auction_type = event_dict['auction_type']
    except:
        auction_type = None

    timestamp = event_dict['transaction']['timestamp']
    total_price = float(event_dict['total_price'])
    payment_token = event_dict['payment_token']['symbol']
    usd_price = float(event_dict['payment_token']['usd_price'])
    transaction_hash = event_dict['transaction']['transaction_hash']

    result = {'asset' : asset,
              'is_bundle': is_bundle,
              'assets_id': assets_id,
              'auction_type': auction_type,
              'seller_address': seller_address,
              'buyer_address': buyer_address,
              'buyer_username': buyer_username,
              'seller_username': seller_username,
              'timestamp': timestamp,
              'total_price': total_price,
              'payment_token': payment_token,
              'usd_price': usd_price,
              'transaction_hash': transaction_hash}

    return result


# legacy function
def parse_animetas_data(animetas_dict):
    animetas_id = animetas_dict['token_id']

    try:
        creator_username = animetas_dict['creator']['user']['username']
    except:
        creator_username = None

    try:
        creator_address = animetas_dict['creator']['address']
    except:
        creator_address = None

    try:
        owner_username = animetas_dict['owner']['user']['username']
    except:
        owner_username = None

    owner_address = animetas_dict['owner']['address']

    traits = animetas_dict['traits']
    num_sales = int(animetas_dict['num_sales'])

    result = {'animeta_id': animetas_id,
              'creator_username': creator_username,
              'creator_address': creator_address,
              'owner_username': owner_username,
              'owner_address': owner_address,
              'traits': traits,
              'num_sales': num_sales}

    return result


# legacy function
def parse_sale_data(sale_dict):
    is_bundle = False

    if sale_dict['asset'] is not None:
        asset_id = sale_dict['asset']['token_id']
    elif sale_dict['asset_bundle'] is not None:
        asset_id = [asset['token_id'] for asset in sale_dict['asset_bundle']['assets']]
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
              'event_id': asset_id,
              'seller_address': seller_address,
              'buyer_address': buyer_address,
              'buyer_username': buyer_username,
              'seller_username': seller_username,
              'timestamp': timestamp,
              'total_price': total_price,
              'payment_token': payment_token,
              'usd_price': usd_price,
              'transaction_hash': transaction_hash}

    return result


# legacy function
def parse_listing_data(listing_dict):
    is_bundle = False

    if listing_dict['asset'] is not None:
        asset_id = listing_dict['asset']['token_id']
    elif listing_dict['asset_bundle'] is not None:
        asset_id = [asset['token_id'] for asset in listing_dict['asset_bundle']['assets']]
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
              'event_id': asset_id,
              'seller_address': seller_address,
              'seller_username': seller_username,
              'created_date': created_date,
              'starting_price': starting_price,
              'payment_token': payment_token,
              'usd_price': usd_price}

    return result


def parse_collection_data(collection_dict):
    name = collection_dict['name']
    market_cap = collection_dict['stats']['market_cap']
    stats = collection_dict['stats']
    created_date = collection_dict['created_date']
    dev_buyer_fee_basis_points = collection_dict['dev_buyer_fee_basis_points']
    dev_seller_fee_basis_points = collection_dict['dev_seller_fee_basis_points']
    opensea_buyer_fee_basis_points = collection_dict['opensea_buyer_fee_basis_points']
    opensea_seller_fee_basis_points = collection_dict['opensea_seller_fee_basis_points']

    result = {'name': name,
              'market_cap': market_cap,
              'stats': stats,
              'created_date': created_date,
              'dev_buyer_fee_basis_points': dev_buyer_fee_basis_points,
              'dev_seller_fee_basis_points': dev_seller_fee_basis_points,
              'opensea_buyer_fee_basis_points': opensea_buyer_fee_basis_points,
              'opensea_seller_fee_basis_points': opensea_seller_fee_basis_points
              }

    return result
