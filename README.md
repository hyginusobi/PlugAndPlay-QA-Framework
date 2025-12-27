# Plug & Play QA Framework
### Secure • Accessible • Automated

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![PyTest](https://img.shields.io/badge/Testing-PyTest-green)
![OWASP](https://img.shields.io/badge/Security-OWASP%20Top%2010-red)
![WCAG](https://img.shields.io/badge/Accessibility-WCAG%202.1-purple)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-yellow)

---

## Overview  
The **Plug & Play QA Framework** is a lightweight, ready‑to‑use testing solution that integrates:

- 🔐 **OWASP API Security Testing**  
- ♿ **WCAG 2.1 Accessibility Validation**  
- ⚙️ **CI/CD Automation with GitHub Actions**

This framework is designed for **NHS Trusts, SMEs, and public sector organisations** that need secure, accessible, and continuously validated applications — without unnecessary complexity.

---

## Features  
- **OWASP API Security Tests** (auth, BOLA, data exposure)  
- **WCAG Accessibility Checks** (labels, keyboard navigation)  
- **UI Smoke Tests** (login flow, dashboard)  
- **CI/CD Pipeline** (runs tests on every commit)  
- **Clear Documentation** (test plan, service brochure, strategy docs)

---

## 📂 Project Structure

```text
PlugAndPlay-QA-Framework/
├── README.md
├── Documentation/
│   ├── Test_Plan.md
│   ├── Service_Brochure.md
│   └── Accessibility_Strategy.md
├── TestCases/
│   ├── API_TestCases.xlsx
│   └── Accessibility_TestCases.xlsx
├── API/
│   ├── API_Collection.json
│   └── API_Test_Report.md
├── automation/
│   ├── requirements.txt
│   ├── PageObjects/
│   │   ├── LoginPage.py
│   │   └── DashboardPage.py
│   └── tests/
│       ├── test_api_security.py
│       ├── test_accessibility.py
│       └── test_login.py
└── .github/
    └── workflows/
        └── qa_pipeline.yml
```



---

## 🛠 Installation  

Install dependencies:

```bash
pip install -r automation/requirements.txt
