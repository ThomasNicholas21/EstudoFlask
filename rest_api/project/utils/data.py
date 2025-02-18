# aqui icorrerá processamento de dados vindo da request do tipo "POST"

def get_developer(data_developer, list_developer):
    for devs in list_developer:
        if data_developer == devs:
            return devs
    
    return 'Developer Not Found'

def post_developer_name(data_developer, list_developer):
    default_dict = {}
    default_dict.setdefault('name', data_developer)
    list_developer.append(default_dict)

    return list_developer