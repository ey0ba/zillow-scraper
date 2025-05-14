# zillow-scraper

# 🏡 Advanced Zillow Scraper (ZIP Code-Based, Resumable, Scrapy-Only)

This is an advanced Zillow scraper built using **Scrapy only** — no Selenium, no Playwright, no headless browser.

Instead of parsing rendered HTML, it reads structured listing data directly from Zillow's embedded `__NEXT_DATA__` JSON, making it **faster, lighter, and easier to scale**.

---

## ⚙️ Features

- ✅ ZIP Code–based scraping
- ✅ Resumable by ZIP and page using `progress.json` and `done_zipcodes.txt`
- ✅ Extracts:
  - Listing URL, price, address, beds, baths, status
- ✅ Automatically follows pagination using `nextUrl`
- ✅ Custom headers to reduce bot detection
- ✅ Ideal for scraping **50K+ listings across Canada or the US**

---

## 📁 Project Structure

```text
zillowspider.py         # Main spider logic
progress.json           # Tracks last page scraped per ZIP
done_zipcodes.txt       # Tracks completed ZIPs



🔁 Recovery System

This scraper can resume where it left off, even after crashes:

    progress.json: stores current page per ZIP

    done_zipcodes.txt: stores finished ZIPs

    On restart, it automatically skips ZIPs and resumes others from the last page

🛠️ How to Run

scrapy crawl zillowspider

(Or use scrapy crawl zillowspider -o results.json if not using FEEDS)
📦 Sample Output

{
  "zip_code": "K1A-0B1",
  "page": 2,
  "home_url": "https://www.zillow.com/homedetails/...",
  "price": "$849,000",
  "address": "123 Main St, Ottawa, ON",
  "status": "FOR_SALE"
}

🧠 What I Learned

    How to reverse-engineer dynamic JavaScript websites using backend logic

    Why structured data is often easier to extract than raw HTML

    How to design robust scraping workflows with pause/resume and logging

📌 Future Plans

    Add ScraperAPI or proxy rotation support

    Store progress in SQLite or Redis

    Build a Streamlit dashboard to visualize the scraped data



---

## ✅ Next Steps

Let me know if you'd like:
- A custom project thumbnail or banner image for GitHub/LinkedIn
- Help setting up `FEEDS` to avoid `-o results.json`
- A Markdown badge setup (e.g., ![Scrapy](https://img.shields.io/badge/Scrapy-Framework-blue))




"This code is a demonstration project. Real-world deployments should include error handling, cloud scheduling, and optional proxy support, which I can provide based on your needs."
