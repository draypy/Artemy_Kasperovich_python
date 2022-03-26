from Artemy_Kasperovich_python import Task1, Task2, Task3
import pytest


@pytest.fixture
def bigger_than_seven():
    return Task1.bigger_than_seven


@pytest.fixture
def check_name():
    return Task2.check_name


@pytest.fixture
def multiple_of_three():
    return Task3.multiple_of_three
