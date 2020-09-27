import requests

def get_data(url, api_key, ):

    payload = {"api_key": api_key}

    complete_data = []
    page = 1
    total_pages=1
    while page <= total_pages:
        response = requests.request("GET", url, params=payload)
        data = response.json()
        page = data["page"]
        total_pages = data["total_pages"] - 1
        payload["page"] = page + 1
        complete_data = complete_data + data["results"]

    return complete_data

