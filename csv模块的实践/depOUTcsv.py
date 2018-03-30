#! /usr/bin/env python
# -*- coding: utf-8 -*-
#__auther__:龚志翔
import csv,time,datetime,os
count_csv=[]
now_day=datetime.datetime.now().date()
yester_day=now_day + datetime.timedelta(-1)

now_time=str(now_day)+" 05:55:00"
yester_time=str(yester_day)+" 05:55:00"

now_out_path=os.path.join('F:\dep\depcount',str(now_day),'ChannelUtilization\OutboundChannel.csv')
yester_out_path=os.path.join('F:\dep\depcount',str(yester_day),'ChannelUtilization\OutboundChannel.csv')

now_in_path=os.path.join('F:\dep\depcount',str(now_day),'ChannelUtilization\InboundChannel.csv')

count_csv_file=os.path.join('F:\object',str(now_day)+"count.csv")
# print now_path,yester_path
# print now_time,yester_time
now_norm_time=time.mktime(time.strptime(now_time, "%Y-%m-%d %H:%M:%S"))
yester_norm_time=time.mktime(time.strptime(yester_time, "%Y-%m-%d %H:%M:%S"))

# print now_norm_time,yester_norm_time
# print(norm_tim)
def recive_message(path,service_name,now_norm_time):
    with open(path,'r') as out_csvfile:
        reader = csv.DictReader(out_csvfile)
#     # rows = [row for row in reader]
#     # print(rows)
        a=0
        for row in reader:
#         # print(row)
#         #if row['ClassName']=='ChannelLogger'and row['SubnetID']=='COR'and row['Channel']=='DATA-TSS-0033.ST2':
#
            if  row['Channel']==service_name:
                sco_tim=time.mktime(time.strptime(row['RecordTime'], "%Y-%m-%d %H:%M:%S"))
#             # print(sco_tim)
                if 0<=sco_tim-now_norm_time<=300:
                    print(row)
                    a=a+int(row["TOTAL"])#recivemessage
                    return a
                else:
                    print(service_name,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(now_norm_time)),"recive_message is not exits")
                    return 0

def send_message(path,service_name,now_norm_time):
        with open(path,'r') as in_csvfile:
            reader = csv.DictReader(in_csvfile)
            # rows = [row for row in reader]
            # print(rows)
            for row in reader:
                # print(row)
                if row['ClassName']=='ChannelLogger'and row['SubnetID']=='COR'and row['Channel']==service_name:
                    sco_tim=time.mktime(time.strptime(row['RecordTime' ], "%Y-%m-%d %H:%M:%S"))
                    # print(sco_tim)
                    if 0<sco_tim-now_norm_time<=300:
                        return  int(row["TOTAL"])
                    else:
                        print(service_name,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(now_norm_time)),"sendmessage is not exits")
                        return 0



service_list=['DATA-TSS-00330ST2','DATA-TSS-0010.ST2','DATA-TSS-0001.ST2']
for service_name in service_list:
    now_count_message=recive_message(now_out_path,service_name,now_norm_time)
    yester_count_message=recive_message(yester_out_path,service_name,yester_norm_time)
    count_rcivied_message=now_count_message-yester_count_message
    count_send_message=send_message(now_in_path,service_name,now_norm_time)
    if count_rcivied_message != count_send_message:
        status="False"
    else:
        status="True"
    count_csv.append({"service":service_name,"rcivied_message":count_rcivied_message,"send_message":count_send_message,"status":status})

count_csv=[{'status': 'True', 'rcivied_message': 0, 'send_message': 0, 'service': 'DATA-TSS-0033.ST2'}, {'status': 'True', 'rcivied_message': 0, 'send_message': 0, 'service': 'DATA-TSS-0010.ST2'}, {'status': 'True', 'rcivied_message': 0, 'send_message': 0, 'service': 'DATA-TSS-0001.ST2'}]
with open(count_csv_file, 'w+') as csv_file:
    headers = [k for k in count_csv[0]]
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()
    for dictionary in count_csv:
        writer.writerow(dictionary)

