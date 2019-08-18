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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def find_area_codes_and_mobile_prefixes(input):
    """
    :param input:
    :return:
    """
    output = []
    for row in input:
        if row[0][0:5] == '(080)':
            # Fixed lines start with an area code enclosed in brackets. The area
            #    codes vary in length but always begin with 0.
            if '(' in row[1]:
                end_idx = row[1].find(')')
                if row[1][1:end_idx] not in output:
                    output.append(row[1][1:end_idx])
            # Mobile numbers have no parentheses, but have a space in the middle
            #    of the number to help readability. The prefix of a mobile number
            #    is its first four digits, and they always start with 7, 8 or 9.
            elif ' ' in row[1] and row[1][0] in ['7', '8', '9']:
                if row[1][0:4] not in output:
                    output.append(row[1][0:4])
            # Telemarketers' numbers have no parentheses or space, but they start
            #    with the area code 140.
            elif ' ' not in row[1] and '(' not in row[1] and ')' not in row[1] and row[1][0:3] == '140':
                if row[1][0:3] not in output:
                    output.append(row[1][0:3])
    output.sort()
    return output

def perc_calls_fixed_to_fixed(input):
    """
    :param input:
    :return: string
    """
    calls_from_bangalore = 0
    rec_at_and_from_bangalore = 0
    for row in input:
        if row[0][0:5] == '(080)':
            calls_from_bangalore += 1
            if row[1][0:5] == '(080)':
                rec_at_and_from_bangalore += 1
    return "{0:.2f}".format((rec_at_and_from_bangalore/calls_from_bangalore)*100)

def test_functions():
    def test__find_area_codes_and_mobile_prefixes():
        test_input = [['(080)35121497', '98453 94494', '01-09-2016 06:01:12', '186'],
                      ['(080)35121498', '(022)28952819', '01-09-2016 06:01:59', '2093'],
         ['(080)35121498', '(0220)28952819', '01-09-2016 06:01:59', '2093'],
         ['(080)35121499', '1400010783', '01-09-2016 06:03:51', '1975'],
         ['93427 40118', '(080)33118033', '01-09-2016 06:11:23', '1156'],
         ['90087 42537', '(080)35121497', '01-09-2016 06:17:26', '573']]
        output = find_area_codes_and_mobile_prefixes(test_input)
        assert output == ['022', '0220', '140', '9845']

    def test__perc_calls_fixed_to_fixed():
        test_input = [['(080)33118033', '(080)28952819', '01-09-2016 06:01:12', '186'],
         ['(080)33118032', '(080)28952829', '01-09-2016 06:01:59', '2093'],
         ['(080)33118035', '(080)47410783', '01-09-2016 06:03:51', '1975'],
         ['(080)934240118', '(022)33118033', '01-09-2016 06:11:23', '1156'],
         ['90087 42537', '(022)35121497', '01-09-2016 06:17:26', '573']]
        perc = perc_calls_fixed_to_fixed(test_input)
        assert perc == "75.00"

    test__find_area_codes_and_mobile_prefixes()
    test__perc_calls_fixed_to_fixed()

if __name__ == '__main__':
    test_functions()

    # Part A
    msg_a = "The numbers called by people in Bangalore have codes:"
    print(msg_a)
    for code in find_area_codes_and_mobile_prefixes(calls):
        print(code)

    # Part B
    msg_b = """{0} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."""\
        .format(perc_calls_fixed_to_fixed(calls))
    print(msg_b)