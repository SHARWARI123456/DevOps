from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
app = FastAPI()

@app.get('/')
def index():
    return {'hello': 'world123'}

@app.get('/alert', response_class=HTMLResponse)
def read_root():
    return '<script>alert("This is JavaScript")</script>'

@app.get('/amazon', response_class=RedirectResponse)
def redirect():
    return 'https://www.amazon.com'
