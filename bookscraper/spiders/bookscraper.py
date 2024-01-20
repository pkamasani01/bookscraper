# Import libraries
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bookscraper.items import BookscraperItem
import os
from csv import writer

class BookScraper(CrawlSpider):
    # name of the project
    name = "bookscraper"
    # URL to scrape 
    start_urls = ["http://books.toscrape.com/"]
    
    # Rules for scraping
    rules = (
        Rule(LinkExtractor(restrict_css=".nav-list > li > ul > li > a"),follow = True),
        Rule(LinkExtractor(restrict_css=".product_pod > h3 > a"),callback = "parse_book")
        )
    # Function to parse the website
    # This function is called untill all books are parsed
    def parse_book(self, response):
        book_item = BookscraperItem()
        book_item["image_url"] = response.urljoin(response.css(".item.active > img::attr(src)").get())
        book_item["title"] = response.css(".col-sm-6.product_main > h1::text").get()
        book_item["upc"] = response.css(".table.table-striped > tr:nth-child(1) > td::text").get()
        book_item["url"] = response.url
        book_item["price"] = response.css(".table.table-striped > tr:nth-child(4) > td::text").get()
        book_item["availability"] = response.css(".table.table-striped > tr:nth-child(6) > td::text").get()
        book_item["reviews"] = response.css(".table.table-striped > tr:nth-child(7) > td::text").get()
        self.Save_to_file(
            book_item["image_url"],
            book_item["title"], 
            book_item["price"],
            book_item["upc"], 
            book_item["url"],
            book_item["availability"],
            book_item["reviews"]
            )
        
        return book_item
    # Save data to data.csv file
    def Save_to_file(self, image_url, title, price, upc, url, availability, reviews):
        self.price = price
        self.image_url = image_url
        self.title = title
        self.upc = upc
        self.url = url
        self.availability = availability
        self.reviews = reviews
        if os.path.isfile("data.csv"):
            with open('data.csv', 'a') as f_object:
                writer_object = writer(f_object)
                # Pass the list as an argument into
                # the writerow()
                writer_object.writerow([self.image_url, self.title, self.price, self.upc, self.url, self.availability, self.reviews])
                # Close the file object
                f_object.close()
        else:
            with open('data.csv', 'w') as f_object:
                writer_object = writer(f_object)
                
                # Pass the list as an argument into
                # the writerow()
                writer_object.writerow(["image_url", "title", "price", "upc", "url", "availability", "reviews"])
                writer_object.writerow([self.image_url, self.title, self.price, self.upc, self.url, self.availability, self.reviews])
                # Close the file object
                f_object.close()
        