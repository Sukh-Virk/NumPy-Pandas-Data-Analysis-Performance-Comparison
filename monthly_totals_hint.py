import numpy as np
import pandas as pd


def get_precip_data():
    try:
        data = pd.read_csv('precipitation.csv', parse_dates=[2])
        print("Data loaded successfully!")  # Confirm that the data is loaded
        return data
    except FileNotFoundError:
        print("Error: 'precipitation.csv' file not found.")
        return pd.DataFrame()  # Return an empty DataFrame if the file is missing


def date_to_month(d):
    # You may need to modify this function, depending on your data types.
    return '%04i-%02i' % (d.year, d.month)


def pivot_months_pandas(data):
    """
    Create monthly precipitation totals for each station in the data set using Pandas methods.
    """
    # Add a 'month' column based on the date column
    data['month'] = data['date'].apply(date_to_month)

    # Group by 'name' and 'month', then aggregate using sum for totals and count for observations
    grouped_data = data.groupby(['name', 'month']).agg({'precipitation': 'sum', 'date': 'count'}).reset_index()

    # Pivot the data to create rows for each station and columns for each month
    monthly_totals = grouped_data.pivot(index='name', columns='month', values='precipitation')
    monthly_counts = grouped_data.pivot(index='name', columns='month', values='date')

    # Print the head of the DataFrames to confirm data is processed correctly
    print("Monthly totals:\n", monthly_totals.head())
    print("Monthly counts:\n", monthly_counts.head())

    return monthly_totals, monthly_counts


def pivot_months_loops(data):
    """
    Create monthly precipitation totals for each station in the data set using loops.
    This method is already written and does not need changes for this task.
    """
    # Find all stations and months in the data set.
    stations = set()
    months = set()
    for _, r in data.iterrows():
        stations.add(r['name'])
        m = date_to_month(r['date'])
        months.add(m)

    # Aggregate into dictionaries so we can look up later.
    stations = sorted(list(stations))
    row_to_station = dict(enumerate(stations))
    station_to_row = {s: i for i, s in row_to_station.items()}
    
    months = sorted(list(months))
    col_to_month = dict(enumerate(months))
    month_to_col = {m: i for i, m in col_to_month.items()}

    # Create arrays for the data, and fill them.
    precip_total = np.zeros((len(row_to_station), 12), dtype=np.uint)
    obs_count = np.zeros((len(row_to_station), 12), dtype=np.uint)

    for _, row in data.iterrows():
        m = date_to_month(row['date'])
        r = station_to_row[row['name']]
        c = month_to_col[m]

        precip_total[r, c] += row['precipitation']
        obs_count[r, c] += 1

    # Build the DataFrames we needed all along (tidying up the index names while we're at it).
    totals = pd.DataFrame(
        data=precip_total,
        index=stations,
        columns=months,
    )
    totals.index.name = 'name'
    totals.columns.name = 'month'
    
    counts = pd.DataFrame(
        data=obs_count,
        index=stations,
        columns=months,
    )
    counts.index.name = 'name'
    counts.columns.name = 'month'
    
    return totals, counts


def main():
    print("Starting the processing of precipitation data...")
    data = get_precip_data()
    
    if data.empty:
        print("No data available to process.")
        return

    # Use the pivot_months_pandas function to process the data using Pandas methods
    totals, counts = pivot_months_pandas(data)
    
    # Save the results to CSV and NPZ files
    totals.to_csv('totals.csv')
    counts.to_csv('counts.csv')
    np.savez('monthdata.npz', totals=totals.values, counts=counts.values)
    
    print("Processing complete. Files 'totals.csv', 'counts.csv', and 'monthdata.npz' have been saved.")


if __name__ == '__main__':
    main()
