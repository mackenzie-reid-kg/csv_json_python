import csv
import json
import sys

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    try:
        with open(csvFilePath, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
            for row in csvReader:
                jsonArray.append(row)
    except Exception as e:
        print >> sys.stderr, "ERROR Error reading csvFile: %s" % csvFilePath
        
    try:    
        body = {
            "key_id": "3",
            "contacts": jsonArray
        }
        body = json.dumps(body, indent=4)
    except Exception as e:
        print >> sys.stderr, "ERROR Error creating json request body"

    try: 
        with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
            jsonf.write(body)
    except Exception as e:
        print >> sys.stderr, "ERROR Error writing jsonFile: %s" % jsonFilePath

csvFilePath = r'./test_file.csv'
jsonFilePath = r'./test_file.json'

csv_to_json(csvFilePath, jsonFilePath)