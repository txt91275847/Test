import json

json_str = '{"a": 0, "b": 0, "c": 0}'
result = json.loads(json_str)
print(result)
print(type(result))