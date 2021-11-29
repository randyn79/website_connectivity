import requests
import time
import csv
import pandas as pd


def web_connectivity(file):
    with open (file, 'r') as urls:
        
        fields = urls.readline()
        rows = []
        for line in urls:
            line = line.strip('\n').split(',')
            response = requests.get(line[1])
            
            if response.status_code >= 100 and response.status_code < 200:
                message = 'Informational Response'
            elif response.status_code >= 200 and response.status_code < 300:
                message = 'Success'
            elif response.status_code >=300 and response.status_code < 400:
                message = 'Redirection'
            elif response.status_code >= 400 and response.status_code < 500:
                message = 'Client Error'
            elif response.status_code >= 500 and response.status_code < 600:
                message = 'Server Error'
            else:
                message = 'UNKNOWN'

            line.append(response.status_code)
            line.append(message)
            rows.append(line)

        fields = fields.strip('\n').split(',')
        fields.append('status_code')
        fields.append('message')
        return fields, rows


                
def report_csv_log(fields, rows, filename='web_connectivity_log'):
    todays_date = time.strftime("%m-%d-%Y Time %H-%M-%S")
    new_file_name = filename + ' - ' + todays_date + '.csv'

    with open(new_file_name, 'w', newline='') as logfile:
        csvwriter = csv.writer(logfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

def report_print(fields, rows):
    df = pd.DataFrame(rows, columns = fields)
    df = df.set_index(["website_name"])
    
    print(df)
    
    

fields, rows = web_connectivity('web_connectivity_urls.csv')
report_csv_log(fields, rows)
report_print(fields, rows)


