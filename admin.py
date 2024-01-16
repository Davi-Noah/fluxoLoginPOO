lista_admins = []

class Admin():
    def __init__(self) -> None:
        pass
         

    def changeRole(self, users):
        user_name = input('Escolha o nome:\n')
        for user in users:
            if user_name == user['name']:
                role = input(
                    'Escolha o cargo\n'
                    '[1] - Membro\n'
                    '[2] - Membro Vip\n'
                    '[3] - Moderador\n'
                    '[4] - Admin\n'
                    '[0] - Cancelar\n'
                    )
        
                match role:
                    case '1':
                        user['role'] = 'Membro'
                        print(f'{user["id"]}.{user_name} - {user["role"]}.')
                    case '2':
                        user['role'] = 'Membro Vip'
                        print(f'O {user_name} foi alterado para Membro Vip')
                    case '3':
                        user['role'] = 'Moderador'
                        print(f'O {user_name} foi alterado para Moderador')
                    case '4':
                        user['role'] = 'Admin'
                        print(f'O {user_name} foi alterado para Admin')
                    case '0':
                        break
                    case _ :
                        print('Escolha uma opção válida.')

    def deleteUser(self, users):
        user_name = input('Digite o nome do usuário que deseja excluir:\n')
        for user in users:
            if user_name == user['name']:
                users.remove(user)
                print(f'O usuário {user_name} foi excluído com sucesso.')
                return

        print('Usuário não encontrado.')
                        

    def menuAdmin(self, users):
        while True:
            print('===== Opções =====')
            op = input(
                '[1] - Mudar cargo\n'
                '[2] - Excluir usuário\n'
                '[0] - Sair\n'
                    )
            match op:
                case '1':
                    print('====== Mudar cargo ======')
                    self.changeRole(users)

                case '2':
                    print('====== Excluir usuário ======')
                    self.deleteUser(users)

                case '0':
                    break
                case _:
                    print('Escolha uma opção válida.')