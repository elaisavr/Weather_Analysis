# **Weather_Analysis**
Verona (IT) weather analysis of the last 20 years. 
 
## **Purpose**
This project aims to demonstrate how to get datas through a web request, create a readible and clean table from it and make an analysis on the subject.

Python and some of its main libraries for Data Analysis are used (Pandas, Numby, Datetime, Requests etc.)

In this case datas come from the Italian weather archive and are related to the features of the weather in Verona (Italy) of the past 20 years.

### **Main Steps:**
- Python script to get the datas related to the last 20 years - divided in 240 months urls - of Verona weather details through a request and put the text of the response in a final raw Data Frame saved to CSV before proceiding with data cleaning.

    ***code:*** **[`Weather get data_script.py`]**(https://github.com/elaisavr/Weather_Analysis/blob/main/Weather%20get%20data_script.py)
    
    ***output:*** **[Weather_raw df.csv]**(https://github.com/elaisavr/Weather_Analysis/blob/main/Weather_raw%20df.csv) <--please download and read for the data cleaning step

- Data Cleaning techniques applied to obtain the cleaned Data Frame saved to CSV ready to read for Data Analysis and Visualisation step.
    
    ***code:*** **[`Raw_Df_Data Cleaning.ipynb`]**(https://github.com/elaisavr/Weather_Analysis/blob/main/Raw_Df_Data%20Cleaning.ipynb)
    
    ***output:*** **[Weather_df.csv]**(https://github.com/elaisavr/Weather_Analysis/blob/main/Weather_df.csv) <--please download and read for next step

- Time Series and Data Visualization Analysis (WIP)

