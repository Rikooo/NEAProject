
import json
a = [
    [
        {'time': 0.0, 'position': [300.0, 200.0], 'angle': 0.0},
        {'time': 0.028000000000000004, 'position': [
            300.0784, 200.0], 'angle': 0.0},
        {'time': 0.048, 'position': [
            300.18559999999997, 200.0], 'angle': 0.0}
    ],
]

json_str = json.dumps(a, indent=4)
# print(json_str)
# a([turn_count-2][snapshot_number]['key']) OR a([turn_count-1][snapshot_number]['key'][x/y])
# print(a[0][0]['time'])  # = 0.0 (Y)
# print(a[0][0]['position'])  # = [300.0, 200.0]
# print(a[0][0]['position'][0])  # = 300.0

# print(a[0][2]['time'])
print(len(a))
