import pandas as pd

# -------------- Series func() -------------

# -------- :Series from a list: ---------

a = [1,3,5,7]

# df = pd.Series(a)  # Series is like a column in a table

# print(df)

# df = pd.Series(a, index=['a','b','c','d'])   #  name your own labels
# print(df)

# print(df['c'])  # access an item by referring to the label


# -------- :Series from a dictonary: ---------

workout = {'day 1' : 'Chest', 'day 2' : 'Arm', 'day 3' : 'Back', 'day 4' : 'Leg', 'day 5' : 'Abs'}

# df = pd.Series(workout)

# df = pd.Series(workout, index=['day 1', 'day 5'])  # specify only the items you want to include in the Series.

# print(df)

# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

# -------------- DataFrame func() --------------

data = {
    'Day' : ['day 1', 'day 2', 'day 3', 'day 4', 'day 5'],
    'Workout': ['chest', 'arm', 'back', 'leg', 'abs']
    }

# df = pd.DataFrame(data)  #  Series is like a column, a DataFrame is the whole table.

df = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])  # give name to indexes

# print(df)


#  --------> loc attribute: 

# print(df.loc[1])   # return one or more specified row(s)
# print(df.loc[[0,1]])  # for multiple values use double brackest [[]]

# print(df.loc[['d', 'e']])  # Use the named index in the loc attribute to return the specified row(s)

# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------


# ----------- Read CSV file -------------

# --------> With to_string()

df = pd.read_csv('data.csv')
# print(df.to_string())    #  use to_string() to print the entire dataframe

# --------> Without to_string()

# print(df)


# ----------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------


# ----------- Read json file -------------

df_2 = pd.read_json('data.json')
# print(df_2)


# ----------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------


# ----------- Analyzing DataFrame -------------

# ----------> head()

# print(df.head())   # Print the first 5 rows of the DataFrame
# print(df.head(10)) # printing the first 10 rows of the DataFrame


# ----------> tail()

# print(df.tail())   # Print the last 5 rows of the DataFrame


# ----------> info()

# print(df.info())   # Print information about the data