# services/tasks/manage.py


import unittest

from flask.cli import FlaskGroup

from project import create_app, db   # new


app = create_app()  # new
cli = FlaskGroup(create_app=create_app)  # new


@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def test():
    """ Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    cli()
