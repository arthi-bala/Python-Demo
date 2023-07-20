import sys
sys.path.append("./")
from src.char_frequency import FrequencyCalculator

def test_when_numeric_string_given_return_frequency_dictionary():
    frequency_invalid_string = FrequencyCalculator().char_frequency("123")
    assert frequency_invalid_string == {'1': 1, '2': 1, '3': 1}
	assert False