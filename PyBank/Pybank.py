# Working With
import os

import csv

#with variables
total_revenue = 0
prev_rev = 0
diff_max = 0
diff_min = 0
prev_month_rev =0
month_rev=0
months = 0
diff = 0
large_month = " "
small_month = " "
agg_rev_chge = 0

output_path = os.path.join( "output", "pybankout.csv")

#import csv
input_file = input("What is the filename you need to analyze?  ")
csvpath = os.path.join(input_file)

with open(csvpath,newline="")as bud_data:
    csvreader = csv.reader(bud_data, delimiter=',')
    reader = csv.DictReader(bud_data)
    header = next(bud_data)
# gather data from each row
    for row in csvreader:
            #gather aggregate info
            #update number of months
              months = months + 1
              #update total revenue with data from row
              total_revenue = total_revenue + int(row[1])
              #set revenue for month
              month_rev=int(row[1])
              #if current rows revenue is greater than previous month's revenue stored at the end of this
              # then store this month as maximum revenue              
              diff = int(month_rev) - int(prev_month_rev)
              if int(diff)> int(diff_max):
                  diff_max=diff
              else:
                  diff_max = diff_max
              if int(diff)< int(diff_min):
                  diff_min=diff
                  large_month = row[0]
              else:
                  diff_max = diff_max
                  smmall_month = row[0]

              agg_rev_chge = agg_rev_chge + int(diff)

              prev_month_rev=row[1]
              final_month =row[0]

              
avg_rev_change = int(agg_rev_chge)/int(months)

tot_months_out = ("Total Months in Period : " + str(months))
tot_revenue_out=("\""+"Total Revenue : $"+f"{total_revenue:,d}"+"\"")
avg_rev_change_out =("\""+"Average Revenue Change : "+" $"+f"{avg_rev_change:.2f}"+"\"")
diff_min_out = ("\""+"Minimum Revenue Decrease : $"+f"{diff_min:,d}"+"\"")
diff_max_out = ("\""+"Maximum Revenue Increase :"+large_month+" $"+f"{diff_max:,d}"+"\"")
#agg_rev_chge_out = 



tot_revenue_out_qts = "\"" + tot_revenue_out + "\""
title =("Financial Analysis for the " + str(months) + "month period ending " + str(final_month))
with open(output_path, 'w',newline='') as pybank_file_out:

    # Initialize csv.writer
    csvwriter = csv.writer(pybank_file_out, delimiter=',')
    
    pybank_file_out.write(title+'\n')
    pybank_file_out.write('-'*75+'\n')
    pybank_file_out.write(tot_months_out+'\n')
    pybank_file_out.write(avg_rev_change_out+'\n')
    pybank_file_out.write(diff_min_out+'\n')
    pybank_file_out.write(diff_max_out+'\n')
    pybank_file_out.write(tot_revenue_out)