📘 Using the API Collection
The API_Collection.json file provides a ready‑to‑use Postman collection for testing API security scenarios aligned with OWASP Top 10 principles.

🔹 Importing the Collection into Postman
Open Postman

Click Import

Select:

Code
API/API_Collection.json
The collection loads with:

Create Payment – No Auth

Create Payment – With Auth

Get Payment by ID (Authorization Test)

🔹 Setting Up Environment Variables
Variable	Description	Default
base_url	API host under test	http://localhost:8080
auth_token	Token for authenticated requests	demo-token
Steps:

Go to Environments → Add

Create: Plug & Play QA Environment

Add variables

Select the environment from the top-right dropdown

🔹 Running the Requests
Create Payment – No Auth → Expected: 401 Unauthorized

Create Payment – With Auth → Expected: 201 Created

Get Payment by ID → Expected: 403 Forbidden or 404 Not Found

🔹 How It Fits Into the Framework
The Postman collection complements:

Automated API tests

CI/CD pipeline

API Test Report

Together they provide:

Manual validation

Automated validation

Continuous validation

📄 Documentation
Test Plan

Service Brochure

Accessibility Strategy

⚙️ CI/CD Pipeline
The GitHub Actions workflow automatically runs:

API security tests

Accessibility checks

UI smoke tests

on every push or pull request.

Workflow file:

Code
.github/workflows/qa_pipeline.yml
🤝 Contributing
Pull requests are welcome.
For major changes, open an issue first to discuss improvements.

📬 Contact
Hyginus Obi  
Cybersecurity & QA Automation Professional
obichuks4lyf@gmail.com
hyginusc.obi@gmail.com
+447766128957