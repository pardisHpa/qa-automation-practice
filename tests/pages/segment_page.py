class SegmentPage:
    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url

    def open(self):
        self.page.goto(f"{self.base_url}/index.html")

    def check(self, recency, frequency):
        self.page.fill("#recency", str(recency))
        self.page.fill("#frequency", str(frequency))
        self.page.click("#check")

    def result_text(self):
        return self.page.inner_text("#result")

    def error_text(self):
        return self.page.inner_text("#error")
