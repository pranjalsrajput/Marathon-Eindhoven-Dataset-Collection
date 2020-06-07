# Web Scraping
To collect the complete data from the official website.

The program intercepts the request and reads all the data, and write it to a `.xls` file.



## Explaination

The request is intercepted first using the browser developer tool. The url of the request is then copied from the "Network" tab and the minimum, maximum and the total number of requests is also noted down. The code loops through all the requests one by one and the required data is extracted. The extracted data is then saved in a xls file.
