users = [
    {
        'id': 1,
        'username': 'bob',
        'password': 'super'
    }
]

username_mapping = {'bob': {
        'id': 1,
        'username': 'bob',
        'password': 'super'
    }
}

user_id_mapping = {1: {
        'id': 1,
        'username': 'bob',
        'password': 'super'
    }
}


def authentication(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return user_id_mapping.get(user_id, None)
