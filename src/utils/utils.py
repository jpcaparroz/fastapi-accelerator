import os
import json

from typing import Literal

CONFIG_PATH = f'{os.getcwd()}\src\config\config.json'

def get_config(section: Literal['server', 'database']) -> dict:
    with open(CONFIG_PATH) as op:
        config = json.load(op)

    return config.get(section)

