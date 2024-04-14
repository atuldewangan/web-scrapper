# Push-Notification

## Problem
 A scraping tool using Python FastAPI framework to automate the information scraping process from the target website.

## Instructions 

1.  Start this Application
    -  `uvicorn app.main:app`
    
2.  Create Users
    -   endpoint : `http://127.0.0.1:8000/scrape`
    -   Request Type : POST
    -   Headers : 
          ```
            x-token:SAMPLE_STATIC_TOKEN
          ```
    -   Query Param : 
        ```
            num_pages: number of pages from which we need to scrape the information
            proxy:  proxy string can use for scraping
        ```   
    -   Response :
     
           ```
            {
                "message": "24 products scraped and updated in the DB."
            }

          ```
    -   Request CURL :
     
           ```
                curl --location --request POST 'http://127.0.0.1:8000/scrape?proxy=&num_pages=1' \
                --header 'x-token: SAMPLE_STATIC_TOKEN'
          ```
