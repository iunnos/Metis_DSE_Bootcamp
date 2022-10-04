# Question
- My project will be based on a Smoke Detector's readings to determine if there is a fire or not (ie. should the fire alarm be triggered)
- Improved processing for fire alarms could help to avoid false alarms (such as while cooking) and improve the sensitivity to actual fires

# Data Description
- My data was found on [Kaggle](https://www.kaggle.com/datasets/deepcontractor/smoke-detection-dataset)
- One row of data shows every second of a sensor's readings. The sensor detects temperature, humidity, TVOC \(Total Volatile Organic Compounds\), eCO2 \(co2 equivalent concentration\), Raw H2, Raw Ethanol, Presure\[hPa\] \(Air Pressure\), PM 1.0, PM 2.5 \(particulate matter size\),NC0.5, NC1.0,	NC2.5 \(Number concentration of particulate matter\), CNT \(Sample counter\) and Fire Alarm \(1 if it goes off\)
- I'll be implimenting a Logistic Regression Model to start.

# Tools
- I'll be using SKLearn's Logistic Regression, Pandas, and Numpy

# MVP Goal
- The MVP will have an initial Logistic Regression Model and it's initial scoring