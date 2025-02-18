# NumPy-Pandas-Data-Analysis-Performance-Comparison

📌 Overview
This exercise is designed to enhance proficiency with the NumPy and Pandas APIs while enforcing a no-loops policy to encourage efficient, vectorized operations. The tasks include:

Signal Processing with NumPy – Simulating noisy sensor data and applying filters.
Weather Data Analysis – Computing precipitation statistics using NumPy & Pandas.
Data Transformation with Pandas – Converting raw climate data into structured monthly summaries.
Performance Comparison – Comparing Pandas' groupby & pivot to a loop-based approach.
🛠 Required Libraries
Ensure you have the following Python libraries installed:

sh
Copy
Edit
pip install numpy pandas statsmodels jupyter
📊 Task 1: Signal Processing with NumPy
Objective
Generate a sine wave signal and simulate noisy sensor data.
Apply a signal processing filter to reconstruct the clean signal.
Visualize the raw vs. filtered signal.
🚀 Running the Jupyter Notebook
Open signal-plot.ipynb in Jupyter.
Run all cells to generate the visualized output.
🌧 Task 2: Weather Data Analysis (NumPy)
Objective
Analyze precipitation data from monthdata.npz and compute:

City with lowest total precipitation
Average monthly precipitation
Average precipitation per city
Quarterly precipitation totals
🚀 Running the Script
sh
Copy
Edit
python3 np_summary.py
📊 Output
Prints required statistics, matching np_summary.txt.
📑 Task 3: Weather Data Analysis (Pandas)
Objective
Reproduce the NumPy calculations using Pandas, but with:

Labeled months & cities for improved readability.
More structured output in a Pandas DataFrame.
