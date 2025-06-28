from pipeline import validate_data
from utils import load_json_file

if __name__ == "__main__":
    df = load_json_file("data/data.json")
    report = validate_data(df)
    from pprint import pprint
    pprint(report)
