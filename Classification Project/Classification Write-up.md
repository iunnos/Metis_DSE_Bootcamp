## Abstract
Traditional fire alarms typically work in one of two ways: ionization or photoelectric. Ionization uses a small amount of radioactive material to measure the airflow between two electrically charged plates while photoelectric uses a a combination of light sources and refraction to detect smoke. 

The goal of this project is to use classification models to optimize the performance of smoke alarms that use air and temperature sensors rather than traditional fire alarm methods. I worked with data found on (Kaggle)[https://www.kaggle.com/datasets/deepcontractor/smoke-detection-dataset] based of reading from a DIY smoke alarm made using Arduino boards and various air and temperature sensors.

## Design
Successful modeling that would be deployed along with a smoke alarm made of an Arduino board and various sensors would allow for a more accurate and precise generation of fire alarms. This would potentially allow people to no longer worry about setting off their smoke alarm while cooking or while doing other day to day tasks. This would result in encouragement for more households to install and keep smoke alarms potentially saving lives.

## Data
The dataset contains 62630 readings from a sensor in various different environments, with 15 features measured. One row of data shows every second of a sensor's readings \(UTC\). The sensor detects temperature \(in degrees celsius\), air humidity, TVOC \(Total Volatile Organic Compounds\), eCO2 \(co2 equivalent concentration\), Raw H2, Raw Ethanol, Presure\[hPa\] \(Air Pressure\), PM 1.0, PM 2.5 \(particulate matter size\),NC0.5, NC1.0,	NC2.5 \(Number concentration of particulate matter\), CNT \(Sample counter\) and Fire Alarm \(1 if it goes off\).

## Algorithms
### Models
Logistic regression and gradient boosting models were made, and while the gradient boosting model out performed logistic regression models, I settled on the logistic regression model as being the final model due to considerations that this model would need to be make decisions quickly and wouldn't have a lot resources available to it to make these decisions. 

### Model Evaluation and Selection
The dataset was split into a 75/25 train vs test. While various metrics such as F1 score, probability, RMSE and MSE were looked at the metric that weighed most on my mind was precision. My goal was to minimize the number of false positives while ensuring that fires were still being detected all the time. 

## Final Logistic Regression scores:
- Test F1 Score: 0.99
- Test Precision Score: 1.00
- Test prediction time: 0.002 seconds

## Tools
- Numpy and Pandas for data manipulation
- Scikit-learn for modeling
- Matplotlib and Seaborn for plotting