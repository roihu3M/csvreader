import os
import csv

def file_processing_func(files):
    objects = []
    for file in files:
        paths = os.path.abspath(file)
        with open(paths, encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                object = {}
                for field_name in reader.fieldnames:
                    value = row.get(field_name)
                    object[field_name] = value
                objects.append(object)
    return objects