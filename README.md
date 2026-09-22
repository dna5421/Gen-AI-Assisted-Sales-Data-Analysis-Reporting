<body>

<div class="container">
 
<header class="hero">
    <h1>🎯 Gen-AI-Assisted Sales Data Analysis & Reporting</h1>
    <p>Transforming raw sales transactions into business KPIs,visual insights, and AI-assisted management reporting.</p>
</header>

<section class="section">
    <h2>📝 Project Overview</h2>
    <p>This project analyzes sales transaction data, derives business KPIs,visualizes trends, and uses a generative AI model to produce amanagement-friendly business report.</p>
    <p>It combines traditional data analysis with AI-assisted summarization to convert raw sales data into actionable recommendations.</p>
</section>

<section class="section">
    <h2>✨ Problem Statement</h2>
    <p>Businesses often have raw sales records but struggle to turn them into clear insights about revenue performance, product trends, regional differences, customer retention risk, and operational           opportunities.</p>
    <p>This project addresses that gap by automating data cleaning, KPI calculation, chart generation, and AI-generated executive reporting from sales data.</p>
</section>

<section class="section">
    <h2>📊 Dataset</h2>
    <p>The project uses a sales dataset stored in<strong>sales_data.csv</strong>.</p>
    <p>The dataset includes 20 orders collected across January–August 2025 and contains:</p>
    <ul>
        <li>OrderID</li>
        <li>OrderDate</li>
        <li>CustomerName</li>
        <li>Region</li>
        <li>Category</li>
        <li>Product</li>
        <li>Quantity</li>
        <li>UnitPrice</li>
        <li>Discount</li>
    </ul>
    <h3>Business Dataset Summary</h3>
    <div class="highlight-grid">
        <div class="card"><span class="number">20</span><span class="label">Total Orders</span></div>
        <div class="card"><span class="number">157</span><span class="label">Total Units Sold</span>
        </div>
        <div class="card"><span class="number">20</span><span class="label">Unique Customers</span>
        </div>
        <div class="card"><span class="number">₹13.74L</span><span class="label">Net Revenue</span></div>
    </div>
</section>

<section class="section">
    <h2>⚒️ Tools & Technologies</h2>
    <div class="tech-list">
        <span class="tech">Python</span>
        <span class="tech">Pandas</span>
        <span class="tech">Matplotlib</span>
        <span class="tech">Seaborn</span>
        <span class="tech">OpenPyXL</span>
        <span class="tech">Google GenAI</span>
        <span class="tech">Gemini API</span>
        <span class="tech">Python-dotenv</span>
        <span class="tech">CSV</span>
        <span class="tech">Excel</span>
    </div>
</section>

<section class="section">
    <h2>Ⓜ️ Methods</h2>
        <li>Read the CSV file.</li>
        <li>Check for missing or invalid records.</li>
        <li>Remove duplicate rows.</li>
        <li>Clean date and numerical fields.</li>
    </ul>
    <h3>2. Feature Engineering</h3>
    <ul>
        <li>Compute GrossSales.</li>
        <li>Compute DiscountAmount.</li>
        <li>Compute Revenue.</li>
        <li>Create Month and Year columns.</li>
    </ul>
    <h3>3. Business Analytics</h3>
    <ul>
        <li>Total revenue.</li>
        <li>Average order value.</li>
        <li>Revenue by region.</li>
        <li>Revenue by category.</li>
        <li>Top and low-performing products.</li>
        <li>Customer contribution analysis.</li>
        <li>Discount impact analysis.</li>
    </ul>
    <h3>4. Visualization</h3>
    <ul>
        <li>Monthly sales trend chart.</li>
        <li>Region-wise revenue chart.</li>
        <li>Top product chart.</li>
        <li>Correlation heatmap.</li>
    </ul>
    <h3>5. AI-Assisted Report Generation</h3>
    <ul>
        <li>Convert analysis metrics into a JSON payload.</li>
        <li>Send the data to Gemini using a business-analysis prompt.</li>
        <li>Generate management-friendly insights.</li>
        <li>Generate recommendations based only on supplied data.</li>
    </ul>
</section>

<section class="section">
    <h2>📊 Key Insights</h2>
    <div class="success"><strong>Total Net Revenue:</strong> ₹1,373,850</div>
    <div class="insight"><strong>Average Order Value:</strong>₹68,692.50</div>
    <div class="insight"><strong>Category Performance:</strong>Electronics is the dominant category, contributing 78.89%of total revenue.</div>
    <div class="insight"><strong>Regional Performance:</strong>North is the strongest region, contributing 40.44% of revenue.</div>
    <div class="warning"><strong>East Region:</strong>East has the lowest revenue despite selling a high volume of units,indicating a potential revenue-efficiency opportunity.</div>
    <div class="insight"><strong>Top Products:</strong>Mobile, Laptop, and Monitor are among the leading products.</div>
    <div class="warning"><strong>Customer Retention:</strong>100% of customers are one-time buyers in this dataset,indicating a customer-retention opportunity.</div>
    <div class="warning"><strong>Revenue Trend:</strong>Revenue declined in recent months, indicating a possibledownward demand trend.</div>
    <div class="insight"><strong>Low-Performing Products:</strong>Products such as Printer Paper generate quantity but contribute comparatively low revenue.</div>
</section>

<section class="section">
    <h2>🧑‍💼 AI Model & Output</h2>
    <p>The project uses Google Gemini models for AI-assisted businessreport generation.</p>
    <h3>Gemini Model Fallback Options</h3>
    <ul>
        <li>gemini-3.6-flash</li>
        <li>gemini-3.5-flash</li>
        <li>gemini-3.1-flash-lite</li>
        <li>gemini-2.5-flash</li>
    </ul>
    <h3>Generated Outputs</h3>
    <ul class="output-list">
        <li>📄 cleaned_sales_data.csv</li>
        <li>📊 sales_analysis_report.xlsx</li>
        <li>📈 monthly_sales.png</li>
        <li>📊 regional_sales.png</li>
        <li>📦 product_sales.png</li>
        <li>🔥 correlation_heatmap.png</li>
        <li>🤖 genai_sales_report.txt</li>
    </ul>
</section>

<section class="section">
    <h2>🚀 How to Run This Project</h2>
    <h3>1. Clone the Repository</h3>
    <p>Clone the project repository to your local machine.</p>
    <h3>2. Create a Virtual Environment</h3>
    <p>Creating a virtual environment is optional but recommended.</p>
    <h3>3. Install Dependencies</h3>
    <div class="command">pip install pandas matplotlib seaborn python-dotenv google-genai openpyxl</div>
    <h3>4. Configure Gemini API</h3>
    <p>Create a <strong>.env</strong> file in the project root and add:</p>
    <div class="env">GEMINI_API_KEY=your_api_key_here</div>

   <h3>5. Add Dataset</h3>
    <p>Ensure <strong>sales_data.csv</strong> is available either inthe project root or inside the <strong>data/</strong> directory.</p>
   
   <h3>6. Run the Script</h3>
    <div class="command">python sales_genai_analysis.py</div>

   <h3>The Script Will</h3>
    <ul>
        <li>Clean the sales data.</li>
        <li>Generate business KPIs.</li>
        <li>Generate charts.</li>
        <li>Create Excel analytics.</li>
        <li>Call Gemini for AI-powered insights.</li>
        <li>Save generated outputs inside the output/ directory.</li>
    </ul>
</section>

<section class="section">
    <h2>🎯 Results</h2>
    <p>The project successfully produces:</p>
    <ul>
        <li>Cleaned dataset for analysis.</li>
        <li>Revenue and trend analysis.</li>
        <li>Region, category, and product insights.</li>
        <li>Executive-level recommendations.</li>
        <li>Business-friendly AI summary report.</li>
        <li>Visual dashboard elements for stakeholder review.</li>
    </ul>
</section>

<section class="section">
    <h2>✨ Conclusion</h2>
    <p>This project demonstrates how data analytics and generative AIcan be combined to create an intelligent business reporting
        workflow.</p>
    <p>It transforms raw transaction data into structured insights,visual evidence, and actionable recommendations while reducing
        the amount of manual reporting required.</p>
</section>

<section class="section">
    <h2>🏢 Future Work</h2>
    <ul>
        <li>Add real-world sales data importing from APIs or databases.</li>
        <li>Integrate forecasting models for future revenue prediction.</li>
        <li>Build an interactive dashboard using Streamlit or Dash.</li>
        <li>Add customer segmentation and churn analysis.</li>
        <li>Improve AI prompt design for more nuanced executive reporting.</li>
        <li>Include region-wise and product-wise forecasting.</li>
        <li>Add automated email or PDF report generation.</li>
    </ul>
</section>

<footer class="footer">
    <h2>📡 Author & Contact</h2>
    <p style="margin-top: 15px;">👤 Author: <strong>dna5421</strong></p>
    <p>📧 GitHub Profile:<a href="https://github.com/dna5421"target="_blank">github.com/dna5421</a></p>
    <p>🔗 Repository:<a href="https://github.com/dna5421/Gen-AI-Assisted-Sales-Data-Analysis-Reporting"target="_blank">Gen-AI-Assisted-Sales-Data-Analysis-Reporting</a></p>
</footer>

</div>

</body> </html>
