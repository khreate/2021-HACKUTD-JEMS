from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError

try:
    api = Finding(appid="SurajKho-hackutd-PRD-cdc74433e-5e966209", config_file=None)
    response = api.execute('findItemsAdvanced', {'keywords': 'toilet paper'})
    c = (response.dict()['searchResult']['item'])
    result_array = []
    result_cost = []
    result_images = []
    result_link = []
    for item in range(10):
        result_array.append(c[item]['title'])
        result_images.append(c[item]['galleryURL'])
        result_cost.append(c[item]['sellingStatus']['currentPrice']['value'])
        result_link.append(c[item]['viewItemURL'])
    print(result_array)
    print(result_cost)
    print(result_images)
    print(result_link)
except ConnectionError as e:
    print(e)
    print(e.response.dict())



