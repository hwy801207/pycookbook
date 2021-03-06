class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)
def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))

from operator import attrgetter

def sort_by_lambda():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key = attrgetter('user_id')))
    print("max", max(users, key = attrgetter('user_id')))
    print("min", min(users, key = attrgetter('user_id')))

sort_notcompare()

sort_by_lambda()

