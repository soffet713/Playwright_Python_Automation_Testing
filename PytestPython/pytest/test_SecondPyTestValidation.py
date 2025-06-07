# Fixtures - reusable code that can be used throughout test file(s)
import pytest

# smoke test
@pytest.mark.smoke
def test_third_check(pre_setup):
    print("Executing the third test")

def test_fourth_test(pre_setup):
    print("Executing the fourth test")
