<div align="center">

<img src="docs/architecture.svg" alt="Slashmark Task 1 · E-Commerce Testing architecture map" width="100%" />

</div>

# Slashmark Task 1 · E-Commerce Testing

> End-to-end browser coverage for login, catalog, sorting and cart behavior.

A Python + Selenium + pytest suite for SauceDemo flows, with page objects separating user intent from browser mechanics.

<div align="center">

`Python · Selenium · pytest` &nbsp;·&nbsp; `login → catalog → product detail → cart / logout`

</div>

## `01 / SYSTEM CARD`

- **Primary boundary:** `pytest scenario → page objects → SauceDemo`
- **Documentation stance:** architecture and presentation only; application source is intentionally untouched.
- **Visual language:** Y2K terminal grid, brutalist labels, maximalist contrast, readable static SVG fallback.

## `02 / ARCHITECTURE`

The map above is a compact view of the repository's visible runtime boundary. It is designed to answer three questions quickly: where input enters, where policy or domain logic lives, and where external side effects leave the system.

![Architecture map for Slashmark Task 1 · E-Commerce Testing](docs/architecture.svg)

## `03 / DESIGN NOTES`

- The README-defined flows are represented as a user journey rather than a list of test files.
- Only documentation and a new architecture asset are part of this upgrade.

This upgrade adds documentation assets only. It does not change source files, dependency manifests, tests, workflows or runtime configuration.

## `04 / EXISTING PROJECT DOCUMENTATION`

<details open>
<summary>Read the original project notes</summary>

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

</details>

