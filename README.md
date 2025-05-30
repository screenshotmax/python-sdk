# ScreenshotMAX Python SDK

[![build](https://github.com/screenshotmax/python-sdk/actions/workflows/build.yml/badge.svg)](https://github.com/screenshotmax/python-sdk/actions/workflows/build.yml)
[![test](https://github.com/screenshotmax/python-sdk/actions/workflows/test.yml/badge.svg)](https://github.com/screenshotmax/python-sdk/actions/workflows/test.yml)

This is the official Python SDK for the [ScreenshotMAX API](https://screenshotmax.com/).

It allows you to easily capture high-quality screenshots of any URL directly from your applications.
The SDK handles authentication, request signing, and provides a simple interface to integrate ScreenshotMAX’s powerful screenshot services into your Python projects.

Get started in minutes. Just [sign up](https://screenshotmax.com) to receive your access and secret keys, import the client, and you’re ready to capture screenshots.”

The SDK client is synchronized with the latest [ScreenshotMAX API options](https://docs.screenshotmax.com/guides/start/introduction).


```python
from python_sdk import SDK
from python_sdk.options import ScreenshotOptions

sdk = SDK("<ACCESS_KEY>", "<SECRET_KEY>")

opts = ScreenshotOptions(url="https://example.com")
sdk.screenshot.set_options(opts)
url = sdk.screenshot.get_url()
result, headers = sdk.screenshot.fetch()
```
