An application that print out 10 of the best restaurants in Pardes Hana - Karkur.
Using Flask, SerpAPI and HTML.

Full DevLog -
https://docs.google.com/document/d/1mkcwvSBSLPz9QdM4lPZAQP8IseL-r2E9XegbkxCUXSc/edit?usp=sharing

Requierements (Docker):
Docker installed and running
A terminal window/CMD

How to run:
1. Run "docker pull ghcr.io/weare2car2/idf-test-project:nightly"
2. Wait for the image to be downloaded.
3. After finished, run "docker run -p 5000:5000 ghcr.io/weare2car2/idf-test-project:nightly"
4. Go to "http://127.0.0.1:5000"


Requierements (Non-Docker)
Python 3+
Run:
1. "pip install serpapi"
2. "pip install flask"
3. "pip install pytest"
4. "pip install python-dotenv"

How to run:
1. Get the code by pulling it/downloading it
2. run "python app.py"
