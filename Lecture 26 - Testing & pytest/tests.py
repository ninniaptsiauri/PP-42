import pytest
import main

@pytest.fixture
def calculator():
    return main.Calculator()

def test_add_two_positive(calculator):
    assert calculator.add(2, 3) == 5

def test_add_two_negative(calculator):
    assert calculator.add(-2, -3) == -5

# @pytest.mark.skip
# # @pytest.mark.xfail
def test_subtract_two_positive(calculator):
    assert calculator.subtract(10, 5) == 5

def test_divide_two_positive(calculator):
    assert calculator.divide(10, 2) == 5.0

def test_divide_by_zero(calculator):
    with pytest.raises(ZeroDivisionError, match='Cannot divide by zero'):
        calculator.divide(10, 0)


@pytest.fixture
def temp_file(tmp_path):
    # SETUP
    file = tmp_path / "data.txt"
    file.write_text("hello world")
    yield file  # test runs here
    # TEARDOWN
    file.unlink(missing_ok=True)

def test_file_content(temp_file):
    assert temp_file.read_text() == "hello world"


@pytest.mark.parametrize("a, b, expected", [
    (2,   3,   5),
    (-1,  1,   0),
    (0,   0,   0),
    (100, -50, 50),
])
def test_add(a, b, expected):
    calculator = main.Calculator()
    assert calculator.add(a, b) == expected


def test_add(mocker):
    mock_add = mocker.patch("main.add")
    mock_add.return_value = 5

    result = mock_add(2, 3)

    assert result == 5
    mock_add.assert_called_once_with(2, 3)