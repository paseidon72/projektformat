import json


input_data = [
    {
        123456: (
            {
                "firstname": "name1",
                "age": 22
            }
        ),
        654321: (
            {
                "firstname": "name2",
                "age": 25
            }
        ),
        987654: (
            {
                "firstname": "name3",
                "age": 28
            }
        ),
        456789: (
            {
                "firstname": "name4",
                "age": 30
            }
        ),
        234567: (
            {
                "firstname": "name5",
                "age": 35
            }
        ),
        876543: (
            {
                "firstname": "name6",
                "age": 38
            }
        )

    }
]

with open('task_1.json', 'w') as f:
    json.dump(input_data, f)
