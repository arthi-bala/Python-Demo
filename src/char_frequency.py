''' This function is to count of each letter of the given string (the frequency of each character)'''

class FrequencyCalculator:
    def __init__(self) -> None:
        return
    
    def char_frequency(self, given_string) -> dict:
        frequency_dict = {}
        for i in given_string:
            if i not in frequency_dict:
                frequency_dict[i] = given_string.count(i)
        return frequency_dict

    # if __name__ == "__main__":
    #     input_string = input("Enter the string : ")
    #     print(char_frequency(input_string))