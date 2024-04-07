from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get('/', response_class=FileResponse)
async def root():
    return 'index.html'

@app.post('/calculate')
async def root(num1, num2):
    sum = int(num1) + int(num2)
    return {'result': sum}