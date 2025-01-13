# 🛒 Depop.com Scraping: Extract Product Details Effortlessly 📊

<p align="right">

<a href="https://github.com/JanakDobariya/">
<img src="https://badges.pufler.dev/visits/JanakDobariya/depop.com-scraping?label=VISITOR&style=for-the-badge&logoColor=FFFFFF&color=purple&labelColor=640464&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9IndoaXRlIiB2ZXJzaW9uPSIxLjEiIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2IiBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWV5ZSIgYXJpYS1oaWRkZW49InRydWUiPjxwYXRoIGQ9Ik04IDJjMS45ODEgMCAzLjY3MS45OTIgNC45MzMgMi4wNzggMS4yNyAxLjA5MSAyLjE4NyAyLjM0NSAyLjYzNyAzLjAyM2ExLjYyIDEuNjIgMCAwIDEgMCAxLjc5OGMtLjQ1LjY3OC0xLjM2NyAxLjkzMi0yLjYzNyAzLjAyM0MxMS42NyAxMy4wMDggOS45ODEgMTQgOCAxNGMtMS45ODEgMC0zLjY3MS0uOTkyLTQuOTMzLTIuMDc4QzEuNzk3IDEwLjgzLjg4IDkuNTc2LjQzIDguODk4YTEuNjIgMS42MiAwIDAgMSAwLTEuNzk4Yy40NS0uNjc3IDEuMzY3LTEuOTMxIDIuNjM3LTMuMDIyQzQuMzMgMi45OTIgNi4wMTkgMiA4IDJaTTEuNjc5IDcuOTMyYS4xMi4xMiAwIDAgMCAwIC4xMzZjLjQxMS42MjIgMS4yNDEgMS43NSAyLjM2NiAyLjcxN0M1LjE3NiAxMS43NTggNi41MjcgMTIuNSA4IDEyLjVjMS40NzMgMCAyLjgyNS0uNzQyIDMuOTU1LTEuNzE1IDEuMTI0LS45NjcgMS45NTQtMi4wOTYgMi4zNjYtMi43MTdhLjEyLjEyIDAgMCAwIDAtLjEzNmMtLjQxMi0uNjIxLTEuMjQyLTEuNzUtMi4zNjYtMi43MTdDMTAuODI0IDQuMjQyIDkuNDczIDMuNSA4IDMuNWMtMS40NzMgMC0yLjgyNS43NDItMy45NTUgMS43MTUtMS4xMjQuOTY3LTEuOTU0IDIuMDk2LTIuMzY2IDIuNzE3Wk04IDEwYTIgMiAwIDEgMS0uMDAxLTMuOTk5QTIgMiAwIDAgMSA4IDEwWiI+PC9wYXRoPjwvc3ZnPg==">
</a> 

</p>

## Overview
This project demonstrates web scraping of product data from [Depop.com](https://www.depop.com). By leveraging Python and libraries like requests and BeautifulSoup, the script extracts product details such as name, price, size, and images, and stores them in a structured CSV format for further analysis.

## Key Features
- *🔗 URL Collection*: Collect product page links dynamically from category listings.
- *🛍 Product Details Extraction*: Scrape product name, price, size, and associated images.
- *📄 Data Storage*: Save the extracted data into a CSV file for easy access and analysis.
- *📊 Pandas Integration*: Utilize pandas for efficient data handling and storage.

## Tech Stack
- *🐍 Python*: Core language for the scraping script.
- *📦 Libraries Used*:
  - requests: For making HTTP requests to fetch page content.
  - BeautifulSoup (bs4): For parsing and extracting information from HTML pages.
  - pandas: For organizing and exporting data to a CSV file.

## Installation
1. *Clone the repository*:
   bash
   git clone https://github.com/JanakDobariya/depop.com-scraping.git
   cd depop.com-scraping
   

2. *Install dependencies*:
   Ensure you have Python installed, then run:
   bash
   pip install -r requirements.txt
   

3. *Run the script*:
   bash
   python depop.py
   

## Usage
- The script scrapes product data from the men's category on Depop.com.
- Outputs a CSV file (depop.csv) containing the following columns:
  - *Product Name*
  - *Product Price*
  - *Product Size*
  - *Product Photo* (URLs of images)

## Example Output
![image](https://github.com/user-attachments/assets/a5fe2fa3-3b12-4189-9d08-0b390656380b)


## Important Notes
- Ensure stable internet connectivity for scraping.
- The script may require updates if Depop.com changes its website structure.

## Contributions
Contributions are welcome! You can fix this repository, make changes, and open a pull request.

## Disclaimer
This project is for educational purposes only. Please make sure that Depop.com's terms of service while using this script.

---
Happy Scraping! 🚀
