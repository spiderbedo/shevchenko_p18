import json

def to_json(func):

    """
    Decorator that converts result to JSON string.
    """
    
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result, ensure_ascii=False)
    return wrapper


@to_json
def get_data():
    return {"name": "Барсик", "age": 7}


@to_json
def get_list():
    return [1, 2, 3]


if __name__ == "__main__":
    print(get_data())
    print(get_list())
