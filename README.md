# BookScraper Project

## Overview
BookScraper is a web scraping application designed to harvest data from the e-commerce bookstore **http://books.toscrape.com/**. It extracts important information regarding the selection of books available on the website, compiling details such as the names of books, costs, URLs, image URLs, number of reviews, availability status, and unique product codes.

## Project Aim
The aim of this project is to provide users with a comprehensive dataset of books from the targeted e-commerce website. It facilitates data analysis, price monitoring, and inventory management for interested parties such as data analysts, market researchers, and book enthusiasts.

## Main Features
- Scrape book data efficiently and accurately.
- Save all book details into a structured CSV file for easy access and manipulation.
- User-friendly and easily automatable for recurring scraping tasks.

## Prerequisites
Before running BookScraper, ensure you have the following:
- Python 3.6 or higher
- Pip (Python package installer)
- Necessary Python libraries: Scrapy

To install Scrapy:

bash
pip install scrapy


## Installation
1. Clone this repository or download the source code.
2. Navigate to the repository's root directory in your terminal or command prompt.

To clone the repository:
bash
git clone https://github.com/pkamasani01/bookscraper.git
cd bookscraper


## Usage
From the root directory of the project, you can execute the following command to start the scraping process:

scrapy crawl bookscraper


This command is telling Scrapy to run the spider defined in the bookscraper.py file and output the scraped data into a file called data.csv in the root directory.

## Output File
- *data.csv:* The output file containing the scraped book data. This comma-separated values file consists of the following columns per book entry:
  - Name
  - Cost
  - URL
  - Image URL
  - Number of Reviews
  - Availability
  - Unique Product Code
