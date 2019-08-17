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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def never_send_texts(compare_num, texting_nums):
    """
    :param compare_num:
    :param texting_nums:
    :return:
    """
    if compare_num not in texting_nums:
        return True
    return False

def never_receive_texts(compare_num, get_text_nums):
    """
    :param compare_num:
    :param get_text_nums:
    :return:
    """
    if compare_num not in get_text_nums:
        return True
    return False

def never_receive_calls(compare_num, get_call_nums):
    """
    :param compare_num:
    :param get_call_nums:
    :return:
    """
    if compare_num not in get_call_nums:
        return True
    return False

def not_duplicate(compare_num, list):
    """
    :param compare_num:
    :param list:
    :return:
    """
    if compare_num not in list:
        return True
    return False

def find_possible_telemarketers(input_calls, input_texts):
    """
    :param input_calls:
    :param input_texts:
    :return:
    """
    output = []

    send_text_nums = list(set([row[0] for row in input_texts]))
    rec_text_nums = list(set([row[1] for row in input_texts]))
    rec_call_nums = list(set([row[1] for row in input_calls]))

    for row in input_calls:
        if never_send_texts(row[0], send_text_nums) \
                and never_receive_texts(row[0], rec_text_nums) \
                and never_receive_calls(row[0], rec_call_nums) \
                and not_duplicate(row[0], output):
            output.append(row[0])
    output.sort()
    return output

def test_functions():
    assert never_send_texts('12345', ['(080)33118033', '(022)33118033', '93427 40118']) == True
    assert never_send_texts('93427 40118', ['(080)33118033', '(022)33118033', '93427 40118']) == False

    assert never_receive_texts('12345', ['(080)33118033', '(022)33118033', '93427 40118']) == True
    assert never_receive_texts('93427 40118', ['(080)33118033', '(022)33118033', '93427 40118']) == False

    assert never_receive_calls('12345', ['(080)33118033', '(022)33118033', '93427 40118']) == True
    assert never_receive_calls('93427 40118', ['(080)33118033', '(022)33118033', '93427 40118']) == False


    assert not_duplicate('93427 40118', ['(080)33118033', '(022)33118033', '93427 40118']) == False
    assert not_duplicate('12345', ['(080)33118033', '(022)33118033', '93427 40118']) == True

    input_calls = [['78130 00821', '98453 94494', '01-09-2016 06:01:12', '186'],
                   ['78130 00821', '(080)35121497', '01-09-2016 06:17:26', '573'],
                   ['78130 00821', '(04344)322628', '01-09-2016 06:19:28', '2751'],
                   ['98453 46196', '94005 06213', '01-09-2016 06:40:20', '2457'],
                   ['78290 99865', '89071 31755', '01-09-2016 06:46:56', '9'],
                   # '(022)28952819' received a call
                   ['(022)28952819', '93427 40118', '01-09-2016 06:01:59', '2093'],
                   ['93427 40118', '(022)28952819', '01-09-2016 06:11:23', '1156'],
                   # '(080)45291968' sent a text
                   ['(080)45291968', '90365 06212', '01-09-2016 06:30:36', '9'],
                   # '78132 18081' received a text
                   ['78132 18081', '77956 90632', '01-09-2016 06:39:03', '3043']]
    input_texts = [['(080)45291968', '90365 06212', '01-09-2016 06:03:22'],
                   ['94489 72078', '78132 18081', '01-09-2016 06:05:35']]
    output = find_possible_telemarketers(input_calls, input_texts)
    # Ordered lexicographically
    assert output == ['78130 00821', '78290 99865', '98453 46196']

if __name__ == "__main__":
    test_functions()

    print("These numbers could be telemarketers: ")
    for number in find_possible_telemarketers(calls, texts):
        print(number)