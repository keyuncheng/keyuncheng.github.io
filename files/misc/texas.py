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
col_profit = "Profit"


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
    # column_names_spent = [ col for col in df.columns if col != col_idx and col != col_profit ]

    df.rename(dict(zip(column_names_unicode, column_names)))

    df = df.applymap(convert_column)

    # convert date time
    df[col_idx] = pd.to_datetime(df[col_idx], format='%Y-%m-%d')



    # df = df[[col_idx] + column_names_spent + [col_profit]]

    summary = pd.DataFrame()

    summary[col_idx] = df[col_idx]
    summary[col_profit] = df[col_profit]
    # summary["All"] = df[column_names_spent].sum(axis=1)
    # summary["Remain"] = summary[col_profit] - summary["All"]
    # for col_name, cols in col_map.items():
    #     summary[col_name] = df[cols].sum(axis=1)

    # print(df)
    # print(summary)

    # year summary
    for year in range(2021, 2025):
        df_time = df[(df[col_idx] >= "{}-01-01".format(year)) & (df[col_idx] <= "{}-12-31".format(year))]

        print(df_time)
        print("Income ({} to {}): {}".format(df_time.iloc[0][col_idx], df_time.iloc[-1][col_idx], df_time[col_profit].sum(axis=0)))

    summary_plot = pd.Series(summary[col_profit].values, index=summary[col_idx])
    summary_plot = summary_plot.cumsum()
    fig = summary_plot.plot(marker='o').get_figure()
    fig.savefig("texas_summary.png")

    print("Income (total): {}".format(summary[col_profit].sum(axis=0)))    
    # print("Income: {}".format(summary["Remain"].sum(axis=0)))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: {} filename".format(sys.argv[0]))

    print(sys.argv)
    main(sys.argv)

