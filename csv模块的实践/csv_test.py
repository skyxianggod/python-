#! /usr/bin/env python
# -*- coding: utf-8 -*-
import csv

count_csv=[{'status': 'True', 'rcivied_message': 0, 'send_message': 0, 'service': 'DATA-TSS-0033.ST2'}, {'status': 'True', 'rcivied_message': 0, 'send_message': 0, 'service': 'DATA-TSS-0010.ST2'}, {'status': 'True', 'rcivied_message': 0, 'send_message': 0, 'service': 'DATA-TSS-0001.ST2'}]
with open('count.csv', 'w+') as csv_file:
    headers = [k for k in count_csv[0]]
    print(headers)
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()
    for dictionary in count_csv:
        writer.writerow(dictionary)

with open('count.csv', 'r+') as csv_file:
    reader = csv.DictReader(csv_file)
    print(reader)
    print([row for row in reader])