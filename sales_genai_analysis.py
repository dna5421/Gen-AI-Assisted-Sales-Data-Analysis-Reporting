import os
import json
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from google import genai
from dotenv import load_dotenv


# ============================================================
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

DATA_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

DATA_FILE = DATA_DIR / "sales_data.csv"

# ============================================================
# 2. LOAD GEMINI API KEY
# ============================================================

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file."
    )

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# ============================================================
# 3. CHECK / CREATE SALES DATA
# ============================================================

print("\n======================================")
print("CHECKING SALES DATA")
print("======================================")

# First check data folder
if DATA_FILE.exists():

    print(
        f"Sales file found:\n{DATA_FILE}"
    )

# If not found, check project folder
else:

    ROOT_FILE = BASE_DIR / "sales_data.csv"

    if ROOT_FILE.exists():

        print(
            f"Sales file found in project folder:\n{ROOT_FILE}"
        )

        DATA_FILE = ROOT_FILE

    # If still not found, create sample data
    else:

        print(
            "\nWARNING: sales_data.csv not found."
        )

        print(
            "Creating sample sales_data.csv..."
        )

        sample_data = [
            [1001, "2025-01-05", "Amit Sharma", "North",
             "Electronics", "Laptop", 2, 55000, 0.05],

            [1002, "2025-01-08", "Priya Singh", "South",
             "Furniture", "Office Chair", 5, 7500, 0.10],

            [1003, "2025-01-15", "Rahul Verma", "West",
             "Electronics", "Mobile", 4, 25000, 0.05],

            [1004, "2025-02-03", "Sneha Gupta", "East",
             "Office Supplies", "Printer Paper", 20, 450, 0.02],

            [1005, "2025-02-10", "Arjun Patel", "North",
             "Electronics", "Monitor", 3, 18000, 0.08],

            [1006, "2025-02-18", "Neha Sharma", "South",
             "Furniture", "Desk", 2, 15000, 0.05],

            [1007, "2025-03-02", "Rohit Kumar", "West",
             "Electronics", "Laptop", 1, 55000, 0.03],

            [1008, "2025-03-12", "Pooja Singh", "East",
             "Office Supplies", "Printer", 2, 12000, 0.07],

            [1009, "2025-03-20", "Vikas Gupta", "North",
             "Electronics", "Mobile", 6, 25000, 0.05],

            [1010, "2025-04-05", "Anjali Verma", "South",
             "Furniture", "Office Chair", 4, 7500, 0.10],

            [1011, "2025-04-15", "Manish Patel", "West",
             "Electronics", "Monitor", 5, 18000, 0.05],

            [1012, "2025-04-25", "Kavita Sharma", "East",
             "Office Supplies", "Printer Paper", 30, 450, 0.02],

            [1013, "2025-05-05", "Ravi Kumar", "North",
             "Electronics", "Laptop", 3, 55000, 0.04],

            [1014, "2025-05-15", "Simran Gupta", "South",
             "Furniture", "Desk", 4, 15000, 0.06],

            [1015, "2025-06-01", "Akash Verma", "West",
             "Electronics", "Mobile", 8, 25000, 0.05],

            [1016, "2025-06-15", "Nisha Patel", "East",
             "Office Supplies", "Printer", 3, 12000, 0.05],

            [1017, "2025-07-05", "Karan Sharma", "North",
             "Electronics", "Monitor", 6, 18000, 0.07],

            [1018, "2025-07-20", "Riya Singh", "South",
             "Furniture", "Office Chair", 7, 7500, 0.08],

            [1019, "2025-08-10", "Varun Gupta", "West",
             "Electronics", "Laptop", 2, 55000, 0.05],

            [1020, "2025-08-25", "Meena Sharma", "East",
             "Office Supplies", "Printer Paper", 40, 450, 0.03],
        ]

        columns = [
            "OrderID",
            "OrderDate",
            "CustomerName",
            "Region",
            "Category",
            "Product",
            "Quantity",
            "UnitPrice",
            "Discount"
        ]

        sample_df = pd.DataFrame(
            sample_data,
            columns=columns
        )

        sample_df.to_csv(
            DATA_FILE,
            index=False
        )

        print(
            f"\nSample file created:\n{DATA_FILE}"
        )


# ============================================================
# 4. LOAD SALES DATA
# ============================================================

print("\n======================================")
print("LOADING SALES DATA")
print("======================================")

df = pd.read_csv(DATA_FILE)

print("\nFirst 5 rows:")
print(df.head())

print(
    f"\nTotal rows: {len(df)}"
)


# ============================================================
# 5. DATA CLEANING
# ============================================================

print("\n======================================")
print("DATA CLEANING")
print("======================================")

# Remove duplicates
df = df.drop_duplicates()

# Convert date
df["OrderDate"] = pd.to_datetime(
    df["OrderDate"],
    errors="coerce"
)

# Convert numeric fields
df["Quantity"] = pd.to_numeric(
    df["Quantity"],
    errors="coerce"
)

df["UnitPrice"] = pd.to_numeric(
    df["UnitPrice"],
    errors="coerce"
)

df["Discount"] = pd.to_numeric(
    df["Discount"],
    errors="coerce"
)

# Remove invalid rows
df = df.dropna(
    subset=[
        "OrderID",
        "OrderDate",
        "Product",
        "Quantity",
        "UnitPrice"
    ]
)

# Missing discount = 0
df["Discount"] = df["Discount"].fillna(0)

# Valid values only
df = df[df["Quantity"] > 0]

df = df[df["UnitPrice"] > 0]

# Discount between 0 and 1
df["Discount"] = df["Discount"].clip(
    0,
    1
)


# ============================================================
# 6. CREATE BUSINESS METRICS
# ============================================================

print("\n======================================")
print("CREATING BUSINESS METRICS")
print("======================================")

df["GrossSales"] = (
    df["Quantity"] *
    df["UnitPrice"]
)

df["DiscountAmount"] = (
    df["GrossSales"] *
    df["Discount"]
)

df["Revenue"] = (
    df["GrossSales"] -
    df["DiscountAmount"]
)

df["Month"] = (
    df["OrderDate"]
    .dt.to_period("M")
    .astype(str)
)

df["Year"] = (
    df["OrderDate"]
    .dt.year
)


# ============================================================
# 7. OVERALL KPIs
# ============================================================

total_revenue = df["Revenue"].sum()

total_orders = df["OrderID"].nunique()

total_quantity = df["Quantity"].sum()

total_discount = df["DiscountAmount"].sum()

unique_customers = df["CustomerName"].nunique()

average_order_value = (
    total_revenue / total_orders
    if total_orders > 0
    else 0
)


print("\n======================================")
print("BUSINESS KPIs")
print("======================================")

print(
    f"Total Revenue: ₹{total_revenue:,.2f}"
)

print(
    f"Total Orders: {total_orders}"
)

print(
    f"Total Quantity: {total_quantity}"
)

print(
    f"Average Order Value: ₹{average_order_value:,.2f}"
)

print(
    f"Total Discount: ₹{total_discount:,.2f}"
)

print(
    f"Unique Customers: {unique_customers}"
)


# ============================================================
# 8. MONTHLY SALES
# ============================================================

monthly_sales = (
    df.groupby("Month")
      .agg(
          Revenue=("Revenue", "sum"),
          Orders=("OrderID", "nunique"),
          Quantity=("Quantity", "sum")
      )
      .reset_index()
)

monthly_sales["Growth_%"] = (
    monthly_sales["Revenue"]
    .pct_change()
    .mul(100)
    .round(2)
)


# ============================================================
# 9. REGIONAL ANALYSIS
# ============================================================

regional_sales = (
    df.groupby("Region")
      .agg(
          Revenue=("Revenue", "sum"),
          Orders=("OrderID", "nunique"),
          Quantity=("Quantity", "sum")
      )
      .reset_index()
      .sort_values(
          "Revenue",
          ascending=False
      )
)

regional_sales["Revenue_%"] = (
    regional_sales["Revenue"] /
    regional_sales["Revenue"].sum() *
    100
).round(2)


# ============================================================
# 10. CATEGORY ANALYSIS
# ============================================================

category_sales = (
    df.groupby("Category")
      .agg(
          Revenue=("Revenue", "sum"),
          Orders=("OrderID", "nunique"),
          Quantity=("Quantity", "sum")
      )
      .reset_index()
      .sort_values(
          "Revenue",
          ascending=False
      )
)


# ============================================================
# 11. PRODUCT ANALYSIS
# ============================================================

product_sales = (
    df.groupby("Product")
      .agg(
          Revenue=("Revenue", "sum"),
          Quantity=("Quantity", "sum"),
          Orders=("OrderID", "nunique")
      )
      .reset_index()
      .sort_values(
          "Revenue",
          ascending=False
      )
)

top_products = product_sales.head(10)

low_products = (
    product_sales
    .sort_values("Revenue")
    .head(10)
)


# ============================================================
# 12. CUSTOMER ANALYSIS
# ============================================================

customer_sales = (
    df.groupby("CustomerName")
      .agg(
          Revenue=("Revenue", "sum"),
          Orders=("OrderID", "nunique"),
          Quantity=("Quantity", "sum")
      )
      .reset_index()
      .sort_values(
          "Revenue",
          ascending=False
      )
)


# ============================================================
# 13. DISCOUNT ANALYSIS
# ============================================================

discount_analysis = (
    df.groupby("Category")
      .agg(
          GrossSales=("GrossSales", "sum"),
          DiscountAmount=("DiscountAmount", "sum"),
          Revenue=("Revenue", "sum")
      )
      .reset_index()
)

discount_analysis["Discount_%"] = (
    discount_analysis["DiscountAmount"] /
    discount_analysis["GrossSales"] *
    100
).round(2)


# ============================================================
# 14. CREATE CHART - MONTHLY SALES
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    monthly_sales["Month"],
    monthly_sales["Revenue"],
    marker="o"
)

plt.title(
    "Monthly Revenue Trend"
)

plt.xlabel("Month")

plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_sales.png",
    dpi=300
)

plt.close()


# ============================================================
# 15. CREATE CHART - REGION
# ============================================================

plt.figure(figsize=(9, 6))

sns.barplot(
    data=regional_sales,
    x="Region",
    y="Revenue"
)

plt.title(
    "Revenue by Region"
)

plt.xlabel("Region")

plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "regional_sales.png",
    dpi=300
)

plt.close()


# ============================================================
# 16. CREATE CHART - PRODUCTS
# ============================================================

plt.figure(figsize=(10, 6))

sns.barplot(
    data=top_products,
    x="Revenue",
    y="Product"
)

plt.title(
    "Top Products by Revenue"
)

plt.xlabel("Revenue")

plt.ylabel("Product")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "product_sales.png",
    dpi=300
)

plt.close()


# ============================================================
# 17. CORRELATION HEATMAP
# ============================================================

correlation_columns = [
    "Quantity",
    "UnitPrice",
    "Discount",
    "GrossSales",
    "DiscountAmount",
    "Revenue"
]

correlation_matrix = (
    df[correlation_columns]
    .corr()
)

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f"
)

plt.title(
    "Sales Metrics Correlation"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "correlation_heatmap.png",
    dpi=300
)

plt.close()


# ============================================================
# 18. SAVE CLEANED CSV
# ============================================================

cleaned_file = (
    OUTPUT_DIR /
    "cleaned_sales_data.csv"
)

df.to_csv(
    cleaned_file,
    index=False
)


# ============================================================
# 19. CREATE EXCEL REPORT
# ============================================================

print("\n======================================")
print("CREATING EXCEL REPORT")
print("======================================")

excel_file = (
    OUTPUT_DIR /
    "sales_analysis_report.xlsx"
)

with pd.ExcelWriter(
    excel_file,
    engine="openpyxl"
) as writer:

    df.to_excel(
        writer,
        sheet_name="Cleaned Data",
        index=False
    )

    monthly_sales.to_excel(
        writer,
        sheet_name="Monthly Sales",
        index=False
    )

    regional_sales.to_excel(
        writer,
        sheet_name="Regional Analysis",
        index=False
    )

    category_sales.to_excel(
        writer,
        sheet_name="Category Analysis",
        index=False
    )

    product_sales.to_excel(
        writer,
        sheet_name="Product Analysis",
        index=False
    )

    customer_sales.to_excel(
        writer,
        sheet_name="Customer Analysis",
        index=False
    )

    discount_analysis.to_excel(
        writer,
        sheet_name="Discount Analysis",
        index=False
    )


print(
    f"Excel file created:\n{excel_file}"
)


# ============================================================
# 20. PREPARE DATA FOR GEMINI
# ============================================================

analysis_data = {

    "overall_kpis": {

        "total_revenue":
            round(float(total_revenue), 2),

        "total_orders":
            int(total_orders),

        "total_quantity":
            int(total_quantity),

        "average_order_value":
            round(float(average_order_value), 2),

        "total_discount":
            round(float(total_discount), 2),

        "unique_customers":
            int(unique_customers)
    },

    "monthly_sales":
        monthly_sales.to_dict(
            orient="records"
        ),

    "regional_sales":
        regional_sales.to_dict(
            orient="records"
        ),

    "category_sales":
        category_sales.to_dict(
            orient="records"
        ),

    "top_products":
        top_products.to_dict(
            orient="records"
        ),

    "low_products":
        low_products.to_dict(
            orient="records"
        ),

    "top_customers":
        customer_sales.head(10).to_dict(
            orient="records"
        ),

    "discount_analysis":
        discount_analysis.to_dict(
            orient="records"
        )
}


# ============================================================
# 21. GEMINI PROMPT
# ============================================================

prompt = f"""
You are an experienced Business Analyst.

Analyze the following sales data.

DATA:

{json.dumps(
    analysis_data,
    indent=2,
    default=str
)}

Create a professional management-friendly report.

Include:

1. Executive Summary
2. Overall Sales Performance
3. Revenue Trend Analysis
4. Best Performing Region
5. Weakest Performing Region
6. Best Performing Category
7. Top 5 Products
8. Low Performing Products
9. Customer and Order Insights
10. Discount Impact
11. Business Risks
12. Three Actionable Recommendations

Rules:

- Do not invent numbers.
- Use only the supplied data.
- Mention actual values where useful.
- Mention percentages where available.
- Use simple business language.
- Give practical recommendations.
"""


# ============================================================
# 22. GEMINI AI ANALYSIS
# ============================================================

import time

print("\n======================================")
print("GENERATING GEMINI AI INSIGHTS")
print("======================================")

# Current Gemini models
# We try them one by one if a temporary 503 error occurs.

GEMINI_MODELS = [
    "gemini-3.6-flash",
    "gemini-3.5-flash",
    "gemini-3.1-flash-lite",
    "gemini-2.5-flash"
]

ai_report = None

for model_name in GEMINI_MODELS:

    print(
        f"\nTrying Gemini model: {model_name}"
    )

    # Retry same model up to 3 times
    for attempt in range(1, 4):

        try:

            print(
                f"Attempt {attempt}/3..."
            )

            response = client.models.generate_content(
                model=model_name,
                contents=prompt
            )

            # Check response
            if response and response.text:

                ai_report = response.text

                print(
                    f"\nSUCCESS: {model_name}"
                )

                break

        except Exception as e:

            error_message = str(e)

            print(
                f"\nGemini Error: {error_message}"
            )

            # ------------------------------------------------
            # 503 = Temporary high demand
            # ------------------------------------------------

            if (
                "503" in error_message
                or "UNAVAILABLE" in error_message
                or "high demand" in error_message.lower()
            ):

                print(
                    "\nGemini server is busy."
                )

                if attempt < 3:

                    wait_time = 5 * attempt

                    print(
                        f"Waiting {wait_time} seconds..."
                    )

                    time.sleep(
                        wait_time
                    )

                    continue

                else:

                    print(
                        f"Model {model_name} "
                        "is currently unavailable."
                    )

                    break

            # ------------------------------------------------
            # Other errors
            # ------------------------------------------------

            else:

                print(
                    f"Skipping model: {model_name}"
                )

                break

    # If successful, don't try another model
    if ai_report:

        break


# ============================================================
# 23. IF ALL GEMINI MODELS FAIL
# ============================================================

if not ai_report:

    print("\n======================================")
    print("GEMINI AI ANALYSIS FAILED")
    print("======================================")

    print(
        "\nAll Gemini models are currently unavailable."
    )

    print(
        "Your Python/Pandas/Excel analysis was completed."
    )

    ai_report = """
Gemini AI analysis could not be generated because
the Gemini API models were temporarily unavailable.

The Python sales analysis and Excel report were
successfully generated.
"""


# ============================================================
# 24. DISPLAY AI REPORT
# ============================================================

print("\n======================================")
print("GENAI SALES REPORT")
print("======================================")

print("\n")

print(ai_report)


# ============================================================
# 25. SAVE AI REPORT
# ============================================================

ai_report_file = (
    OUTPUT_DIR /
    "genai_sales_report.txt"
)

with open(
    ai_report_file,
    "w",
    encoding="utf-8"
) as file:

    file.write(ai_report)


print("\n======================================")
print("AI REPORT SAVED")
print("======================================")

print(
    f"\nFile:\n{ai_report_file}"
)


# ============================================================
# 26. FINAL PROJECT OUTPUT
# ============================================================

print("\n======================================")
print("PROJECT COMPLETED SUCCESSFULLY")
print("======================================")

print("\nGenerated files:")

print("✓ cleaned_sales_data.csv")

print("✓ sales_analysis_report.xlsx")

print("✓ monthly_sales.png")

print("✓ regional_sales.png")

print("✓ product_sales.png")

print("✓ correlation_heatmap.png")

print("✓ genai_sales_report.txt")

print(
    f"\nOutput folder:\n{OUTPUT_DIR}"
)