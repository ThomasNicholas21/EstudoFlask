# aqui icorrerá processamento de dados vindo da request do tipo "POST"

def get_developer(data_developer: dict, list_developer: list[dict]):
    for devs in list_developer:
        if devs['name'] == data_developer:
            return devs

    return None


def post_developer_name(data_developer: dict, list_developer: list[dict]):
    default_dict = {'name': data_developer}
    list_developer.append(default_dict)


def post_developer_tecnologie(data_developer: dict, data_tecnologie: dict, list_developer: list[dict]):
    get_developer_info = get_developer(data_developer, list_developer)
    if get_developer_info:
        get_developer_info.update(data_tecnologie)
        

