import os

import json

import numpy as np
import pandas as pd

from rich import tree

from utils.clean_data import summarize_data


"""

"""


def main():
    # Read in Data from file
    filename = "data/anime.csv"
    
    raw_anime_data = pd.read_csv(filename)

    # Create Data Summary
    data_summary = summarize_data(raw_anime_data)

    print(data_summary)  # Display Summary

    # Save Summary
    with open("data/summary.txt", 'w') as out_file:
        out_file.write(data_summary)  
    

if __name__ == "__main__":
    main()
