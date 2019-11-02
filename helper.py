import json


def write_object_to_json(obj: object, file: str):
    js = json.dumps(obj)
    f = open(file, "x")
    f.write(js)
    f.close()


def read_obj_from_json(file: str):
    with open(file, "r") as json_file:
        return json.load(json_file)