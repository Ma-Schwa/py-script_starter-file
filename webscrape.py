import requests
import pyodide_http
import json
# Patch the Requests library so it works with Pyscript
pyodide_http.patch_all()

# Make a request to the JSON Placeholder API
res = requests.get("https://jsonplaceholder.typicode.com/todos")
display("json from https://jsonplaceholder.typicode.com/todos\n\n", target="json_out")
display(json.dumps(res.json()[0:3], indent=4), target="json_out")


res2 = requests.get('https://raw.githubusercontent.com/pyscript/pyscript/main/MAINTAINERS.md')
display("\n text from https://raw.githubusercontent.com/pyscript/pyscript/main/MAINTAINERS.md\n", target="text_out")
display(res2.text, target="text_out")

