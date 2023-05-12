#!/usr/bin/python3
'''
A script that reads stdin line by line and computes metrics:
  Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
  <status code> <file size> (if the format is not this one, the line
  must be skipped)
'''


import sys


status_codes = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
  }

# is the sum of all previous <file size>
total_size = 0

count = 0
try:

    for line in sys.stdin:
        parser = line.split()

        # skip the line if the format doesn't match above
        if len(parser) < 5:
            continue

        file_size = int(parser[-1])
        status_code = parser[-2]

        total_size += file_size
        count += 1

        # checks if the status_code is exists in the dict `status_codes`
        if status_code in status_codes.keys():
            status_codes[status_code] += 1

        if count == 10:
            count = 0
            print('File size: {}'.format(total_size))
            [print('{}: {}'.format(code, count))
                for code, count in sorted(status_codes.items()) if count != 0]

except Exception as error:
    pass

finally:
    print('File size: {}'.format(total_size))
    [print('{}: {}'.format(code, count))
        for code, count in sorted(status_codes.items()) if count != 0]
