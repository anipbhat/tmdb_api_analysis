import json

def write_to_file_fun(file, data):
    with open(file, 'w', encoding='utf-16') as f:
        json.dump(data, f, ensure_ascii=False)