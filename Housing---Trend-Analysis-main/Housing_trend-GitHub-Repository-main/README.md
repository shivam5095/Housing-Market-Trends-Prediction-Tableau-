🏠 Housing Market Analysis using Tableau

Live Demo on Vercel
📌 Project Overview

In this project for ABC Company, the goal is to address challenges in understanding the factors that influence house prices and sales trends. By analyzing comprehensive housing data—including total sales by years since renovation, house age distribution by structural features (bathrooms, bedrooms, and floors), and the impact of renovations on house age—the company aims to uncover key insights.

Utilizing Tableau for this analysis, the objective is to visualize and interpret patterns in the housing market to inform strategic decisions, optimize pricing strategies, and enhance overall market competitiveness. Key stakeholders include real estate analysts, marketing teams, and company executives, all of whom will benefit from a deeper understanding of housing market dynamics.


🎯 Project Objectives

The primary objectives of this project are:

    Analyze housing sales data to identify trends and patterns.
    Understand how renovation affects house prices.
    Study the relationship between house age and property features.
    Visualize housing characteristics such as bedrooms, bathrooms, and floors.
    Build an interactive Tableau dashboard for better market insights.

🛤️ Project Phases

To accomplish our objectives, the project follows this end-to-end workflow:

    Data Collection: Collect the .csv dataset and connect the data with Tableau.
    Data Preparation: Clean and prepare the data specifically for visualization.
    Data Visualizations: Create targeted visualization scenarios to uncover insights.
    Dashboard: Design a responsive, centralized dashboard.
    Storyboard: Create a narrative storyboard tying the insights together.
    Performance Testing: Optimize the utilization of data filters, calculated fields, and graphics.
    Web Integration: Publish the visualizations and embed the dashboard and story within a web UI using Flask.

📊 Dataset Information

    Dataset Name: Housing_Data.csv
    Total Records: 21,609
    Total Columns: 31

The dataset contains detailed information about housing properties, including price, structure, renovation status, and location attributes.
Key Attributes
Attribute 	Description
Sale Price 	Selling price of the house
Bedrooms 	Number of bedrooms
Bathrooms 	Number of bathrooms
Flat Area 	Living area of the house (sqft)
Lot Area 	Total lot area (sqft)
Floors 	Number of floors
House Age 	Age of the house
Years Since Renovation 	Years passed since last renovation
Above Ground Area 	Area of house above basement
Basement Area 	Basement size
Latitude / Longitude 	Geographic coordinates
Property Condition 	Condition category of the house
Waterfront View 	Whether the property has a waterfront view
Zipcode Groups 	Location category
🧹 Data Cleaning and Preparation

Data cleaning was performed in Tableau to ensure the dataset is structured and ready for visualization. This included verifying data structures, checking value distributions, and exploring attributes.

Field Renaming for Readability:

    No of Bedrooms ➡️ Bedrooms
    No of Bathrooms ➡️ Bathrooms
    Flat Area (in Sqft) ➡️ Flat Area
    Lot Area (in Sqft) ➡️ Lot Area
    No of Floors ➡️ Floors
    Area of the House from Basement (in Sqft) ➡️ Above Ground Area

📈 Data Visualizations (Scenarios)

The following key visual scenarios were created in Tableau:


Scenario 1: Overall Data Overview

This visualization presents a summary of the dataset, showing the count of transformed housing data records, the average sales price, and the total area of houses from the basement in square feet. This overview provides a quick snapshot of the dataset's scale and key metrics, offering stakeholders a foundational understanding of the data being analyzed.
Scenario 2: Total Sales by Years Since Renovation

This histogram illustrates the distribution of total sales based on the number of years since a house was renovated. The bars represent different sales price bins, highlighting how recently renovated houses correlate with varying price ranges. This scenario helps stakeholders understand the impact of renovations on house prices and identify trends in buyer preferences regarding renovated homes.
Scenario 3: Distribution of House Age by Renovation Status

This pie chart shows the distribution of houses based on their age and renovation status. Each segment of the pie represents a different age group, providing insight into how the age of houses is spread across the dataset and the proportion of houses that have been renovated versus those that have not. This visualization assists in assessing the age characteristics of the housing inventory and the prevalence of renovations.
Scenario 4: House Age Distribution by Number of Bathrooms, Bedrooms, and Floors

This grouped bar chart displays the distribution of house ages categorized by the number of bathrooms, bedrooms, and floors. It shows how houses of different ages are distributed according to these attributes, offering a detailed view of how house features vary with age over time.
🧠 Dashboard & Expected Insights

The Tableau dashboard integrates these visualizations into an interactive interface featuring filters, clear layouts, and visual comparisons. The project helps answer questions such as:

    Do renovated houses sell at higher prices?
    How does house age affect property characteristics?
    What types of houses dominate the housing market?
    How do structural features influence housing prices?

🛠 Tools and Technologies
Tool 	Purpose
Tableau Public 	Data visualization and dashboard creation
GitHub 	Version control and project collaboration
Flask (Python) 	Web UI integration and embedding
CSV 	Housing data source
🚀 Future Improvements

Potential enhancements for this project include:

    Integration with real-time housing data APIs.
    Machine learning models for predictive price analysis.
    Advanced geographic mapping of housing prices.

📜 License: This project is for educational and analytical purposes.

