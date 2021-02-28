from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError


def ebay_title(keyword):
    try:
        api = Finding(appid="SurajKho-hackutd-PRD-cdc74433e-5e966209", config_file=None)
        response = api.execute('findItemsAdvanced', {'keywords': 'toilet paper'})
        c = (response.dict()['searchResult']['item'])
        result_array = []
        for item in range(10):
            result_array.append(c[item]['title'])
    except ConnectionError as e:
        print(e)
        print(e.response.dict())
    return result_array


def ebay_cost(keyword):
    try:
        api = Finding(appid="SurajKho-hackutd-PRD-cdc74433e-5e966209", config_file=None)
        response = api.execute('findItemsAdvanced', {'keywords': 'toilet paper'})
        c = (response.dict()['searchResult']['item'])
        result_cost = []
        for item in range(10):
            result_cost.append(c[item]['sellingStatus']['currentPrice']['value'])
    except ConnectionError as e:
        print(e)
        print(e.response.dict())
    return result_cost


def ebay_image(keyword):
    try:
        api = Finding(appid="SurajKho-hackutd-PRD-cdc74433e-5e966209", config_file=None)
        response = api.execute('findItemsAdvanced', {'keywords': 'toilet paper'})
        c = (response.dict()['searchResult']['item'])
        result_images = []
        for item in range(10):
            result_images.append(c[item]['galleryURL'])
    except ConnectionError as e:
        print(e)
        print(e.response.dict())
    return result_images


def ebay_link(keyword):
    try:
        api = Finding(appid="SurajKho-hackutd-PRD-cdc74433e-5e966209", config_file=None)
        response = api.execute('findItemsAdvanced', {'keywords': 'toilet paper'})
        c = (response.dict()['searchResult']['item'])
        result_link = []
        for item in range(10):
            result_link.append(c[item]['viewItemURL'])
    except ConnectionError as e:
        print(e)
        print(e.response.dict())
    return result_link



