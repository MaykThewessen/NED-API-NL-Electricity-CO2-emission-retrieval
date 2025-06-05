**🇳🇱 NED.nl CO₂ Emissions & Electricity Production Data Extractor**

This Python script retrieves electricity production data from the Nationaal Energie Dashboard (NED.nl) via its API. It downloads quarter-hourly production data for a full calendar year and calculates:
	•	Total CO₂ emissions per 15-minute time block
	•	Specific emissions in kgCO₂ per kWh generated (average per 15-minute block)

📊 Features
	•	Retrieves data in 15-minute intervals
	•	Aggregates CO₂ emissions and electricity production volumes
	•	Exports results to a timestamped Excel file
	•	Designed for full-year analysis with automated batching to bypass API limits

🛠 Requirements
	•	Python 3.8+
	•	API key from api.ned.nl
	•	pip install -r requirements.txt

Python Packages Used

pandas
requests
python-dotenv

🔐 Setup
	1.	Clone this repo.
	2.	Create a .env file in the root directory with your API key:

NED_API_KEY=your_actual_api_key_here

	3.	Run the script:

python nednlAPI_CO2_Benke_working.py

📁 Output

The script exports an Excel file:

data_export_NED_CO2_20240101_to_20241231_15min.xlsx

Each row contains:

Column	Description
capacity	Installed capacity in MW
volume	Electricity produced in MWh
percentage	Share of total capacity used
emission	Total CO₂ emitted in kg
emissionfactor	CO₂ per kWh generated (kgCO₂/kWh)
validfrom	Timestamp (start of 15-min block)

⚠️ Notes
	•	The NED API limits exports to 144 datapoints (6 days of hourly data, or 1 day of 15-min data). This script automatically steps through the year in 6-day intervals.
	•	Be mindful of API rate limits.

🧑‍💻 Author

Created by Benke — for energy modeling and transparency in Dutch grid emissions 🇳🇱⚡

⸻

Let me know if you’d like this as a markdown file or want a diagram/graph for the repo as well. ￼
