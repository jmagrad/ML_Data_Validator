import pandas as pd
from typing import Dict, Any

def validate_data(df: pd.DataFrame) -> Dict[str, Any]:
    results = {}

    results['inferred_schema'] = df.dtypes.apply(lambda x: str(x)).to_dict()

    results['missing_values'] = df.isnull().sum().to_dict()

    results['unique_counts'] = df.nunique().to_dict()

    results['numerical_summary'] = df.describe(include='number').to_dict()

    return results
