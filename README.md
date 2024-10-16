# Sprint-4
This is my repository for TripleTen's Sprint 4 project.
I'll be looking at a data set for a car advertisement and will be using this data set to simulate random events through use of plotly.express, pandas, altair, streamlit.

Methods used:
* I used fillna() to replace any instances of NaN in the model_year, odometer, is_4wd, and cylinders columns to the integer 0.
* I used fillna() to replace any instances of NaN in the paint_color column with the string type "Unknown"
* I converted date_posted to datetime to avoid any possible complications with the column later on.
* I split the model column to seperate the make and model of the cars listed and placed all the makes of the cars in a new column designated as "make"
* I omited any vehicles that displayed a 0 in the model_year column and assigned this change to the variable known_years.
* I used .min() with the model_year to display the earliest known year of the vehicles displayed.
* I used .info to verify null counts.
* I used .median().reset_index() with the price column to get the median prices for my scatterplot and assigned this change to a new dataframe variable known_median.

Checkbox:
I placed a checkbox to switch between vehicle make and vehicle model on the scatterplot.

Conclusion:
The data seems to show that the bulk of inventory will sell between two to five weeks of being listed and that the dealership puts a higher price point towards Trucks and SUVs, presumably because of demands of the demographics of the area or possibly the geographical region requires it to ease difficulty of travel.