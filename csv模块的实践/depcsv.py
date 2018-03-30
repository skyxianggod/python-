#! /usr/bin/env python
# -*- coding: utf-8 -*-
import csv,time
count_csv=[]
norm_tim=time.mktime(time.strptime('2017-09-08 05:55:00', "%Y-%m-%d %H:%M:%S"))
print(norm_tim)
service_list=['DATA-TSS-0033.ST2','DATA-TSS-0010.ST2','DATA-TSS-0001.ST2']
for service_name in service_list:
    with open(r'F:\dep\depcount\2017-09-08\ChannelUtilization\InboundChannel.csv','r') as csvfile:
        reader = csv.DictReader(csvfile)
        # rows = [row for row in reader]
        # print(rows)
        for row in reader:
            # print(row)
            if row['ClassName']=='ChannelLogger'and row['SubnetID']=='COR'and row['Channel']==service_name:
                sco_tim=time.mktime(time.strptime(row['RecordTime'], "%Y-%m-%d %H:%M:%S"))
                # print(sco_tim)
                if 0<sco_tim-norm_tim<=300:
                    row["TOTAL"]
                    count_csv.append({"service":service_name,"sendmessage":row["TOTAL"]})
                    print(count_csv)


