import requests


def store_document(url, document):
    url += "/documents"
    headers = {"Content-Type": "application/json"}
    data = {"text": document}

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 201:
        # dataset_id = response.json()["data"][0]["id"]
        print(response.text)
        return response.text
    elif response.status_code == 401:
        return "Unauthorized! You shall not pass!! Please check the API token"
    elif response.status_code == 404:
        return "Not Found"
    else:
        return response.text


def retrieve(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    elif response.status_code == 404:
        return "Not Found"
    else:
        return response.status_code


def retrieve_document(url, document_id):
    url += "/documents/" + document_id
    return retrieve(url)


def retrieve_summary(url, document_id):
    url += "/summary/" + document_id
    return retrieve(url)
