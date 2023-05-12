## py-script starter file

The index.html file in this repo contains py-script stuff so that you can run python code in the browser.
    Use the file to understand the basics and as a template file for your own protects.

Project Link: [https://github.com/Ma-Schwa/py-script_starter-file](https://github.com/Ma-Schwa/py-script_starter-file)
## Usage

```console
git clone https://github.com/Ma-Schwa/py-script_starter-file.git
```
As described in that post
[https://blog.logrocket.com/pyscript-run-python-browser/#opening-index-html-file-browser](https://blog.logrocket.com/pyscript-run-python-browser/#opening-index-html-file-browser) 
browsers will refuse to load and execute the external Python file due to the Cross-Origin Resource Sharing (CORS) policy error.
To properly load the html file with python running you need to start a server by
```python
python -m http.server
```
Then go to your browser and visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) (or whatever your port is). This automatically loads the index.html file.
