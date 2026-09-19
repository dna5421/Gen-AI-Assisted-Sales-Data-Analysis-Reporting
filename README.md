## 🎯 Gen-AI-Assisted Sales Data Analysis & Reporting

## 📝 Project Overview

This project analyzes sales transaction data, derives business KPIs, visualizes trends, and uses a generative AI model to produce a management-friendly business report. It combines traditional data analysis with AI-assisted summarization to convert raw sales data into actionable recommendations.

 ## ✨ Problem Statement

 Businesses often have raw sales records but struggle to turn them into clear insights about revenue performance, product trends, regional differences, customer retention risk, and operational opportunities.  This project addresses that gap by automating data cleaning, KPI calculation, chart generation, and AI-generated executive reporting from sales data.

 ## 📊 Dataset
 
 ✅ The project uses a sales dataset stored in sales_data.csv. The dataset includes 20 orders collected across January–August 2025 and contains:
 
  • OrderID
  • OrderDate
  • CustomerName
  • Region
  • Category
  • Product
  • Quantity
  • UnitPrice
  • Discount


 
 ✅ The data reflects a business with:

  •  20 total orders
  •  157 total units sold
  •  20 unique customers
  •  Revenue distributed across regions, categories, and products


  ## ⚒️ Tools and Technologies

  • Python
  • Pandas
  • Matplotlib
  • Seaborn
  • OpenPyXL
  • Google GenAI / Gemini API
  • Python-dotenv
  • CSV and Excel output generation

  
  ## Ⓜ️ METHODS

  1 Data loading and validation

  • Read the CSV file
  • Check for missing or invalid records
  • Remove duplicate rows and clean date/number fields
  
  2 Feature engineering

  • Compute GrossSales
  • Compute DiscountAmount
  • Compute Revenue
  • Create month and year columns for trend analysis

  3 Business analytics

  • Total revenue
  • Average order value
  • Revenue by region
  • Revenue by category
  • Top and low-performing products
  • Customer contribution analysis
  • Discount impact analysis

  4 Visualization

  • Monthly sales trend chart
  • Region-wise revenue chart
  • Top product chart
  • Correlation heatmap

  5 AI-assisted report generation

  • Convert analysis metrics into a JSON payload
  • Send the data to Gemini with a business-analysis prompt
  • Generate a management summary and recommendations based only on the supplied numbers

 ## 📊 Key Insights

 ✅ The generated report highlights several important findings:

  • Total net revenue: 1,373,850
  • Average order value: 68,692.5
  • Electronics is the dominant category, contributing 78.89% of total revenue
  • North is the strongest region, contributing 40.44% of revenue
  • East has the lowest revenue despite selling a high volume of units
  • Top products include Mobile, Laptop, and Monitor
  • Customer retention is a major risk: 100% of customers are one-time buyers
  • Revenue declined in recent months, indicating a possible downward demand trend
  • Low-performing products such as Printer Paper generate quantity but weak revenue

  ## 🧑‍💼 Model / Output

 ✅ The project uses Google Gemini models for report generation. The script attempts several model options:

  • gemini-3.6-flash
  • gemini-3.5-flash
  • gemini-3.1-flash-lite
  • gemini-2.5-flash
  
 ✅ Generated outputs include:

  • cleaned_sales_data.csv
  • sales_analysis_report.xlsx
  • monthly_sales.png
  • regional_sales.png
  • product_sales.png
  • correlation_heatmap.png
  • genai_sales_report.txt

  ## 🚀 How To Run This Project

  ✅ Clone the repository
  ✅ Create a virtual environment (optional but recommended)
  ✅ Install dependencies: pip install pandas matplotlib seaborn python-dotenv google-genai openpyxl
  ✅ Create a .env file in the project root with: GEMINI_API_KEY=your_api_key_here
  ✅ Ensure sales_data.csv is present in the project root or in the data/ folder
  ✅ Run: python sales_genai_analysis.py

  6 The script will:
  
  • clean the data
  • generate charts
  • produce Excel analytics
  • call Gemini for AI-powered insights
  • save all outputs to the output/ directory

  ## 🎯 Results

 ✅ The project successfully produces:

  • A clean dataset for analysis
  • Revenue and trend analysis
  • Region/category/product insights
  • Executive-level recommendations
  • Business-friendly AI summary report
  • Visual dashboard elements for stakeholder review

 ## ✨ CONCLUSION

  This project demonstrates how data analytics and generative AI can be combined to create an intelligent business reporting workflow. It turns raw transaction data into structured insight, visual           evidence, and actionable recommendations without requiring manual reporting from scratch.


  ## 🏢 Future Work

  • Add real-world sales data importing from APIs or databases
  • Integrate forecasting models for future revenue prediction
  • Build an interactive dashboard using Streamlit or Dash
  • Add customer segmentation and churn analysis
  • Improve AI prompt design for more nuanced executive reporting
  • Include region-wise and product-wise forecasting
  • Add automated email or PDF report generation

  ## 📡 Author & Contact

  👤 Author: dna5421
  📧 GitHub Profile: https://github.com/dna5421
  🔗 Repository: https://github.com/dna5421/Gen-AI-Assisted-Sales-Data-Analysis-Reporting
  
