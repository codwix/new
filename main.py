from fastapi import FastAPI

app = FastAPI()

company_db = [
    {"company_name" : "Apple"},
    {"company_name" : "Tesla"},
    {"company_name" : "Amazon"},
    {"company_name" : "Alphabet"},
    {"company_name" : "Microsoft"},
    {"company_name" : "Morderna"},
    {"company_name" : "Samsung"},
    {"company_name" : "Nvidia"},
    {"company_name" : "Meta"},
    {"company_name" : "Nike"},
    {"company_name" : "IBM"},
    {"company_name" : "3M"},
    {"company_name" : "Oracle"},
    {"company_name" : "Sony"},
    {"company_name" : "MCDonald"},
    {"company_name" : "Dell"},
    {"company_name" : "CocaCola"},
    {"company_name" : "Mercedes Benz"},
    {"company_name" : "Walmart"},
    {"company_name" : "BMW"},   
]

@app.get("/items/")
async def read_student(skip: int=0, limit:int=20):
    return company_db[skip:skip+limit]