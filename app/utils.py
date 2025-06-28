import pandas as pd
from typing import Union
import json

def load_json_file(filepath: str) -> pd.DataFrame:
    return pd.read_json(filepath)
