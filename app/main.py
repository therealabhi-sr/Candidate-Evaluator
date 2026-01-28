from fastapi import FastAPI,Query,Path
from pydantic import BaseModel,Field

app=FastAPI()

reg_nos=[1234,45678,8901]

class InputAccept(BaseModel):
    age:int
    ml_project_done : int = Field(ge=2)
    know_genai : bool
    know_python : bool
    class Config:
        extra="forbid"


class OutputSent(BaseModel):
    dec : bool
    reas  :str

    class Config:
        extra = "forbid"

def result(reg_no: int ,req:InputAccept):    
    if reg_no not in reg_nos:
        return False,"Invalid Registration Number"
    if req.age>25:
        return False,"Over Age!"
    if req.ml_project_done<2:
        return False,"Do More Projects"
    elif req.know_python==False:
        return False,"Learn Python"
    elif req.know_genai==False:
        return False,"Learn GenAI"
    else:
        return True,"Eligible"


@app.post("/result/{reg_no}/",response_model=OutputSent)
def Candidateresult(reg_no:int,req:InputAccept=None):
    dec,reas=result(reg_no,req)

    return{
        "dec":dec,
        "reas":reas
    }