from connection import employees_collection

def get_engineering_high_salary_employees():
    return list(employees_collection.find({
        "job_role.department": "Engineering",
        "salary": {"$gt": 65000}
    }, {
        "employee_id": 1,
        "name": 1,
        "salary": 1,
        "_id": 0
    }))

def get_employees_by_age_and_role():
    return list(employees_collection.find({
        "age": {"$gte": 30, "$lte": 45},
        "job_role.title": {"$in": ["Engineer", "Specialist"]}
    },{"_id": 0}))

def get_top_seniority_employees_excluding_hr():
    return list(employees_collection.find({
        "job_role.department": {"$ne": "HR"}
    },{"_id": 0}).sort("years_at_company", -1).limit(7))

def get_employees_by_age_or_seniority():
    return list(employees_collection.find({
        "$or": [
            {"age": {"$gt": 50}},
            {"years_at_company": {"$lt": 3}}
        ]
    }, {
        "employee_id": 1,
        "name": 1,
        "age": 1,
        "years_at_company": 1,
        "_id": 0
    }))

def get_managers_excluding_departments():
    return list(employees_collection.find({
        "job_role.title": "Manager",
        "job_role.department": {"$nin": ["Sales", "Marketing"]}
    },{"_id": 0}))

def get_employees_by_lastname_and_age():
    return list(employees_collection.find({
        "$or": [
            {"name": {"$regex": "Nelson$"}},
            {"name": {"$regex": "Wright$"}}
        ],
        "age": {"$lt": 35}
    }, {
        "name": 1,
        "age": 1,
        "job_role.department": 1,
        "_id": 0
    }))
