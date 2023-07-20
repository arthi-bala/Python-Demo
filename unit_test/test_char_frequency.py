import sys
sys.path.append("./")
from src.char_frequency import FrequencyCalculator

def test_when_string_given_char_frequency_return_frequency_dictionary():
    frequency_malayalam = FrequencyCalculator().char_frequency("malayalam")
    frequency_halocination = FrequencyCalculator().char_frequency("halocination")
    assert frequency_malayalam == {'a': 4, 'l': 2, 'm': 2, 'y': 1}
    assert frequency_halocination == {'a': 2, 'c': 1, 'h': 1, 'i': 2, 'l': 1, 'n': 2, 'o': 2, 't': 1}
