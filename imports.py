from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import json
import csv
import re
import itertools
import numpy as np
import pandas as pd
pd.set_option('display.max_rows', None)

def flatten(xss):
    return [x for xs in xss for x in xs]

def json_print(data):
    print(json.dumps(data, indent=2, ensure_ascii=False))
  
