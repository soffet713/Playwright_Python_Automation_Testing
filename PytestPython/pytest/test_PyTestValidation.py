# Fixtures - reusable code that can be used throughout test file(s)
import pytest

# Scope can also be set to class if tests are executed within a class and you only want the fixture executed once
@pytest.fixture(scope="module")
def pre_work():
    print("Module setup the browser instance..")
    return "pass"

@pytest.fixture(scope="function")
def second_work():
    print("Setup second_work function instance..")
    yield # pause - return to test and complete, then come back to fixture to finish steps
    print("Teardown function instance..")

# smoke test - use mark.smoke as custom tag
@pytest.mark.smoke
def test_initial_check(pre_work, second_work):
    print("Executing the first test")
    assert pre_work == "pass"

# skip test - use mark.skip as custom tag for skipping
@pytest.mark.skip
def test_second_test(pre_work, second_work):
    print("Executing the second test")
