# ScreenshotMAX Python SDK

[![test](https://github.com/screenshotmax/python-sdk/actions/workflows/test.yml/badge.svg)](https://github.com/screenshotmax/python-sdk/actions/workflows/test.yml)

This is the official Python SDK for the [ScreenshotMAX API](https://screenshotmax.com/).

It allows you to easily capture high-quality screenshots of any URL directly from your applications.
The SDK handles authentication, request signing, and provides a simple interface to integrate ScreenshotMAX’s powerful screenshot services into your Python projects.

Get started in minutes. Just [sign up](https://screenshotmax.com) to receive your access and secret keys, import the client, and you’re ready to capture screenshots.”

The SDK client is synchronized with the latest [ScreenshotMAX API options](https://docs.screenshotmax.com/guides/start/introduction).

## Usage

Use the SDK to generate signed or unsigned URLs for screenshots, PDFs, web scraping, or animated screenshot—without executing the request. Or fetch and download the result directly. You have full control over when and how each capture runs.

### Screenshot example
```python
from screenshotmax import SDK
from screenshotmax.options import ScreenshotOptions

sdk = SDK("<ACCESS_KEY>", "<SECRET_KEY>")

# set up options
opts = ScreenshotOptions(url="https://example.com")
sdk.screenshot.set_options(opts)

#// generate URL (https://api.screenshotmax.com/v1/screenshot?url=https%3A%2F%2Fexample.com&image_width=1280&image_height=720&format=png&image_quality=80&access_key=<ACCESS_KEY>&signature=370f5b161bc59eed13b76........1f778635d7fc595dbab12)
url = sdk.screenshot.get_url()

# generate screenshot
result, headers = sdk.screenshot.fetch()
```

### Web scraping example
```python
from screenshotmax import SDK
from screenshotmax.options import ScrapeOptions

sdk = SDK("<ACCESS_KEY>", "<SECRET_KEY>")

# set up options and scrape content (chaining)
opts = ScrapeOptions(url="https://example.com")
sdk.scrape.set_options(opts)

result, headers = sdk.scrape.fetch()
```

### PDF generation example
```python
from screenshotmax import SDK
from screenshotmax.enums import PDFPaperFormat
from screenshotmax.options import PDFOptions

sdk = SDK("<ACCESS_KEY>", "<SECRET_KEY>")

# set up options and scrape content (chaining)
opts = PDFOptions(url="https://example.com", pdf_paper_format=PDFPaperFormat.LETTER)
result, headers = sdk.pdf.set_options(opts).fetch()
```

### Scheduled task example
```python
from screenshotmax import SDK
from screenshotmax.options import PDFOptions

sdk = SDK("<ACCESS_KEY>", "<SECRET_KEY>")

# get all tasks from account
tasks = sdk.task.get_tasks()
# {"tasks":[{
# "id":5678133109850112,
# "name":"Test CRON",
# "api":"screenshot",
# "query":
# "url=https%3A%2F%2Fexample.com",
# "frequency":"every_day",
# "crontab":"25 13 * * *",
# "timezone":"Etc/UTC",
# "enabled":true,
# "created":1747229104,
# "last_run":1748611516,
# "runs":18}]}
```

## License

`screenshotmax` is released under [the MIT license](LICENSE).
