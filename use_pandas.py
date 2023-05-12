import pandas as pd

df = pd.read_csv('csv.csv')
# use print for datastream to an object/ console
# use display to print to an DOM element
# https://docs.pyscript.net/latest/reference/API/display.html
display(df, target="display_output")
