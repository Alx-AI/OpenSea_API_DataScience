from helpers import parse_assets_data, parse_sale_data, parse_listing_data
from datetime import date, timedelta, datetime

import numpy as np
import requests
import time
import os
import glob


# load most recent saved version of assets
def load_assets_info(save_location, asset_name="animeta"):
    files = glob.glob(str(save_location) + asset_name + '_list' + '????-??-??.npz')
    listofassets = np.load(max(files, key=os.path.getctime), allow_pickle=True)['arr_0']
    return listofassets


# load all events lists & combine them
def load_events_info(save_location):
    files = [filename for filename in os.listdir(save_location) if filename.startswith('assets_events')]
    all_events = []
    # load all files for events by day
    for file in files:
        all_events.append(np.load(str(save_location) + str(file), allow_pickle=True)['arr_0'])

    # flatten into one list
    all_events = [item for sublist in all_events for item in sublist]

    return all_events
