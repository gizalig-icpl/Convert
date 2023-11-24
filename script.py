import pandas as pd
import json
import os
import argparse

def main(json_file_name):
    base_name = os.path.splitext(os.path.basename(json_file_name))[0]

    with open(json_file_name, 'r') as json_file:
        data = json.load(json_file)

    df = pd.json_normalize(data)

    excel_file_name = f'{base_name}.xlsx'
    df.to_excel(excel_file_name, index=False)
    print(f'Data has been saved to {excel_file_name}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert JSON to Excel')

    parser.add_argument('json_file', type=str, help='Path to the JSON file')

    args = parser.parse_args()

    main(args.json_file)
