from admin import *

users = []

class Dados():
    def __init__(self) -> None:
        pass

    def addUser(self, name, email, password):
        if not name or not password or not email or '@' not in email or '.com' not in email:
            return 'Erro ao cadastrar o usuário. Verifique os dados fornecidos'
        else:
            user = {
                'id': len(users) + 1,
                'name': name,
                'pass': password,
                'email': email,
                'role': 'Membro'
            }
            users.append(user)
            for user in users:
                if user['id'] == 1:
                    user['role'] = 'Admin'

            return f'O usuário {name} foi cadastrado com sucesso'
        

    def showUsers(self):
        if users:
            for user in users:
                print(f'{user["id"]}.{user["name"]}')
        else:
            print('A lista de usuários está vazia')

    def detailsUser(self, name):
        for user in users:
            if user['name'] == name:
                print(f'{user["id"]}.{user["name"]} - {user["email"]} - {user["role"]}')
                return
        print("Usuário não encontrado.")

    def adminUser():
        admin_name = input('Usuário:\n')
        admin_pass = input('Senha:\n')
        if lista_admins:
            for admin in users:
                if admin_name == admin['name'] and admin_pass == admin['pass'] and admin['role'] =='Admin':
                    print(f'Seja bem vindo {admin_name} à área admin.')
                    lista_admins[0]['id'].menuAdmin(users)
                else:
                    print('Você não tem permissão para acessar essa área!')
        else:
            adm = Admin()
            admin = {
                'id' : adm,
                'admin': admin_name,
                'password' : admin_pass
            }
            lista_admins.append(admin)
