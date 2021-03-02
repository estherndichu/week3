from app import create_app,db
from flask_script import Manager,Shell, Server
from app.models import User,Pitches
from flask_migrate import Migrate,MigrateCommand
from flask_login import LoginManager

# Creating app instance
app = create_app('development')

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Pitches = Pitches)
if __name__ == '__main__':
    manager.run()