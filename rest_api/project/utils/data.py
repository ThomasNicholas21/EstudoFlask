# aqui icorrerá processamento de dados vindo da request do tipo "POST"

def get_developer(data_developer, list_developer):
    for devs in list_developer:
        for value in devs.values():
            if value == data_developer:
                return value

            return 'Developer not Found'



def post_developer_name(data_developer, list_developer):
    default_dict = {'name': data_developer}
    list_developer.append(default_dict)
    

def get_devoloper_tecnologie():
    ...

def post_developer_tecnologie():
    ...

LIST_DEV = []
valor1 = 'thomas'
valor2 = 'asdsad'
valor3 = 'ddddd'

valor_t = 'tecnologia'

post_developer_name(valor1, LIST_DEV)
post_developer_name(valor2, LIST_DEV)
post_developer_name(valor3, LIST_DEV)

print(LIST_DEV)
# info_tec = post_developer_tecnologie(valor3, valor_t, LIST_DEV)
