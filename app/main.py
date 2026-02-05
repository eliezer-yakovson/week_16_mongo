from fastapi import FastAPI, HTTPException
from dal import (
    get_engineering_high_salary_employees,
    get_employees_by_age_and_role,
    get_top_seniority_employees_excluding_hr,
    get_employees_by_age_or_seniority,
    get_managers_excluding_departments,
    get_employees_by_lastname_and_age
)

app = FastAPI()

@app.get("/employees/engineering/high-salary")
def engineering_high_salary():
    try:
        return get_engineering_high_salary_employees()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/employees/by-age-and-role")
async def employees_by_age_and_role():
    try:
        return get_employees_by_age_and_role()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/employees/top-seniority")
async def top_seniority_employees_excluding_hr():
    try:
        return get_top_seniority_employees_excluding_hr()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/employees/age-or-seniority")
async def employees_by_age_or_seniority():
    try:
        return get_employees_by_age_or_seniority()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/employees/managers/excluding-departments")
async def managers_excluding_departments():
    try:
        return get_managers_excluding_departments()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/employees/by-lastname-and-age")
async def employees_by_lastname_and_age():
    try:
        return get_employees_by_lastname_and_age()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)