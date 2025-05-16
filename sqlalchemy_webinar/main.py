from project.utils import add_user, get_user_by_id, get_all_users, update_user, drop_user
import prompt


if __name__ == "__main__":
    while True:
        choice = input('Action: ')
        match choice:
            case 'add':
                name = prompt.string('Name: ')
                email = prompt.string('Email: ')
                add_user(name=name, email=email)
            case 'get':
                id = prompt.integer('ID: ')
                user = get_user_by_id(id)
                if user:
                    print(user.name, user.email)
                else:
                    print('User not found')
            case 'get all':
                users = get_all_users()
                if not users:
                    print('Users not found')
                    continue
                for user in users:
                    print(f'{user.id}. {user.name}, {user.email}')
            case 'update':
                user_id = prompt.integer('ID: ')
                new_name = input('Name: ')
                new_email = input('Email: ')
                user = update_user(user_id, new_name=new_name, new_email=new_email)
                if not user:
                    continue
                print('Success')
            case 'delete':
                user_id = prompt.integer('ID: ')
                message = drop_user(user_id)
                print(message)
            case 'exit':
                break
            case _:
                print('Unavailable')
