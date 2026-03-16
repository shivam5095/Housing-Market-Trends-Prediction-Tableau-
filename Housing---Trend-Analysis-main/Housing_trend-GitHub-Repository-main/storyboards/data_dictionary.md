# 📖 Housing Data Dictionary

This document serves as a comprehensive reference guide to the `Housing_Data.csv` dataset, explaining the meaning, data type, and context of each specific column.

The dataset consists of **21,609 records** and **31 columns** after preprocessing. Categorical variables such as 'Condition', 'Zipcode Group', and 'Waterfront View' have been one-hot encoded.

---

## 🏠 Core Property Features
| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| **Sale_Price** | Float (`float64`) | The final selling price of the property in USD. Note: Extreme outliers have been capped at the 95th percentile ($1,129,575.0) to prevent skewing models and visualizations. |
| **No of Bedrooms** | Integer (`int64`) | The total number of bedrooms in the house. |
| **No of Bathrooms** | Integer (`int64`) | The total number of bathrooms in the house. |
| **No of Floors** | Integer (`int64`) | The number of stories/floors the property has. |
| **Overall Grade** | Integer (`int64`) | An overall structural and design score assigned to the house based on the local grading system. higher score indicates better quality. |

## 📐 Area and Size Metrics
| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| **Flat Area (in Sqft)** | Float (`float64`) | The total interior living space of the house in square feet. |
| **Lot Area (in Sqft)** | Float (`float64`) | The total square footage of the land/lot that the property sits on. |
| **Area of the House from Basement (in Sqft)** | Float (`float64`) | The square footage of the house that is strictly above ground level (excludes the basement). |
| **Basement Area (in Sqft)** | Float (`float64`) | The square footage of the basement area. If 0, the property does not have a basement. |
| **Living Area after Renovation (in Sqft)** | Float (`float64`) | The living space area after the most recent property update or renovation. |
| **Lot Area after Renovation (in Sqft)** | Float (`float64`) | The lot area space after the most recent update or landscaping change. |

## 🕰 House Age and Renovation History
| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| **Age of House (in Years)** | Integer (`int64`) | The age of the home calculated from its year built. |
| **Ever_Renovated_Yes** | Integer (`int64`, binary) | A flag indicating whether the house has ever been renovated. `1` = Yes, `0` = No. |
| **Years Since Renovation** | Float (`float64`) | The number of years that have passed since the property was last renovated. `0` indicates no renovation or very recent. |

## 📍 Location and Accessibility
| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| **Latitude** | Float (`float64`) | The geographical latitudinal coordinate of the property. |
| **Longitude** | Float (`float64`) | The geographical longitudinal coordinate of the property. |
| **Waterfront_View_Yes** | Integer (`int64`, binary) | Specifies if the property overlooks a waterfront. `1` = Yes, `0` = No. |
| **No of Times Visited** | Integer (`int64`) | The frequency the property was viewed or toured by potential buyers before selling. |

---

## 📊 One-Hot Encoded Categorical Features

### House Condition
These binary variables represent the inspector's evaluation of the property's physical condition. Only one of these will equal `1` per row.
- **Condition_of_the_House_Excellent**: `1` if condition is excellent, else `0`.
- **Condition_of_the_House_Fair**: `1` if condition is fair, else `0`.
- **Condition_of_the_House_Good**: `1` if condition is good, else `0`.
- **Condition_of_the_House_Okay**: `1` if condition is merely okay, else `0`.

### Zipcode Groupings
The original property zipcodes have been clustered or categorized into 9 distinct geographic groups to improve model performance and simplify visualizations. Only one will equal `1` per row.
- **Zipcode_Group_Zipcode_Group_1** through **Zipcode_Group_Zipcode_Group_9** (9 separate columns mapping to location clusters).
