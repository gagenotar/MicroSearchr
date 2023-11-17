import logging

import os
from dotenv import load_dotenv
from schemas.openai_responses import *
from schemas.serper_responses import *
import requests
import json


class SearchrClient:
    """A client class for interacting with the serper.dev API."""

    # Not sure if this is even necessary. I have not found the code to access the
    # API key like you did in the openAI client.
    def __init__(self, api_key):
        os.environ["SERPER_API_KEY"] = api_key

    @staticmethod
    def lookup(query: str):
        try:
            url = "https://google.serper.dev/search"

            payload = json.dumps({
            "q": query
            })

            # Below is where the API key is supposed to be accessed.
            # I can't figure out how to assign it my .env variable.
            headers = {
            'X-API-KEY': 'API_KEY_GOES_HERE',
            'Content-Type': 'application/json'
            }
            # make API call to serper.dev
            response = requests.request("POST", url, headers=headers, data=payload)

            # we want to extract the response into a model from the 'schema' module:
            # The model will contain only the fields we care about, and ignore any other fields from
            # the response.
            search_response = SerperResponse(**json.loads(response.text))

            # we then return the model we created
            return search_response
        except Exception as e:
            logging.error(e)
            raise Exception("Failed to call Serper API")


def get_searchr_client():
    load_dotenv()
    return SearchrClient(os.getenv("SERPER_API_KEY"))


if __name__ == "__main__":
    client = get_searchr_client()
    response = client.lookup("hammock")
    print(response.organic)
