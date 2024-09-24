# Test Report: Due Diligence Automation System

---

**Project Name**: Due Diligence Automation System  
**Test Date**:2024-09-24
**Test Lead**:   
**Project Version**: V1.0  
**Backend Tech Stack**: FastAPI  
**Database**: MySQL  
**Web Scraping Targets**: Common Australian business query websites (e.g., ASIC, ABN Lookup) and Google  
**Test Tools**: Pytest, Postman, Selenium  
**Scope**: The test plan covers most user stories and system requirements, and code is tested regularly and thoroughly.

---

## 1. Project Overview

The Due Diligence Automation System aims to help users quickly and accurately retrieve risk information about target companies, reduce manual operations, and optimize the corporate query process. The system automatically crawls and analyzes Australian business information and generates detailed due diligence reports. Key features include querying, data scraping, risk assessment, report generation, cache management, and notification mechanisms.

---

## 2. User Stories

### **User Story 1: As a user, I want to query detailed information about a company via a front-end page**
- **Description**: Users can enter the target company's name into the front-end application, and the system will scrape relevant information from multiple Australian business databases (e.g., ASIC, ABN Lookup, Google) and display it on the front-end.
- **Acceptance Criteria**:
  - Users can input the target company's name and submit the query.
  - The system successfully retrieves relevant company information and displays it on the front-end.

### **User Story 2: As a due diligence analyst, I want the system to generate a risk assessment report**
- **Description**: After retrieving company information, the system analyzes financial status, legal issues, negative news, etc., and generates a report that includes risk levels and detailed analysis.
- **Acceptance Criteria**:
  - The system can analyze various aspects of the company.
  - Users can download or view a complete risk assessment report.

### **User Story 3: As an administrator, I want to receive alerts for high-risk companies**
- **Description**: When generating reports, the system will send notifications to designated users if it detects high-risk companies.
- **Acceptance Criteria**:
  - If the system identifies high-risk information about a company, the notification system triggers and sends alerts via email or SMS to the administrator.

### **User Story 4: As a user, I want to quickly retrieve previously queried company information**
- **Description**: Users can quickly retrieve previously queried company information through the system's cache mechanism, avoiding repeated crawling.
- **Acceptance Criteria**:
  - If the cache already contains the company's information, the system should retrieve data from the cache.
  - The query time should be significantly reduced.

### **User Story 5: As a developer, I want the system to function stably under various loads**
- **Description**: The system should remain stable and performant under high concurrent requests or large amounts of data.
- **Acceptance Criteria**:
  - During load testing, the system should remain stable, with no significant delays in response times under a reasonable level of concurrent requests.
  - When large amounts of company data are stored in the database, query and retrieval performance should remain consistent.

---

## 3. Test Scope

- **Functional Testing**:
  - User login and authentication
  - Company information query (for Australian business query sites and Google)
  - Data scraping and processing
  - Risk report generation
  - Cache mechanism
  - Data storage and retrieval
  - Notification sending (optional)
  - Error handling and edge case testing

- **Performance Testing**:
  - System load testing
  - Data scraping speed and frequency
  - Database query efficiency
  - System response time

- **Security Testing**:
  - SQL Injection protection
  - CSRF (Cross-Site Request Forgery) testing
  - User privacy data protection and encryption
  - User permissions and authentication

---

## 4. Test Cases

| **ID** | **Test Name**               | **Test Description**                                         | **Expected Outcome**                                         | **Actual Outcome** | **Status** |
| ------ | --------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------ | ---------- |
| TC001  | User Login & Authentication | Test login with correct and incorrect credentials            | Successful login with correct credentials, failure with wrong | Pass               | Pass       |
| TC002  | ASIC Query Test             | Test company data retrieval from ASIC                        | Successfully retrieve and display correct company data       | Pass               | Pass       |
| TC003  | ABN Lookup Query Test       | Test company data retrieval from ABN Lookup                  | Successfully retrieve and display correct company data       | Pass               | Pass       |
| TC004  | Google Query Test           | Test Google search for related company information & news    | Successfully retrieve company info and relevant news         | Pass               | Pass       |
| TC005  | Risk Report Generation Test | Test the system's ability to generate a complete risk report | Report is generated and displayed correctly on the front end | Pass               | Pass       |
| TC006  | Cache Mechanism Test        | Test if identical queries retrieve data from cache           | Data is successfully retrieved from the cache, avoiding re-fetch | Pass               | Pass       |
| TC007  | Database Read/Write Test    | Test if data is correctly stored and retrieved from MySQL    | Data is successfully stored in and retrieved from the database | Pass               | Pass       |
| TC008  | Notification Mechanism Test | Test if notifications are sent after a report is generated   | Notifications are successfully sent to the user              | Pass               | Pass       |
| TC009  | System Load Test            | Test system stability and response under high concurrent requests | System remains stable with no significant performance drops  | Pass               | Pass       |
| TC010  | SQL Injection Test          | Test if the system prevents SQL Injection attacks            | System is not vulnerable to SQL Injection                    | Pass               | Pass       |
| TC011  | CSRF Protection Test        | Test if the system prevents Cross-Site Request Forgery       | System successfully blocks unauthorized CSRF attempts        | Pass               | Pass       |
| TC012  | Data Encryption & Privacy   | Test if user-sensitive data is encrypted and protected       | Sensitive data is encrypted and not accessible as plain text | Pass               | Pass       |
| TC013  | User Permissions Test       | Test if users can only access data and actions within their scope | Users can only access their authorized data and actions      | Pass               | Pass       |

---

## 5. Test Execution

- **Test Tools**:
  - **Postman**: Used to test API functionality and performance.
  - **Pytest**: Used for unit testing, covering various backend functional modules.
  - **Selenium**: Used for web scraping testing, simulating user actions and checking data accuracy and website interaction.
  - **JMeter**: Used for performance testing, simulating high concurrent requests to evaluate system stability.

- **Test Cycle**: Unit testing is conducted after each functional module is developed. Integration, functional, performance, and security testing are carried out after integration.  
- **Test Frequency**: Automated testing is triggered after each code commit, and full regression testing is performed daily.

---

## 6. Test Results Summary

- **Passed Test Cases**: [Number of passed test cases]  
- **Failed Test Cases**: [Number of failed test cases]  
- **Test Conclusion**:
  - All major functional test cases (e.g., company information queries, data processing, report generation) passed.
  - Performance testing shows that the system remains stable under high concurrent requests.
  - Security testing confirms that the system successfully defends against SQL injection and CSRF attacks.
  - Some test cases need further optimization (e.g., the scraping speed for specific data sources can be improved).

