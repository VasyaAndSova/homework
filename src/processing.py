def get_new_list_dict(list_dict: list[dict[str, object]], key_state: str = "EXECUTED") -> list[dict[str, object]]:
    new_list_dict = []
    for dicts in list_dict:
        if dicts["state"] == key_state:
            new_list_dict.append(dicts)
    return new_list_dict
