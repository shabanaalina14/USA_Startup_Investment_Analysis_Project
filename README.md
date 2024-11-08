# USA_Startup_Investment_Analysis_Project
## Overview
This project performs multiple linear regression analysis to understand the factors influencing the profit of startups in the USA. By leveraging various features such as R&D Spend, Administration, and Marketing Spend, the model predicts the potential profit of startups.

Dataset
The dataset used in this project contains information about startups, including:

R&D Spend

Administration

Marketing Spend

State

Profit

Steps to Run the Project
1. Prerequisites
Make sure you have the following installed:

Python 3.x

Required libraries: pandas, numpy, scikit-learn

2. Clone the Repository
bash
git clone https://github.com/shabanaalina14/project_on_usa-_startup_investment.git
cd project_on_usa-_startup_investment
3. Install Dependencies
bash
pip install -r requirements.txt
4. Run the Analysis
Execute the script to perform multiple linear regression:

bash
python analysis.py
Explanation of the Code
data.csv: Contains the dataset with startup information.

analysis.py: Main script that:

Loads and preprocesses the data.

Converts categorical variables using one-hot encoding.

Splits the data into training and testing sets.

Trains multiple linear regression models.

Evaluates the models using R² score.

Results
The model's performance is evaluated based on the R² score, which indicates how well the model explains the variability of the profit based on the given features.

Conclusion
The multiple linear regression model provides insights into the factors impacting startup profits, helping stakeholders make informed investment decisions.
