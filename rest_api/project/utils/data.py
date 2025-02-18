# aqui icorrerá processamento de dados vindo da request do tipo "POST"

def get_developer(data_developer, list_developer):
    for devs in list_developer:
        for value in devs.values():
            if value == data_developer:
                return value

            return 'Developer not Found'



def post_developer_name(data_developer, list_developer):
    default_dict = {}
    default_dict.setdefault('name', data_developer)
    list_developer.append(default_dict)
    
    return list_developer
