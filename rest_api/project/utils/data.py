# aqui icorrerá processamento de dados vindo da request do tipo "POST"

def get_developer(data_developer, list_developer):
    for devs in list_developer:
        if devs['name'] == data_developer:
            return devs

    return None


def post_developer_name(data_developer, list_developer):
    default_dict = {'name': data_developer}
    list_developer.append(default_dict)
    

def get_devoloper_tecnologie():
    ...

def post_developer_tecnologie(data_developer, data_tecnologie, list_developer):
    ...