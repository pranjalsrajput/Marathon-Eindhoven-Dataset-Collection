# Web Scraping
To collect the complete data from the official website of the event.
`Selenium Webdriver and Beautiful soup` are used to scrape the data, the browser used was Chrome.
The program intercepts the request and reads all the data, and write it to a `.xls` file.



## Explaination

The request is intercepted first using the browser developer tool. The url of the request is then copied from the "Network" tab and the minimum, maximum and the total number of requests is also noted down. The code loops through all the requests one by one using selenium webdriver.The data on the source page is then read using Beautiful soup, which gives the output in the json format. The json is then read to get the required information. The extracted data is then saved in a xls file.
