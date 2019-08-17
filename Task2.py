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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def find_index_longest_call(input):
    """
    :param input: list of csv data where each item is a row
    :return: index of csv of longest call
    """
    index = 0
    duration = 0
    for idx, row in enumerate(input):
        if duration < int(row[3]):
            duration = int(row[3])
            index = idx
    return index

def test__find_index_longest_call():
    test_input = [['78130 00821', '98453 94494', '01-09-2016 06:01:12', '186'],
                  ['78298 91466', '(022)28952819', '01-09-2016 06:01:59', '2093'],
                  ['97424 22395', '(022)47410783', '01-09-2016 06:03:51', '1975'],
                  ['78298 91786', '(022)28952810', '01-09-2016 08:01:59', '6093']]
    index = find_index_longest_call(test_input)
    assert index == 3

if __name__ == '__main__':
    # Test find_index_longest_call function
    test__find_index_longest_call()

    longest_index = find_index_longest_call(calls)
    msg = "{0} spent the longest time, {1} seconds, on the phone during September 2016."\
        .format(calls[longest_index][1], calls[longest_index][3])
    print(msg)