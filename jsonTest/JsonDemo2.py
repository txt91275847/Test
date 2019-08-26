import json

a = ['foo', {'bar': ('baz', None, 1.0, 2)}]
result = json.dumps(a)
print(result)
print(type(result))
