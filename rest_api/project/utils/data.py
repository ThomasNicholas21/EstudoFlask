# aqui icorrerá processamento de dados vindo da request do tipo "POST"

def get_developer(developer_id: int, list_developer: list[dict]):
    try:
        developer = list_developer[developer_id]

    except IndexError:
        message = "ID is invalid, does not exist".format(developer_id)
        developer = {"status": "Erro", "Message": message}

    return developer


def post_developer_name(data_developer: dict, list_developer: list[dict]):
    list_developer.append(data_developer)


def update_developer_name(data_developer: dict, developer_id:int, list_developer: list[dict]):
    list_developer[developer_id] = data_developer


def delete_developer(developer_id: int, list_developer: list[dict]):
    list_developer.pop(developer_id)
