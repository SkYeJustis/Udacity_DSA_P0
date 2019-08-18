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

def find_chattiest_phone_number(input):
    """
    :param input: list of csv data where each item is a row
    :return: tuple of the phone number and seconds spent on the phone
    """
    phone_number_time = {}
    for row in input:
        # Recording duration spent making calls for a phone number
        if row[0] not in phone_number_time:
            phone_number_time[row[0]] = int(row[3])
        else:
            phone_number_time[row[0]] += int(row[3])
        # Recording duration spent answering calls for a phone number
        if row[1] not in phone_number_time:
            phone_number_time[row[1]] = int(row[3])
        else:
            phone_number_time[row[1]] += int(row[3])

    return sorted(phone_number_time.items(), key=lambda x: x[1], reverse=True)[0]

def test__function():
    test_input = [['78130 00821', '98453 94494', '01-09-2016 06:01:12', '4000'],
                  ['78298 00000', '78130 00821', '01-09-2016 06:01:59', '2093'],
                  ['78298 91466', '(022)28952819', '01-09-2016 06:01:59', '2093'],
                  ['78298 91466', '(022)47410783', '01-09-2016 06:03:51', '1975'],
                  ['78298 91780', '(022)28952810', '01-09-2016 08:01:59', '100'],
                  ['78298 91781', '(022)28952810', '01-09-2016 08:01:59', '200'],
                  ['78298 91782', '(022)28952810', '01-09-2016 08:01:59', '400'],
                  ]
    chattiest_phone_number = find_chattiest_phone_number(test_input)
    assert chattiest_phone_number == ('78130 00821', 6093)

if __name__ == '__main__':
    # Test find_chattiest_phone_number function
    test__function()

    chattiest_phone_number = find_chattiest_phone_number(calls)
    msg = "{0} spent the longest time, {1} seconds, on the phone during September 2016."\
        .format(*chattiest_phone_number)
    print(msg)