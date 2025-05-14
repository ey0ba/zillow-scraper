
  
import scrapy
import json
import os

class ZillowSpider(scrapy.Spider):
    name = "zillowspider"
    allowed_domains = ["zillow.com"]

    all_zipcodes = ["K1A-0B1", "V6B-0N5"]
    progress_file = "progress.json"
    done_file = "done_zipcodes.txt"

    def start_requests(self):
        self.progress = self.load_progress()
        self.done_zips = self.load_done_zipcodes()

        for zip_code in self.all_zipcodes:
            if zip_code in self.done_zips:
                self.logger.info(f"Skipping {zip_code}, already done.")
                continue

            last_page = self.progress.get(zip_code, 0)
            url = f"https://www.zillow.com/homes/{zip_code}_rb/"
            meta = {"zip_code": zip_code, "page": last_page + 1}
            yield scrapy.Request(
                url=url,
                headers=self.custom_headers(),
                callback=self.parse,
                meta=meta
            )

    def parse(self, response):
        zip_code = response.meta["zip_code"]
        page = response.meta["page"]

        raw_data = response.xpath("//script[@id='__NEXT_DATA__']/text()").get()
        if not raw_data:
            self.logger.warning(f"No JSON data for {zip_code} page {page}")
            return

        json_data = json.loads(raw_data)
        try:
            listings = json_data['props']['pageProps']['searchPageState']['cat1']['searchResults']['listResults']
        except KeyError:
            self.logger.warning(f"No listings found for {zip_code} page {page}")
            return

        for home in listings:
            yield {
                "zip_code": zip_code,
                "page": page,
                "home_url": home.get('detailUrl'),
                "price": home.get('price'),
                "address": home.get('address'),
                "status": home.get('statusType'),
            }

        # Save current page progress
        self.progress[zip_code] = page
        self.save_progress()

        # Get next page
        next_url = json_data['props']['pageProps']['searchPageState']['cat1']['searchList']['pagination'].get('nextUrl')
        if next_url:
            next_page_url = f"https://www.zillow.com{next_url}"
            yield scrapy.Request(
                url=next_page_url,
                headers=self.custom_headers(),
                callback=self.parse,
                meta={"zip_code": zip_code, "page": page + 1}
            )
        else:
            # No more pages – mark ZIP as done
            self.mark_zip_done(zip_code)

    def custom_headers(self):
        return {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        }

    def load_progress(self):
        if os.path.exists(self.progress_file):
            with open(self.progress_file, "r") as f:
                return json.load(f)
        return {}

    def save_progress(self):
        with open(self.progress_file, "w") as f:
            json.dump(self.progress, f, indent=2)

    def load_done_zipcodes(self):
        if os.path.exists(self.done_file):
            with open(self.done_file, "r") as f:
                return set(line.strip() for line in f)
        return set()

    def mark_zip_done(self, zip_code):
        with open(self.done_file, "a") as f:
            f.write(zip_code + "\n")
        self.logger.info(f"Marked {zip_code} as fully scraped.")
