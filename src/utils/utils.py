import os
import json

from typing import Literal
from typing import Union


CONFIG_PATH = f'{os.getcwd()}\src\config\config.json'


def get_config(section: Literal['server', 'database', 'security'], 
               key: str = None) -> Union[dict, str]:
    result: str
    
    with open(CONFIG_PATH) as op:
        config = json.load(op)

    if not key:
        result = config.get(section)
    else:
        result = config.get(section).get(key)
        
    return result

