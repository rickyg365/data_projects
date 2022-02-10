import pandas as pd

""" 
Storage for pandas or other data cleaning or utility functions
"""


def summarize_data(raw_data:pd.DataFrame) -> str:
    col_text = ""
    for item in raw_data.columns:
        col_text += f" => {item}\n"

    output_summary = f"""[ Overview ]:

{raw_data.head()}


[ Statistics ]:

{raw_data.describe()}


[ First Row ]:

{raw_data.iloc[0]}


[ Columns ]:

{col_text}
"""
    return output_summary