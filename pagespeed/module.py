import requests

from pagespeed.settings import GOOGLE_API_KEY, GOOGLE_PAGESPEED_URL


def get_results(input_url):
    api_key = GOOGLE_API_KEY
    test_url = GOOGLE_PAGESPEED_URL
    payload = {'url': input_url, 'key': api_key}

    r = requests.get(test_url, params=payload)
    json = r.json()
    results = json["ruleGroups"]["SPEED"]["score"]
    return results