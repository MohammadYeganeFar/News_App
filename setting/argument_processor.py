import os
import argparse
from dotenv import load_dotenv
from setting.constants import (
SUPPORTED_LANGS,
SUPPORTED_CATEGORIES,
SORTING_CHOICES,
SEARCH_IN_CHOICES,
ENDPOINT_CHOICES,
EVERYTHING_URL,
TOP_HEADLINES_URL
)

# valid_date = "(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2})"

# loading environments
load_dotenv()
api_key = os.getenv("NEWS_API")


class Argument:
    def __init__(self):
        self.namespace_args = self.setup_args()
        self.dict_args = self.get_dict_args()
        self.raw_url = self.get_url_and_endpoint()

    @staticmethod
    def setup_args():
        """
        adding args to parser

        :return:
            args: Namespace
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("-E","--endpoint",
                            default='everything',
                            choices= ENDPOINT_CHOICES,
                            type=str)

        parser.add_argument("--q",
                            required=True)

        parser.add_argument('-p',
                            '--pageSize',
                            default=5,
                            type=int)

        parser.add_argument("-l",
                            "--language",
                            choices=SUPPORTED_LANGS,
                            default="")

        parser.add_argument("-a",
                            "--page",
                            type=int,
                            default=1)

        parser.add_argument("-f",
                            "--from_date",
                            default="")

        parser.add_argument("--to",
                            default="")

        parser.add_argument("-s",
                            "--searchIn",
                            choices=SEARCH_IN_CHOICES,
                            default="")

        parser.add_argument("-o",
                            "--sortBy",
                            default='relevancy',
                            choices=SORTING_CHOICES)

        parser.add_argument("-d",
                            "--domains",
                            default="")


        parser.add_argument("-x",
                            "--excludeDomains",
                            default="")

        parser.add_argument("-y",
                            "--country",
                            choices=["us",],
                            default="us")


        parser.add_argument("-c",
                            "--category",
                            choices=SUPPORTED_CATEGORIES,
                            default="")

        parser.add_argument("-r",
                            "--sources",
                            default="")

        args = parser.parse_args()

        return args


    def get_dict_args(self):
        """
        Since Namespace objects are not iterable and subscriptable,
        I created this method to make user args iterable and subscriptable.
        
        :return: 
            dict[str:str]
        """
        if self.namespace_args.endpoint == "everything":
            dict_args = {
                'apiKey': api_key,
                'q': self.namespace_args.q,
                'searchIn': self.namespace_args.searchIn,
                'sources': self.namespace_args.sources,
                'domains': self.namespace_args.domains,
                'excludeDomains': self.namespace_args.excludeDomains,
                'from': self.namespace_args.from_date,
                'to': self.namespace_args.to,
                'language': self.namespace_args.language,
                'sortBy': self.namespace_args.sortBy,
                'pageSize': self.namespace_args.pageSize,
                'page': self.namespace_args.page,
            }


        elif self.namespace_args.endpoint == "top-headlines":
            dict_args = {
                'apiKey': api_key,
                'q': self.namespace_args.q,
                'sources': self.namespace_args.sources,
                'category': self.namespace_args.category,
                'country': self.namespace_args.country,
                'pageSize': self.namespace_args.pageSize,
                'page': self.namespace_args.page,
            }

        return dict_args


    def get_url_and_endpoint(self):
        if self.namespace_args.endpoint == "everything":
            return EVERYTHING_URL

        elif self.namespace_args.endpoint == "top-headlines":
            return TOP_HEADLINES_URL

        return None



