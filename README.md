# Sneaker Price Scraper 🥿📊  

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)  
[![Selenium](https://img.shields.io/badge/Library-Selenium-brightgreen)](https://www.selenium.dev/)  
[![BeautifulSoup](https://img.shields.io/badge/Library-BeautifulSoup-yellow)](https://www.crummy.com/software/BeautifulSoup/)  
[![Pandas](https://img.shields.io/badge/Library-Pandas-lightgrey)](https://pandas.pydata.org/)  
[![Data Analysis](https://img.shields.io/badge/Tool-Power%20BI-orange)](https://powerbi.microsoft.com/)  

A **Python + Selenium + BeautifulSoup** project to scrape **sold listings from eBay** for sneakers, extract details, and save them as clean CSV datasets for analysis in **Power BI** or any other tool.  

Currently includes datasets for:  
- **Air Jordan 1 High** (10 pages scraped)  
- **Adidas Yeezy 350** (10 pages scraped)  

---

## 📌 Features  
- **Search any sneaker**: Specify the sneaker model in the script.  
- **Multiple pages**: Choose how many eBay pages to scrape.  
- **Extracted details**:  
  - Product title  
  - Size  
  - Sold price  
  - Sold date  
  - Condition (New/Used)  
  - Product link  
- **Data cleaning**:  
  - Removes duplicates  
  - Filters out unknown sizes  
  - Converts size to numeric for better sorting  
- **Automatic CSV saving** in `/saved` folder.  

---

## 📂 Project Structure  
.
├── data/ # Raw HTML files for each scraped item
├── saved/ # Final CSV files
├── Sneaker_scrapper.py # Main scraper script
└── README.md # Project documentation

Also, make sure you have Google Chrome installed and ChromeDriver set up in your PATH.

2️⃣ Run the Script

python Sneaker_scrapper.py #bash

💡 Data Analysis Ideas
Price trends over time for each sneaker model

Average resale price by size

Compare resale prices between models (e.g., Air Jordan 1 High vs. Adidas Yeezy 350)

Condition-based price difference (New vs. Used)

📜 License
This project is open-source and free to use for educational and personal purposes.
