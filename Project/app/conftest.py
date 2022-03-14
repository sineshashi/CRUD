
def pytest_addoption(parser):
    parser.addoption(
        "--id",
        help = "id for the profile which you want to test"
    )


def pytest_generate_tests(metafunc):
    if "id" in metafunc.fixturenames:
        metafunc.parametrize("id", metafunc.config.getoption("id"))


