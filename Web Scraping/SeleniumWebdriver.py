import csv
import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
import xlsxwriter

is_task_complete=False
workbook=xlsxwriter.Workbook("Marathon_Eindhoven.xlsx")
worksheet= workbook.add_worksheet("Full marathon sheet")
row=0
col=0
#no_of_requests=2415 #Full marathon
no_of_requests=7410 #Half marathon
content = ["id", "eventId", "raceId", "bib", "bibForUrl", "category", "rank", "genderRank", "categoryRank",
               "gunTime", "chipTime", "primaryDisplayTime", "speedInKmh", "name", "countryCode", "activityType",
               "gender", "city", "cumulativeTime_5k", "name_5k", "cumulativeTime_10k", "name_10k", "cumulativeTime_15k", "name_15k",
               "cumulativeTime_20k", "name_20k", "cumulativeTime_25k", "name_25k", "cumulativeTime_half", "name_half", "cumulativeTime_30k", "name_30k", "cumulativeTime_35k", "name_35k",
               "cumulativeTime_40k", "name_40k", "cumulativeTime_finish", "name_finish", "gunTimeInSec",
               "chipTimeInSec", "customValues", "displayDistance", "qualified"]

col_map={}
data_map={}

def init_data_map():
    for item in content:
        data_map[item]="-"

def scrape_data(driver):


    global row
    global col

    if row==0:
        for item in content:
            # write operation perform
            col_map[item]=col
            worksheet.write(row, col, item)
            col += 1
        row+=1
        col=0

    soup= BeautifulSoup(driver.page_source, 'html.parser')

    jsonData = soup.text
    # parse x:
    json_text = json.loads(jsonData)
    # the result is a Python dictionary:
    # print(type(y["fullClassifications"][0]))
    #print(json_text["fullClassifications"][0])
    fullClassifications_data = json_text["fullClassifications"]
    for n in range(len(fullClassifications_data)):
        for key, value in fullClassifications_data[n].items():
            if (key == 'classification'):
                init_data_map()
                #print("data map initialized: ",data_map)
                for key1, value1 in value.items():

                    if (key1 == 'splits'):  # Split value is a list of dict().
                        split_data_map={}
                        for i in range(0, len(value1)):  # Iterating over the list "value1"
                            cumulative_time = ''
                            distance_covered = "Ok"
                            for key_value1, value_value1 in value1[i].items():  # Iterating the dict value1[i]
                                name_index=0

                                if (key_value1 == 'cumulativeTime'):
                                    cumulative_time=str(value_value1)
                                if(key_value1 == 'name'):
                                    distance_covered=str(value_value1)
                                    split_data_map[distance_covered]=cumulative_time
                        #print("split_data_map: ",split_data_map)

                        for split_data_map_key,split_data_map_value in split_data_map.items():
                            if('5k'==split_data_map_key):
                                if split_data_map_value != '':
                                    data_map['cumulativeTime_5k'] = split_data_map_value
                                data_map['name_5k'] = split_data_map_key
                            if ('10k' == split_data_map_key):
                                if (split_data_map_value != ''):
                                    data_map['cumulativeTime_10k'] = split_data_map_value
                                data_map['name_10k'] = split_data_map_key
                            if ('15k' == split_data_map_key):
                                if split_data_map_value != '':
                                    data_map['cumulativeTime_15k'] = split_data_map_value
                                data_map['name_15k'] = split_data_map_key
                            if ('20k' == split_data_map_key):
                                if (split_data_map_value != ''):
                                    data_map['cumulativeTime_20k'] = split_data_map_value
                                data_map['name_20k'] = split_data_map_key
                            if ('25k' == split_data_map_key):
                                if (split_data_map_value != ''):
                                    data_map['cumulativeTime_25k'] = split_data_map_value
                                data_map['name_25k'] = split_data_map_key
                            if ('Half' == split_data_map_key):
                                if (split_data_map_value != ''):
                                    data_map['cumulativeTime_half'] = split_data_map_value
                                data_map['name_half'] = split_data_map_key
                            if ('30k' == split_data_map_key):
                                if (split_data_map_value != ''):
                                    data_map['cumulativeTime_30k'] = split_data_map_value
                                data_map['name_30k'] = split_data_map_key
                            if ('35k' == split_data_map_key):
                                if (split_data_map_value != ''):
                                    data_map['cumulativeTime_35k'] = split_data_map_value
                                data_map['name_35k'] = split_data_map_key
                            if ('40k' == split_data_map_key):
                                if (split_data_map_value != ''):
                                    data_map['cumulativeTime_40k'] = split_data_map_value
                                data_map['name_40k'] = split_data_map_key
                            if ('Finish' == split_data_map_key):
                                if (split_data_map_value != ''):
                                    data_map['cumulativeTime_finish'] = split_data_map_value
                                data_map['name_finish'] = split_data_map_key
                    else:
                        if('gender'==key1):
                            if('1'==str(value1)):
                                data_map[key1] ='M'
                            elif ('2' == str(value1)):
                                data_map[key1] = 'F'
                        else:
                            data_map[key1]=str(value1)

                for data_key, data_value in data_map.items():
                    try:
                        worksheet.write(row, col_map.get(data_key), str(data_value))
                        col += 1
                    except:
                        print("Invalid Entry - try again ",data_value)
                row+=1
                col=0


def workbook_writer(workbook,worksheet,row,value):
    col=0
    worksheet.write(row, col, str(value))


if __name__=="__main__":
    #url = "https://results.sporthive.com/events/6587307641076513024/races/461111"

    for request_no in range(0 , no_of_requests+1, 15):
        # launch url
        #url = "https://eventresults-api.sporthive.com/api/events/6587307641076513024/races/461111/classifications/search?count=15&offset="+str(request_no) #Full marathon
        url= "https://eventresults-api.sporthive.com/api/events/6587307641076513024/races/461112/classifications/search?count=15&offset="+str(request_no) #Half marathon
        # create a new Firefox session
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get(url)
        scrape_data(driver)

    workbook.close()

