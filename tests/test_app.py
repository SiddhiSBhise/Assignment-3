import pytest
from myapp.app import multiply_by_two, divide_by_two, calculate_area  # ✅ add calculate_area

@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a, b]

class TestApp:
    def test_multiplication(self, numbers):
        res = multiply_by_two(numbers[0])
        assert res == numbers[1]

    def test_division(self, numbers):
        res = divide_by_two(numbers[1])
        assert res == numbers[0]

    def test_area_student_id(self):
        assert calculate_area(34*2) == 68  # ✅ now it should work
