import json

def parse(json_str):

    start = json_str.find("{")
    end = json_str.find("} END")
    text = json_str[start:end+1]
    straight = text.replace("\n", "")

    print(straight)
    f_json = json.loads(straight)
    return f_json

