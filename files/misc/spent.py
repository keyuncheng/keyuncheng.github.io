import pandas as pd
import numpy as np
import sys

col_map = {
    "Mandatory": ["Tuition","Dorm", "Insurance", "CMHK"],
    "Subscriptions": ["Subscription"],
    "Eat": ["Take-away", "Eat"],
    "Cash": ["Cash", "Octopus"],
    "E-shop": ["E-shop"],
    "Misc": ["Misc"]
}

col_idx = "Time"
col_income = "Income"


def convert_column(column):
    if (type(column) == list):
        if (len(column) > 0):
            column = sum(column)
        else:
            column = 0
    
    if (type(column) != type(u'')):
        column = float(column)
    else:
        column = str(column)

    # print(column, type(column))

    return column

def main(argv):
    pd.set_option('display.expand_frame_repr', False)
    df = pd.read_json(argv[1])

    column_names_unicode = df.columns.values
    column_names = map(lambda x: str(x), column_names_unicode)
    column_names_spent = [ col for col in df.columns if col != col_idx and col != col_income ]

    df.rename(dict(zip(column_names_unicode, column_names)))

    df = df.applymap(convert_column)

    df = df[[col_idx] + column_names_spent + [col_income]]

    summary = pd.DataFrame()

    summary[col_idx] = df[col_idx]
    summary[col_income] = df[col_income]
    summary["All"] = df[column_names_spent].sum(axis=1)
    summary["Remain"] = summary[col_income] - summary["All"]
    for col_name, cols in col_map.items():
        summary[col_name] = df[cols].sum(axis=1)

    print(df)
    print(summary)
    print("Income: {}".format(summary["Remain"].sum(axis=0)))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: {} filename".format(sys.argv[0]))

    print(sys.argv)
    main(sys.argv)

