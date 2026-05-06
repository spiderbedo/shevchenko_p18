import json

def sort_json_list() -> list:

    """
    Sorts a list of lists in descending order by the numeric value
    of the second element.
    Returns:
        list: sorted list.
    """

    data = input().strip()
    lst = json.loads(data)
    lst.sort(key=lambda x: x[1], reverse=True)
    return lst


if __name__ == "__main__":
    print(sort_json_list())
