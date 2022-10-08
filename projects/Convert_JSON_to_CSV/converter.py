import json

input_File = 'input.json'
if __name__ == '__main__':
    try:
        with open(input_File, 'r') as f:
            data = json.loads(f.read())
            print("debug")

        output = ','.join([*data[0]])
        for obj in data:
            output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'

        with open('output.csv', 'w') as f:
            f.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')
