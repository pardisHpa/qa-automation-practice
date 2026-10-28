# QA Automation Practice

A practice project for test automation with Python. It tests a small web page
(Customer Segment Checker) and the rules behind it. The segments come from my
RFM customer segmentation work: customers are grouped by how recently and how
often they bought.

## What is in here

- Unit tests with pytest, including boundary values (`tests/test_rfm_unit.py`)
- Browser tests with Playwright (`tests/test_e2e.py`)
- Page Object pattern (`tests/pages/segment_page.py`)
- Fixtures: a local web server starts for the tests (`tests/conftest.py`)
- One list of test cases shared by unit and browser tests (`src/rfm.py`)
- GitHub Actions workflow that runs the tests on every push

## Segment rules

| Segment | Condition |
|---|---|
| Champion | last purchase within 30 days and at least 5 purchases |
| Loyal | within 60 days and at least 3 purchases |
| At risk | within 180 days |
| Lost | everything else |

## Run the tests

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
pytest -v
```

## Next steps

- Compare Playwright with Selenium
- Add screenshots to failed browser tests
- Learn JUnit and C# for the same kind of tests
