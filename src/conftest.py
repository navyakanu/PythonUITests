import pytest


def pytest_addoption(parser):
    parser.addoption("--withdocker", action="store", default=False,
        help="specify if tests need to be run in dockerised Selenium hub")

@pytest.fixture(scope='class')
def withdocker(request):
    return request.config.option.withdocker