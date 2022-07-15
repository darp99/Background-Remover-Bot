from fastapi import FastAPI
from fastapi.responses import FileResponse
from rembg import remove
import requests
from PIL import Image


app = FastAPI()
@app.get("/u")
def hello(param1: str,response_class=FileResponse):
  print(param1)
  response = requests.get(param1)

  with open("demo.jpg", "wb") as f:
      f.write(response.content)

  input_path = 'demo.jpg'
  output_path = 'output.png'
  input = Image.open(input_path)
  output = remove(input)
  output.save(output_path)
  return FileResponse(output_path)


