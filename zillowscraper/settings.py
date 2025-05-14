# Scrapy settings for zillowscraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "zillowscraper"

SPIDER_MODULES = ["zillowscraper.spiders"]
NEWSPIDER_MODULE = "zillowscraper.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "zillowscraper (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}
DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.zillow.com/new-york-ny/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    # 'cookie': 'zguid=24|%248958a821-7bc5-41c1-b8ec-b4eb5ad42bc2; zgsession=1|163266bf-a222-4c31-a87b-02ea3faa1a10; _ga=GA1.2.940009883.1745507419; _gid=GA1.2.369502808.1745507419; zjs_anonymous_id=%228958a821-7bc5-41c1-b8ec-b4eb5ad42bc2%22; zjs_user_id=null; zg_anonymous_id=%22280e1cd0-9db0-47e8-9bd4-87f86e2a0321%22; JSESSIONID=8DEB033E282E2ED0219A93562635EC9E; pxcts=3ddbb788-211e-11f0-b8ca-805264deb802; _pxvid=3ddbaaed-211e-11f0-b8ca-4c8e8f8d463b; _gcl_au=1.1.465745807.1745507424; _rdt_uuid=1745507424670.60554504-f789-42ad-ae20-a56036e40287; _scid=nfLilo-4uyuZl99g4Tc8NKgHrhT0T5dP; _scid_r=nfLilo-4uyuZl99g4Tc8NKgHrhT0T5dP; _fbp=fb.1.1745507425209.970368790185788325; _ScCbts=%5B%5D; _pin_unauth=dWlkPVlqSXdNemhrT1RndE0yWmhOUzAwT1dNeUxXRXhOVFl0WW1JMFpUUmpOMlZpWTJSag; _tt_enable_cookie=1; _ttp=01JSM5K7E31ZQ8JMFNW8P7XWD1_.tt.1; _clck=jtzhag%7C2%7Cfvc%7C0%7C1940; tfpsi=430ca94a-b1ef-458a-8682-a824aafa7609; DoubleClickSession=true; _sctr=1%7C1745442000000; web-platform-data=%7B%22wp-dd-rum-session%22%3A%7B%22doNotTrack%22%3Atrue%7D%7D; AWSALB=FR3A6W5uLM65mXmkWfhvmWRxfelBihVM5RJUkZifuyDCDAowGolSzTuGJRGsgWHnn7z8AkXtqN8g+OMpjubQ0T4vdVwSFQUQcZV2QDr5yB4QS8GtKHOQVqj9tQom; AWSALBCORS=FR3A6W5uLM65mXmkWfhvmWRxfelBihVM5RJUkZifuyDCDAowGolSzTuGJRGsgWHnn7z8AkXtqN8g+OMpjubQ0T4vdVwSFQUQcZV2QDr5yB4QS8GtKHOQVqj9tQom; _uetsid=3f936030211e11f083369fa6538ffd9d; _uetvid=3f938d40211e11f0822081de1a3e132a; _px3=ab3e6dc49037dc8883b459d87dfa66eb29f4deb43e4229086d43b02dd096d946:jlvS5Q6ooc8gaRquAk/ZS4lDDhr3VqIt4meMK461NXlHOlyg6i9g8Po/GYv+3W2RzY5MF+/2JUARVFJOBWvFxQ==:1000:RbPwWnI5Xytq8zCdu3NahGCljuQzuuyeiv4jSzm95TeI64rfis56P8wMuxvIFJVrCUvc57SmCCRa+ByFddFGYr1SvAhG2ENhsHqKPgXG4ssYYLCWrKFFtKU9cQxXI2obdoOhmKoaQUaqfrCe82Xj0E+KjVwTJwTtdtaoLqtH3LVboi3vwznVgo4VoZKKDDhECFWFKs8GQoUssjhGUxgJuLkTo0sETc8sxThNPNh+r6I=; ttcsid=1745507425739::etIH0ZcgCFjC_rRAP-8a.1.1745509227041; search=6|1748101227693%7Crect%3D41.114052531301155%2C-73.60683248925784%2C40.27903398839808%2C-74.35252951074222%26rid%3D6181%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26singlestory%3D0%26housing-connector%3D0%26parking-spots%3Dnull-%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26showcase%3D0%26featuredMultiFamilyBuilding%3D0%26onlyRentalStudentHousingType%3D0%26onlyRentalIncomeRestrictedHousingType%3D0%26onlyRentalMilitaryHousingType%3D0%26onlyRentalDisabledHousingType%3D0%26onlyRentalSeniorHousingType%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%096181%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Afalse%7D%09%09%09%09%09; __gads=ID=42a1fc87c9f55b86:T=1745507456:RT=1745509228:S=ALNI_MZMe4y76qUOimdnPfMrCTPQR9kfrw; __gpi=UID=00001096044dfaf8:T=1745507456:RT=1745509228:S=ALNI_MYpVhH5kFK5RyYYgVFxw2gzSZlkQg; __eoi=ID=ccc7f06213b8425a:T=1745507456:RT=1745509228:S=AA-AfjadQ6JLNs_3ZMZg0sQJYc6D; ttcsid_CN5P33RC77UF9CBTPH9G=1745507425738::R7JNAdEIfS24FSxPkrZb.1.1745509228892',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "zillowscraper.middlewares.ZillowscraperSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "zillowscraper.middlewares.ZillowscraperDownloaderMiddleware": 543,
#}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "zillowscraper.pipelines.ZillowscraperPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
