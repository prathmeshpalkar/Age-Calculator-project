#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Get user input
age = float(input("Enter the person's age in years: "))
selected_units = input("Enter the desired time units (months/weeks/days/hours/minutes/seconds): ")

# Calculate For Seconds
total_seconds = age * 365.25 * 24 * 60 * 60

# Convert To the months,Weeks,Days,Hours,Minutes,Seconds20
if selected_units == "months":
    total_units = age * 12
elif selected_units == "weeks":
    total_units = age * 365.25 / 7
elif selected_units == "days":
    total_units = age * 365.25
elif selected_units == "hours":
    total_units = age * 365.25 * 24
elif selected_units == "minutes":
    total_units = age * 365.25 * 24 * 60
elif selected_units == "seconds":
    total_units = total_seconds
else:
    print("Invalid time unit selected. Please choose from months/weeks/days/hours/minutes/seconds.")
    total_units = None

# result
if total_units is not None:
    print(f"The person has lived for {total_units} {selected_units}.")


# In[ ]:





# In[ ]:




