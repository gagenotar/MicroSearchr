import logging

import openai
import os
from dotenv import load_dotenv
from schemas.openai_responses import *


class SearchrClient:
    """A client class for interacting with the serper.dev API."""

    def __init__(self, api_key):
        self.serper_api_key = api_key

    @staticmethod
    def lookup(query: str):
        try:
            # make API call to serper.dev

            # we want to extract the response into a model from the 'schema' module:
            # The module will contain only the fields we care about, and ignore any other fields from
            # the response.

            # we then return the model we created
            pass
        except Exception as e:
            logging.error(e)
            raise Exception("Failed to call Serper API")


def get_searchr_client():
    load_dotenv()
    return SearchrClient(os.getenv("SERPER_API_KEY"))


if __name__ == "__main__":
    client = get_searchr_client()
    print(client.lookup("banana hammock"))
