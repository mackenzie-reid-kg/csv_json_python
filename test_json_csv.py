import csv
import json

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            jsonArray.append(row)
    
    body = {
        "key_id": "3",
        "contacts": jsonArray
    }
    body = json.dumps(body, indent=4)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(body)

csvFilePath = r'./test_file.csv'
jsonFilePath = r'./test_file.json'

csv_to_json(csvFilePath, jsonFilePath)