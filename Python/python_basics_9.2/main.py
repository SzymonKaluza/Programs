class User():
    def __init__(self, first_name, last_name, last_visit, user_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.last_visit = last_visit
        self.user_name = user_name
        self.age = age

    def describe_user(self):
        print('Użytkownik nazywa się ' + self.first_name.title() + ' ' + self.last_name.title()
              + ', jest graczem o nicku ' + self.user_name + ', ma ' + str(self.age) + ' lat'
              + ', ostatni raz zalogował się : ' + self.last_visit)

    def greet_user(self):
        print('Witaj ' + self.user_name + ' w mojej grze')


describe = User('jan', 'nowak', '12:08:2021', 'paymon', 12)
print(describe.describe_user())
print(describe.greet_user())
