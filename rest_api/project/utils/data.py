# aqui icorrerá processamento de dados vindo da request do tipo "POST"

def get_developer(developer_id: int, list_developer: list[dict]):
    try:
        developer = list_developer[developer_id]
        return developer
    except IndexError:
        raise IndexError(f'Error: list has none value: {developer} ')


def post_developer_name(data_developer: dict, list_developer: list[dict]):
    list_developer.append(data_developer)


def update_developer_name(data_developer: dict, developer_id:int, list_developer: list[dict]):
    list_developer[developer_id] = data_developer


def delete_developer(developer_id: int, list_developer: list[dict]):
    list_developer.pop(developer_id)
