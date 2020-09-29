import requests
import json


def store_document(url, document):
    """
    Stores a document in the database

    :param url: the base url of the REST server
    :param document: document string
    :returns response.text: document_id is returned if successful
    """
    url += "/documents"
    headers = {"Content-Type": "application/json"}
    data = {"text": document}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        # dataset_id = response.json()["data"][0]["id"]
        return response.text
    elif response.status_code == 400:
        return "It is a bad bad request!"
    elif response.status_code == 401:
        return "Unauthorized! You shall not pass!! Please check the API token"
    elif response.status_code == 404:
        return "Not Found"
    else:
        return response.text


def retrieve(url):
    """
    Retrieve a document or it's summary from the database

    :param url: the base url of the REST server + document or summary
    :returns response.text: document or it's summary is returned if successful
    """
    response = requests.get(url)

    if response.status_code == 200:
        return json.loads(response.text)
    elif response.status_code == 404:
        return "Not Found"
    else:
        return response.status_code


def retrieve_document(url, document_id):
    """
    Wrapper around retrieve function

    :param url: the base url of the REST server
    :param document_id: document id to be retrieved
    :returns response.text: document is returned if successful
    """
    url += "/documents/" + document_id
    return retrieve(url)


def retrieve_summary(url, document_id):
    """
    Wrapper around retrieve function

    :param url: the base url of the REST server
    :param document_id: document id to be retrieved
    :returns response.text: summary of the document is returned if successful
    """
    url += "/summary/" + document_id
    return retrieve(url)

def delete_document(url, document_id):
    """
    Wrapper around retrieve function

    :param url: the base url of the REST server
    :param document_id: document id to be deleted
    :returns response.status_code: status code of the request
    """
    url += "/documents/" + document_id
    response = requests.delete(url)
    return response.status_code