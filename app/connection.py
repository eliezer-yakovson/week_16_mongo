from pymongo import MongoClient
import os
import json

MONGO_URI = os.getenv("MONGODB_URL", "mongodb://localhost:27017/")
file_path = './employee_data_advanced.json'

client = MongoClient(MONGO_URI)
db = client["employee_db"]
employees_collection = db["employees"]

with open(file_path) as file:
    file_data = json.load(file)

ins_result = employees_collection.insert_many(file_data)
print(f"Data inserted to MongoDB. Documents inserted: {len(ins_result.inserted_ids)}")