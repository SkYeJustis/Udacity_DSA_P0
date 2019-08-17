"""
Read file into texts and calls.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def process_distinct_numbers(input, col_1, col_2, final_output):
    """
    :param input: list of rows from file
    :param col_1: Column to search for phone #s
    :param col_2: Column to search for phone #s
    :param final_output:
    :return:
    """
    for row in input:
        if row[col_1] not in final_output:
            final_output.append(row[col_1])
        if row[col_2] not in final_output:
            final_output.append(row[col_2])

def test_functions():
    def test__process_distinct_numbers():
        test_output = []
        test_input = [['12345', '678', None],
                      ['1234', '67890', None],
                      ['123', '6789', None],
                      ['12345', '6789', None],
                      ['12345', '6789', None],
                      ]
        process_distinct_numbers(test_input, 0, 1, test_output)
        assert test_output == ['12345', '678', '1234', '67890', '123', '6789']

    def test__alternative_final_output():
        # Alternative method using set
        res = [row[0] for row in texts]
        res.extend([row[1] for row in texts])
        res.extend([row[0] for row in calls])
        res.extend([row[1] for row in calls])

        # Current method using O(n) processing of reach file row
        distinct_numbers = []
        process_distinct_numbers(input=texts, col_1=0, col_2=1, final_output=distinct_numbers)
        process_distinct_numbers(input=calls, col_1=0, col_2=1, final_output=distinct_numbers)

        assert len(list(set(res))) == len(distinct_numbers)
    ## Test process_distinct_numbers
    test__process_distinct_numbers()
    ## Alternative method
    test__alternative_final_output()

if __name__ == '__main__':
    test_functions()

    # Output: all distinct sending/receiving numbers in call + texts
    distinct_numbers = []
    process_distinct_numbers(input=texts, col_1=0, col_2=1, final_output=distinct_numbers)
    process_distinct_numbers(input=calls, col_1=0, col_2=1, final_output=distinct_numbers)

    msg = "There are {0} different telephone numbers in the records.".format(len(distinct_numbers))
    print(msg)
