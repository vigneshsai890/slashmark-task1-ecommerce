# Task 1 — E-Commerce Website Automation Testing

Automated test suite for **SauceDemo** e-commerce website using Python + Selenium + pytest.

## What's Tested

- **Login** — Valid/invalid credentials, logout, locked-out users
- **Browse Products** — Product display, sorting (price, name), product details
- **Cart** — Add/remove items, cart count, continue shopping
- **Checkout** — Form validation, order total, tax calculation, order completion

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run Tests

```bash
# All tests
pytest

# By category
pytest -m smoke
pytest -m regression

# Generate HTML report
pytest --html=reports/report.html --self-contained-html
```

## Tech Stack

- Python 3 + Selenium 4 + pytest
- Page Object Model design pattern
- Data-driven testing with parameterized fixtures
- WebDriver Manager for automatic browser driver management

## Intern

**M Vignesh Sai** — Slash Mark Internship (June 2026)
