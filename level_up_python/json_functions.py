"""module with functions which takes json string and convert it to dictionary and takes
 dictionary and convert it to json string"""
import json


json_string = '{"a": "apple", "b": "bread", "c": "cucumber" }'
simple_dict = {"a": "apple", "b": "bread", "c": "cucumber", "d": "doll"}


def convert_json_string_to_dict(json_string1):
    # with json.loads(json_string) as f:
    simple_dict1 = json.loads(json_string1)
    return simple_dict1


def convert_dict_to_json_string(some_dict):
    json_string1 = json.dumps(some_dict, indent=2)
    return json_string1


if __name__ == '__main__':
    print(type(json_string))
    a = convert_json_string_to_dict(json_string)
    print("Type of a is " + str(type(a)))
    print(a)
    d = convert_dict_to_json_string(simple_dict)
    print(d)
    print(type(d))
