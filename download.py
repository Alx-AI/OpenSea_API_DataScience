from helpers import parse_assets_data, parse_sale_data, parse_listing_data
from datetime import date, timedelta, datetime
import os
import numpy as np
import requests
import time


def download_asset_info(save_location, asset_name="animeta", contract="0x18df6c571f6fe9283b87f910e41dc5c8b77b7da5",
                        limit=1000, request_buffer=0):
    '''
    Download assets from a specific contract
    OpenSea API  only supports offset up to 10,000 as a result we increment token_ids
    Some projects do not start at the same number(e.g. 0 or 1) or increment at all
    Default is taking the first 50,000 assets, (limit = 1000) * 50 per call
    request_buffer is time in seconds to sleep between requests to avoid throttling
    '''
    url = "https://api.opensea.io/api/v1/assets"
    listofassets = []
    # If saved folder doesn't exist, then create it.
    if not os.path.isdir(save_location):
        os.makedirs(save_location)
    for i in range(0, limit):
        time.sleep(request_buffer)
        querystring = {"token_ids": list(range((i * 30), (i * 30) + 30)),
                       "asset_contract_address": contract,
                       "order_direction": "desc",
                       "offset": "0",
                       "limit": "30"}
        response = requests.request("GET", url, params=querystring)

        print(i, end=" ")
        if response.status_code != 200:
            print(response.json())
            print('error')
            break

        # Getting asset data
        assets = response.json()['assets']
        if assets == []:
            break
        # Parsing assets data to be done later
        # parsed_assets = [parse_assets_data(asset) for asset in assets]
        # storing parsed assets data into list
        listofassets.append(assets)
        if i == limit:
            print("There are likely more assets that exist in this collection than were downloaded")

    # Flatten everything
    listofassets = [item for sublist in listofassets for item in sublist]
    print(str(len(listofassets)) + " assets saved to" + save_location + asset_name + '_list' +
          str(date.today()) + r'.npz')
    np.savez(save_location + asset_name + '_list' + str(date.today()) + r'.npz', listofassets)


def download_event_info(save_location, contract="0x18df6c571f6fe9283b87f910e41dc5c8b77b7da5",
                        start_date=date(2021, 7, 30), end_date=date.today(), event_type='all', hour_chunks=24,
                        request_buffer=.5):
    '''
    Download events from a specific contract
    We increment by date to save historical context and avoid OpenSea API limitations
    Download info from start_date to end_date and save them all into their own day's files
    Start date should be first day that collection existed
    Default values to animetas first event ever 7/30/21 to today
    Can specify the event_type of types you are trying to download or set it to 'all' for all
    Event types include: 'created' for new auctions, 'successful' for sales, 'cancelled', 'bid_entered', 'bid_withdrawn'
    Both 'transfer' and 'approve' are supposed to be event types but don't seem to be used by most collections
    hour_chunks = number of hours to search at a time, if > 10,000 of one type of event in a day need to reduce from 24
    request_buffer is time in seconds to sleep between requests to avoid throttling
    '''
    url = "https://api.opensea.io/api/v1/events"
    # get the number of days that we want to download and save an event for for
    delta = end_date - start_date
    count_days = int(delta.days)
    # If saved folder doesn't exist, then create it.
    if not os.path.isdir(save_location):
        os.makedirs(save_location)

    for i in range(count_days + 1):
        events_that_day = []
        # set start and end of the day we are checking, if it's today set end to current time
        if date.today() == (start_date + timedelta(days=i)):
            before = datetime.now()
            after = datetime.combine((start_date + timedelta(days=i)), datetime.min.time())
        else:
            before = datetime.combine((start_date + timedelta(days=i + 1)), datetime.min.time())
            after = datetime.combine((start_date + timedelta(days=i)), datetime.min.time())
        # There are too many transactions, now have to break them up by chunks in the day
        chunk_count = 24 / hour_chunks
        time.sleep(request_buffer)
        for chunk in range(int(chunk_count)):
            end = False
            for j in range(0, 50):
                # add the hour_chunk to the start of the day (after) time for each chunk
                # use the actual before if we pass it chronologically though
                changed_before = after + timedelta(hours=hour_chunks * (chunk + 1)) - timedelta(minutes=1)
                changed_after = after + timedelta(hours=hour_chunks * (chunk))

                # this should only happen on the last chunk of a split day or if on current day
                if before < changed_before:
                    changed_before = before
                    end = True
                # if it's a single type run through the request normally
                if event_type != 'all':
                    querystring = {"asset_contract_address": contract,
                                   "event_type": event_type,
                                   "only_opensea": "false",
                                   "offset": j * 300,
                                   "occurred_before": changed_before,
                                   "occurred_after": changed_after,
                                   "limit": "300"}
                    headers = {"Accept": "application/json"}

                    response = requests.request("GET", url, headers=headers, params=querystring)

                    print(str(j) + event_type + str(changed_before.date()), end=" ")
                    if response.status_code != 200:
                        print('error')
                        print(response.json())
                        break

                    # Getting assets events data
                    asset_events = response.json()['asset_events']

                    if asset_events == []:
                        end = True
                        break

                    # Parsing assets events data
                    # parsed_asset_events = [parse_event_data(event) for event in asset_events]
                    # storing parsed assets data into list
                    events_that_day.append(asset_events)

                # if we want to do all types, do the above but once for each type
                else:
                    event_types = ['created', 'successful', 'cancelled', 'bid_entered', 'bid_withdrawn']
                    for e_type in event_types:
                        time.sleep(.5)
                        querystring = {"asset_contract_address": contract,
                                       "event_type": e_type,
                                       "only_opensea": "false",
                                       "offset": j * 100,
                                       "occurred_before": changed_before,
                                       "occurred_after": changed_after,
                                       "limit": "100"}
                        headers = {"Accept": "application/json"}

                        response = requests.request("GET", url, headers=headers, params=querystring)

                        print(str(j) + e_type + str(changed_before.date()), end=' ')
                        if response.status_code != 200:
                            print('error')
                            print(response.json())
                            break

                        # Getting assets events data
                        asset_events = response.json()['asset_events']

                        if asset_events == []:
                            end = True
                            break

                        # Parsing assets events data
                        # parsed_asset_events = [parse_event_data(event) for event in asset_events]
                        # storing parsed assets data into list
                        events_that_day.append(asset_events)
                if end:
                    break
            if end:
                break
        if len(events_that_day) > 0:
            events_that_day = [item for sublist in events_that_day for item in sublist]
            np.savez(save_location + "assets_events_list_" + str((start_date + timedelta(days=i))) + '.npz', events_that_day)
            print(str(len(events_that_day)) + " events saved to" + save_location + "assets_events_list_" + str(
                start_date + timedelta(days=i)) + '.npz')


