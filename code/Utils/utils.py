#######################################
#   Useful Functions                  #
#######################################

# Function to rename a column by position
def rename_column_by_position(df, position, new_name):
    if 0 <= position < len(df.columns):
        columns = df.columns.tolist()
        columns[position] = new_name
        df.columns = columns
    else:
        raise ValueError(f"Invalid position. DataFrame has {len(df.columns)} columns.")

# Drop specified columns from a DataFrame.
def drop_columns(df, columns_to_drop):
    return df.drop(columns=columns_to_drop)        

# Reads a CSV file from the given URL and returns a pandas DataFrame.
def read_csv_to_dataframe(csv_url):
    return pd.read_csv(csv_url)    

# Reads a CSV file from the given URL and returns a pandas DataFrame including features.
def read_csv_to_dataframe_w_features(csv_url, features):
    return pd.read_csv(csv_url, features=feature_names)    

# Print the shape of the DataFrame
def print_shape(df):
  print('----------------------------')
  print('Shape')
  print('----------------------------')
  print(df.shape)
  rows, columns = df.shape
  print(f"DataFrame has {rows} rows and {columns} columns")

# Print some summary statistics of the DataFrame
def print_statistics(df):
  print('----------------------------')
  print('statistics')
  print('----------------------------')
  print(df.describe())

# Print the list of columns in the CSV file.
def print_columns(df):
  print('----------------------------')
  print('Columns')
  print('----------------------------')
  print(df.columns)  

# Print the first five rows of the DataFrame
def print_head(df):
  print('----------------------------')
  print('First 5 rows')
  print('----------------------------')
  print(df.head())  
