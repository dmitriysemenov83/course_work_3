from functions import get_data, filtered_data, date_and_data_formatting

data = get_data()
operations = filtered_data(data)
date_and_data_formatting(operations)