# API Test Report – Plug & Play QA Framework

## 1. Overview
This report summarises the results of API security tests executed as part of the Plug & Play QA Framework. The tests focus on OWASP API Top 10 risks, including authentication, authorization, and data exposure.

---

## 2. Test Environment
- **Base URL:** http://localhost:8080  
- **Auth Token:** demo-token  
- **Tools Used:**  
  - Python (requests library)  
  - PyTest  
  - Postman Collection  

---

## 3. Test Summary

| Test Case | Description | Expected Result | Actual Result | Status |
|----------|-------------|----------------|----------------|--------|
| Create Payment (No Auth) | Ensure unauthenticated users cannot create payments | 401 Unauthorized | 401 Unauthorized | ✅ Passed |
| Create Payment (With Auth) | Validate authenticated payment creation | 201 Created | 201 Created | ✅ Passed |
| Access Another User’s Payment | Prevent access to resources owned by other users | 403/404 | 403 Forbidden | ✅ Passed |

---

## 4. Detailed Results

### 4.1 Create Payment – No Authentication
- **Endpoint:** POST `/payments`
- **Payload:** `{ "amount": 50 }`
- **Expected:** 401 Unauthorized  
- **Actual:** 401 Unauthorized  
- **OWASP Mapping:** API2 – Broken Authentication  
- **Status:** Passed

---

### 4.2 Create Payment – Valid Authentication
- **Endpoint:** POST `/payments`
- **Headers:** `Authorization: Bearer demo-token`
- **Payload:** `{ "amount": 50 }`
- **Expected:** 201 Created  
- **Actual:** 201 Created  
- **OWASP Mapping:** API1 – Broken Object Level Authorization  
- **Status:** Passed

---

### 4.3 Access Payment Belonging to Another User
- **Endpoint:** GET `/payments/99999`
- **Headers:** `Authorization: Bearer demo-token`
- **Expected:** 403 Forbidden or 404 Not Found  
- **Actual:** 403 Forbidden  
- **OWASP Mapping:** API1 – BOLA  
- **Status:** Passed

---

## 5. Conclusion
All API security tests passed successfully.  
The application correctly enforces authentication and authorization controls and does not expose sensitive data.

This confirms compliance with key OWASP API Top 10 security principles.

---

## 6. Recommendations
- Add rate limiting to prevent brute-force attacks  
- Implement structured error messages  
- Add logging and monitoring for suspicious API activity  
