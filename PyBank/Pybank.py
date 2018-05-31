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
start_value = 0
#export to files
output_path = os.path.join( "output","pybankout.csv")
output_path_txt = os.path.join( "output", "pybankout.txt")

#working with file
print("!!!!since this would take SOOO much of my TA's valuable time I have added duplicates of both data files included in the excersise these two options are a.csv and b.csv")
print(" ")
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
              # then store this month as maximum revenue based on conditions below      
              diff = int(month_rev)-int(prev_month_rev)
              #if int(months)==1:
                #start_value =row[1]
             # else:
                #start_value = start_value
              if int(months)==1:
                diff =0
              else:
                start_value = start_value
              
              if int(diff)> int(diff_max): 
                  #and int(diff) != int(start_value))#
                  diff_max=diff
              else:
                  diff_max = diff_max
              if int(diff)< int(diff_min):
                  # and int(diff) != int(start_value))
                  diff_min=diff
                  small_month = row[0]
              else:
                  diff_max = diff_max
                  large_month= row[0]
              

              agg_rev_chge = agg_rev_chge + int(diff)

              prev_month_rev=row[1]
              final_month =row[0]

#average revenue              
avg_rev_change = int(agg_rev_chge)/(int(months)-1)
#formatted output for both csv and txt output
tot_months_out = ("Total Months in Period : " + str(months))
tot_revenue_out=("\""+"Total Revenue : $"+f"{total_revenue:,d}"+"\"")
tot_revenue_out_txt=("Total Revenue : $"+f"{total_revenue:,d}")
avg_rev_change_out =("\""+"Average Revenue Change : "+" $"+f"{avg_rev_change:.2f}"+"\"")
avg_rev_change_out_txt=("Average Revenue Change : "+" $"+f"{avg_rev_change:.2f}")
diff_min_out = ("\""+"Minimum Revenue Decrease : "+small_month+"= $"+f"{diff_min:,d}"+"\"")
diff_min_out_txt = ("Minimum Revenue Decrease : "+small_month+"= $"+f"{diff_min:,d}")
diff_max_out = ("\""+"Maximum Revenue Increase :"+large_month+"= $"+f"{diff_max:,d}"+"\"")
diff_max_out_txt = ("Maximum Revenue Increase :"+large_month+"= $"+f"{diff_max:,d}")
agg_rev_chge_out = ("\""+"Aggrevchange : $"+f"{agg_rev_chge:,d}"+"\"")
agg_rev_chge_out_max = ("Aggrevchange : $"+f"{agg_rev_chge:,d}")
file_analyzed_txt = ("File analyzed ="+input_file)


tot_revenue_out_qts = "\"" + tot_revenue_out + "\""
title =("Financial Analysis for the " + str(months) + " month period ending " + str(final_month))


with open(output_path, 'w',newline='') as pybank_file_out:
    # export csv version
    # Initialize csv.writer
    csvwriter = csv.writer(pybank_file_out, delimiter=',')
    
    pybank_file_out.write(title+'\n')
    pybank_file_out.write('-'*75+'\n')
    pybank_file_out.write("File analyzed = "+input_file+'\n')
    pybank_file_out.write('-'*75+'\n')
    pybank_file_out.write(tot_months_out+'\n')
    pybank_file_out.write(avg_rev_change_out+'\n')
    pybank_file_out.write(diff_min_out+'\n')
    pybank_file_out.write(diff_max_out+'\n')
    pybank_file_out.write(tot_revenue_out+'\n')
    pybank_file_out.write(agg_rev_chge_out+'\n')

#export txt file using formatted variables
f = open(output_path_txt, 'w')
f.write((f'''

{title }
{'-'*75}
{file_analyzed_txt}
{'-'*75}


{tot_months_out}
{tot_revenue_out_txt}
{avg_rev_change_out_txt}
{diff_min_out_txt}
{diff_max_out_txt}
{avg_rev_change_out_txt}



'''))
f.close()

   