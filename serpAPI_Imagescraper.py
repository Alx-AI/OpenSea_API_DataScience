import os, urllib.request, json  # json for pretty output
from serpapi import GoogleSearch


def get_google_images():
    params = {
        "api_key": os.environ.get("SERPAPI_KEY"),
        "engine": "google",
        "q": "Cat",
        "tbm": "isch",
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    # print(json.dumps(results['suggested_searches'], indent=2, ensure_ascii=False))
    print(json.dumps(results["images_results"], indent=2, ensure_ascii=False))
    # save files to /SerpApi_Images/ if it doesn't exist create the folder
    if not os.path.exists("./SerpApi_Images/"):
        os.makedirs("./SerpApi_Images/")

    # -----------------------
    # Downloading images

    for index, image in enumerate(results["images_results"]):

        print(f"Downloading {index} image...")

        opener = urllib.request.build_opener()
        opener.addheaders = [
            (
                "User-Agent",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582",
            )
        ]
        urllib.request.install_opener(opener)
        # filepath is current working directory + SerpApi_Images + params["q"] + index + .jpg
        filepath = os.path.join("./SerpApi_Images/", params["q"] + str(index) + ".jpg")

        urllib.request.urlretrieve(image["original"], filepath)


get_google_images()
