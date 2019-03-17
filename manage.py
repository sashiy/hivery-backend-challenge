import unittest

from flask_script import Manager

from paranuara_api import blueprint, main

application = main.create_app()
application.register_blueprint(blueprint)
application.app_context().push()

manager = Manager(application)


@manager.command
def run():
    application.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('paranuara_api/test', pattern='test*.py')
    print(tests.countTestCases())
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
