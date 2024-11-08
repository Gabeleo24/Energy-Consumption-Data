# Energy Consumption Data
### AEP Hourly Energy Consumption Forecasting

**Project Overview**

This project involves analyzing and forecasting energy consumption data for American Electric Power (AEP) at an hourly granularity. The dataset includes power usage information in megawatts (MW) from December 31, 2004, onward. The goal of this project is to explore the temporal patterns in energy usage, identify factors influencing demand, and build predictive models to forecast future consumption.

**Dataset**

	•	File: AEP_hourly.csv
	•	Columns:
	•	Datetime: The timestamp of each hourly measurement (in the format YYYY-MM-DD HH:MM:SS).
	•	AEP_MW: Power usage in megawatts (MW) for the corresponding hour.

**Data Source**

The dataset was provided in the AEP_hourly.csv file, likely derived from historical records of American Electric Power’s energy load. This dataset is suitable for various time series analysis techniques due to its high frequency and extensive temporal coverage.

**Project Goals**

	1.	Explore and understand the characteristics of energy demand over time.
	2.	Identify any seasonality or trends in hourly, daily, and monthly usage.
	3.	Forecast future energy demand using advanced time series models.
	4.	Evaluate the accuracy of different predictive models.

**Project Structure**

	•	data/: Contains the raw AEP_hourly.csv file.
	•	notebooks/: Jupyter notebooks for exploratory data analysis (EDA), model development, and evaluation.
	•	src/: Scripts for data preprocessing, model training, and forecasting.
	•	results/: Output of model predictions, evaluation metrics, and visualizations.

_Getting Started_

**Prerequisites**

	•	Python 3.12.4
	•	Libraries: Install the required Python packages:

pip install pandas numpy matplotlib seaborn scikit-learn statsmodels



**Usage**

	1.	Clone the repository:

git clone https:https://github.com/Gabeleo24/Energy-Consumption-Data


	2.	Explore the data:
	•	Run the notebooks/EDA.ipynb to examine patterns and trends.
	3.	Preprocess the data:
	•	Use the src/preprocessing.py script to clean and prepare data for modeling.
	4.	Train and evaluate models:
	•	Run notebooks/Modeling.ipynb to apply time series forecasting techniques such as ARIMA, Prophet, or LSTM.

**Methodology**

	1.	Exploratory Data Analysis (EDA): Analyze patterns in energy usage to uncover trends and seasonality.
	2.	Model Selection: Test and evaluate models, including ARIMA, Prophet, and LSTM.
	3.	Evaluation: Use metrics like RMSE and MAE to assess forecasting accuracy.

**Results**

Results and visualizations of forecasting models will be saved in the results/ folder. Key findings and model performance metrics will be documented in this README after completion.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to adjust any sections to align with your specific findings and methodologies!
