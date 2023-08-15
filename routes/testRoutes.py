from typing import Optional
from models.TestModels import Test
from fastapi import FastAPI

# import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return {"User": "Izaiah"}


@app.get("/api/{id}")
def test(id: int):
    return {"id": id}


# Handling query params
@app.get("/Qparams")
# In the URL type http://127.0.0.1:8000/Qparams?params=yellow&paramtwo=True
def test(params="beans", paramtwo: bool = True, sort_param: Optional[str] = None):
    if paramtwo:
        return {
            "data": f"These are the params, we can do something with them..{params}"
        }  # params will be "yellow"
    else:
        return {"data": "Your second param was false my guy"}


@app.post("/api")
def trialy(test: Test):
    return {"user": test.username}
