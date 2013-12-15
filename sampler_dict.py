import csv, datetime

#read csv using DictReader
file = csv.DictReader(open('small_sample.csv', 'r'))
frontrunner = ['P80003338', 'P80002801']
extraction = []
fieldnames = ['cmte_id','cand_id','cand_nm','contbr_nm','contbr_city','contbr_st','contbr_zip','contbr_employer','contbr_occupation','contb_receipt_amt','contb_receipt_dt','receipt_desc','memo_cd','memo_text','form_tp','file_num','tran_id','election_tp']


for row in file:
    f = file.readlines()
    for i in frontrunner:
        if i in f:
            name = row['cand_nm']
            datestr = row['contb_receipt_dt']
            amount = float(row['contb_receipt_amt'])
            date = datetime.datetime.strptime(datestr, '%d-%b-%y')
            extraction.append(row)

with open("frontrunnerdata_2.csv", 'w') as f:
    writer = csv.DictWriter(f, fieldnames = fieldnames)
    writer.writerows(extraction)
f.close()

