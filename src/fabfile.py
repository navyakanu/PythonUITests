import os

from fabric.api import local
from fabric.decorators import task
from fabric.state import env

env.ROOT_DIR = os.path.dirname(__file__)


def set_environment_variable(environment):
    existing_environment = str(os.environ.get('environment'))

    if existing_environment != environment:
        os.environ['environment'] = environment

    return


def setup_env(environment):
    env.path = env.ROOT_DIR
    set_environment_variable(environment)


@task()
def execute_test(test_type):
    setup_env("local")
    execution_command = "py.test --json=reports/report.json --html=reports/report.html -v -m {0} {1} -d --tx 3*popen".format(
        test_type,env.ROOT_DIR)
    local(execution_command)
