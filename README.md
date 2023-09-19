# **Weather_Analysis**
Verona (IT) weather analysis of the last 20 years. 
 
## **Purpose**
This project aims to demonstrate how to get datas through a web request, create a readible and clean table from it and make an analysis on the subject.

Python and some of its main libraries for Data Analysis are used (Pandas, Numby, Datetime, Requests etc.)

In this case datas come from the Italian weather archive and are related to the features of the weather in Verona (Italy) of the past 20 years.

### **Main Steps:**
1. Python script to get datas from the Italian Web weather archive of to the last 20 years in Verona (divided in 240 months endpoints) - through a request and transform the text response in a raw Data Frame saved to CSV before proceiding with data cleaning.

    - ***code:***  `Weather get data_script.py` (https://github.com/elaisavr/Weather_Analysis/blob/main/Weather%20get%20data_script.py)
    
    - ***output:*** [Weather_raw df.csv] (https://github.com/elaisavr/Weather_Analysis/blob/main/Weather_raw%20df.csv) <--please download and read for the data cleaning step

2. Data Cleaning techniques applied to raw Data Frame to obtain a final cleaned Data Frame saved to CSV ready to be read for Data Analysis and Visualisation step.
    
    - ***code:*** `Raw_Df_Data Cleaning.ipynb` (https://github.com/elaisavr/Weather_Analysis/blob/main/Raw_Df_Data%20Cleaning.ipynb)
    
    - ***output:*** [Weather_df.csv] (https://github.com/elaisavr/Weather_Analysis/blob/main/Weather_df.csv) <--please download and read for next step

3. Weather Analysis - Data Visualization exercise to show ho to plot some simple charts with python main data visualization libraries such as Seaborn and Matplotlib. Please save and read [Weather_df.csv] (https://github.com/elaisavr/Weather_Analysis/blob/main/Weather_df.csv) before run this notebook. 

    - ***code:*** `Weather_Data_Visualization.ipynb` (https://github.com/elaisavr/Weather_Analysis/blob/main/Raw_Df_Data%20Cleaning.ipynb)
    
    - ***output1:*** ![Avg_temp_20y_lineplot](https://github.com/elaisavr/Weather_Analysis/blob/main/Charts%20figure/AVG_Temp_20y.jpg)

    - ***output2:*** ![Avg_seasonal_temp_20y_lineplot](https://github.com/elaisavr/Weather_Analysis/blob/main/Charts%20figure/AVG_Seasonal_Temp_20y.jpg)

    - ***output3:*** ![Avg_temp_20y_barplot](https://github.com/elaisavr/Weather_Analysis/blob/main/Charts%20figure/AVG_Temp_20y_bars.jpg)

    - ***output4:*** ![Precipitation_mm_year_barplot](https://github.com/elaisavr/Weather_Analysis/blob/main/Charts%20figure/Rain_mm.jpg)

    - ***output5:*** ![Precipitation_mm_year_seasonal_barplot](https://github.com/elaisavr/Weather_Analysis/blob/main/Charts%20figure/Rain_mm_season.jpg)
