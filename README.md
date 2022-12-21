<h1>Scraper for Yellowpages</h1>
<h2>Overview</h2>
<p>This scraper is built using Scrapy and is used to scrape data about restaurants in Montreal from Yellowpages.ca. The data includes the name, street address, locality, region, postal code, telephone number, website, and ratings of the restaurants. The scraper follows the links to all the restaurants listed on the first page and then visits each restaurant's page to extract the data. It then moves on to the next page and repeats the process until all the pages have been scraped. The data is stored in a CSV file using the pipeline defined in the project.</p>
<h2>Dependencies</h2>
<ul>
  <li>Scrapy</li>
  <li>SQLite</li>
</ul>
<h2>Usage</h2>
<ol>
  <li>Clone the repository: <code>git clone https://github.com/[USERNAME]/yellowpages</code></li>
  <li>Navigate to the project directory: <code>cd yellowpages</code></li>
  <li>Install the dependencies: <code>pip install -r requirements.txt</code></li>
  <li>Run the scraper: <code>scrapy crawl yellow</code></li>
</ol>
<h2>Files</h2>
<ul>
  <li><code>yellowpages/spiders/yellow_spider.py</code>: Contains the Spider class that defines how the data is scraped and processed.</li>
  <li><code>yellowpages/items.py</code>: Defines the structure of the data that is scraped and stored in the CSV file.</li>
  <li><code>yellowpages/pipelines.py</code>: Defines the pipeline that stores the scraped data in the CSV file.</li>
</ul>

<h2> Future Improvement </h2>
<p> Use SQLite database to store the scraped data rather than csv file.
