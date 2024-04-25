import weaviate, os
from weaviate.embedded import EmbeddedOptions
from weaviate.classes.query import MetadataQuery, Filter, GeoCoordinate

import openai
from dotenv import load_dotenv, find_dotenv

def json_print(data):
    print(json.dumps(data, indent=2, ensure_ascii=False))
  
