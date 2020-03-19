from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    path = '/Users/purvadalvi/MyProjects/vEnv/example_project/users'
    def ready(self):
        import users.signals
