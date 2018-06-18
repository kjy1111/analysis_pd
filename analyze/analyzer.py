import  json
import re
from konlpy.tag import Twitter
from collections import Counter


def json_to_str(filename, key):
    with open(filename, 'r', encoding='utf-8') as infile:
        json_string = infile.read()
        infile.close()

        data = ''
        json_data = json.loads(json_string)
        for item in json_data:
            value = item.get(key)
            if value is None:
                continue