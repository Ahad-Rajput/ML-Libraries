import pandas as pd

df = pd.read_csv('data.csv')

# print(df.to_string())

"""
data.csv:-

     Duration          Date  Pulse  Maxpulse  Calories
  0         60  '2020/12/01'    110       130     409.1
  1         60  '2020/12/02'    117       145     479.0
  2         60  '2020/12/03'    103       135     340.0
  3         45  '2020/12/04'    109       175     282.4
  4         45  '2020/12/05'    117       148     406.0
  5         60  '2020/12/06'    102       127     300.0
  6         60  '2020/12/07'    110       136     374.0
  7        450  '2020/12/08'    104       134     253.3
  8         30  '2020/12/09'    109       133     195.1
  9         60  '2020/12/10'     98       124     269.0
  10        60  '2020/12/11'    103       147     329.3
  11        60  '2020/12/12'    100       120     250.7
  12        60  '2020/12/12'    100       120     250.7
  13        60  '2020/12/13'    106       128     345.3
  14        60  '2020/12/14'    104       132     379.3
  15        60  '2020/12/15'     98       123     275.0
  16        60  '2020/12/16'     98       120     215.2
  17        60  '2020/12/17'    100       120     300.0
  18        45  '2020/12/18'     90       112       NaN
  19        60  '2020/12/19'    103       123     323.0
  20        45  '2020/12/20'     97       125     243.0
  21        60  '2020/12/21'    108       131     364.2
  22        45           NaN    100       119     282.0
  23        60  '2020/12/23'    130       101     300.0
  24        45  '2020/12/24'    105       132     246.0
  25        60  '2020/12/25'    102       126     334.5
  26        60    2020/12/26    100       120     250.0
  27        60  '2020/12/27'     92       118     241.0
  28        60  '2020/12/28'    103       132       NaN
  29        60  '2020/12/29'    100       132     280.0
  30        60  '2020/12/30'    102       129     380.3
  31        60  '2020/12/31'     92       115     243.0

The data set contains some empty cells ("Date" in row 22, and "Calories" in row 18 and 28).

The data set contains wrong format ("Date" in row 26).

The data set contains wrong data ("Duration" in row 7).

The data set contains duplicates (row 11 and 12).
"""

# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------- Cleaning Empty Cells ---------------------------------------

# -----------> Remove Rows

"""
One way to deal with empty cells is to remove rows that contain empty cells.

This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
"""

new_df = df.dropna()

# print(new_df.to_string())

"""
By default, the dropna() method returns a new DataFrame, and will not change the original.
If you want to change the original DataFrame, use the inplace = True argument.
"""

# df.dropna(inplace = True)

# print(df.to_string())


# -------------> Replace Empty Values

"""
Another way of dealing with empty cells is to insert a new value instead.

This way you do not have to delete entire rows just because of some empty cells.
"""

# df.fillna({"Date" : "Unknown", "Calories" : 130}, inplace = True)

# print(df.to_string())   # Notice in the result: empty cells got the value 130 (in row 18, 22 and 28).


# -------------> Replace Using Mean, Median, or Mode

# ------> Mean:
"""
Mean = the average value (the sum of all values divided by number of values).
"""
x = df["Calories"].mean()

# Calculate the MEAN, and replace any empty values with it

df.fillna({"Calories": x}, inplace=True)  

# print(df.to_string())  # In row 18 and 28, the empty values from "Calories" was replaced with the mean: 304.68

# ------> Median:
"""
Median = the value in the middle, after you have sorted all values ascending.
"""

x = df["Calories"].median()

df.fillna({"Calories": x}, inplace=True)

# print(df.to_string())  # In row 18 and 28, the empty values from "Calories" was replaced with the median: 291.2

# --------> Mode:
"""
Mode = the value that appears most frequently.
"""

x = df["Calories"].mode()[0]

df.fillna({"Calories": x}, inplace=True)

# print(df.to_string())  # In row 18 and 28, the empty value from "Calories" was replaced with the mode: 300.0


# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------- Cleaning Data of Wrong Format ---------------------------------------

"""
Cells with data of wrong format can make it difficult, or even impossible, to analyze data.

To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.

In our DataFrame, we have two cells with the wrong format. For row 22 and 26, the 'Date' column should be a string that represents a date
"""

df['Date'] = pd.to_datetime(df["Date"], format='mixed')
# print(df.to_string())

"""
As you can see from the result, the date in row 26 was fixed, but the empty date in row 22 got a NaT (Not a Time) value, in other words an empty value. One way to deal with empty values is simply removing the entire row and we can remove the row by using the dropna() method.

"""


# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------- Fixing Wrong Data ---------------------------------------

# ----------> Replacing Values:

df.loc[7,'Duration'] = 45   # Set "Duration" = 45 in row 7
# print(df.to_string())

"""
For small data sets you might be able to replace the wrong data one by one, but not for big data sets.

To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.
"""

for x in df.index:   # Loop through all values in the "Duration" column. If the value is higher than 60, set it to 60:
    if df.loc[x,'Duration'] > 60: df.loc[x,'Duration'] = 60

# print(df.to_string())
    

# ----------> Replacing Values:
"""
Another way of handling wrong data is to remove the rows that contains wrong data.

This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.
"""

for x in df.index:
    if df.loc[x, 'Duration'] > 60: df.drop(x, inplace=True)   # Delete rows where "Duration" is higher than 60

# print(df.to_string())


# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------- Removing Duplicates ---------------------------------------

# ----------> Discovering Duplicates:
"""
To discover duplicates, we can use the duplicated() method.

The duplicated() method returns a Boolean values for each row
"""

# print(df.duplicated())  # row 11 and 12 are duplicates.


# ----------> Removing Duplicates:

df.drop_duplicates(inplace=True)

print(df.to_string())
