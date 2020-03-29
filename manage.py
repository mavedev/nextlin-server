import os

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS

from app import create_app
from app.model import db

app = create_app(os.getenv('CONFIG') or 'default')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command(
    'shell',
    Shell(make_context=lambda: {
        'app': app,
        'db': db
    })
)


def main() -> None:
    manager.run()


if __name__ == '__main__':
    main()
