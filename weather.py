import pandas as pd
from matplotlib import pyplot as plt
# js library allows python to access Javascript functions
# js.document.getElementById("selectet_year").innerHTML = choice
import js
# create_proxy allowing javascript to call PyScript functions
# js_function_name = create_proxy(python_function_name)
from pyodide.ffi import create_proxy
from pyodide.http import open_url


url = 'https://raw.githubusercontent.com/alanjones2/uk-historical-weather/main/data/Heathrow.csv'
url_content = open_url(url)
df = pd.read_csv(url_content)
df = df[df['Year'] == 2020]


# function to plot the chart
def plot(condition):
    fig, ax = plt.subplots()
    df.plot(y=condition, x='Month', figsize=(8, 4), ax=ax)
    pyscript.write("chart0", fig)


def python_function_name(event):
    """
    This function is called when a change event occurs.
    It reads the value of the selection and then calls the
    previously defined plot function with that value.
    :param event:
    """
    choice = js.document.getElementById("select").value
    js.document.getElementById("selected_condition").innerHTML = choice
    plot(choice)


# set the proxy
def setup():
    # Create a JsProxy for the callback function
    # create_proxy from pyodide allowing javascript to call python functions
    js_function_name = create_proxy(python_function_name)
    dropdown_element = js.document.getElementById("select")
    dropdown_element.addEventListener("change", js_function_name)


setup()

# Intitially call plot with 'Tmax'
plot('Tmax')
