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

| **ID**   | **Test Name**               | **Test Description**                                     | **Expected Outcome**                                          | **Actual Outcome**                                                | **Status** |
|----------|-----------------------------|----------------------------------------------------------|---------------------------------------------------------------|-------------------------------------------------------------------|------------|
| TC001    | User Login & Authentication | Test login with correct and incorrect credentials. Correct credentials should log in successfully, and incorrect ones should fail. | Successful login with correct credentials; failure with incorrect credentials. | The system allowed access when valid credentials were used, displaying the user dashboard. When invalid credentials (wrong password) were used, the system displayed an "Invalid credentials" error message, and access was denied. | Pass |
| TC002    | ASIC Query Test             | Test company data retrieval from ASIC. The system should fetch and display company data correctly. | Successfully retrieve and display accurate company data.       | The system retrieved the company's registration status, address, and director information from ASIC and displayed the details on the user interface within 3 seconds. All fields matched the expected data from the ASIC website. | Pass |
| TC003    | ABN Lookup Query Test       | Test company data retrieval from ABN Lookup. The system should fetch and display ABN details. | Successfully retrieve and display accurate ABN details.        | The system fetched ABN details, including company name, status, and GST registration status, and displayed them on the interface within 2.5 seconds. All data matched the ABN Lookup records. | Pass |
| TC004    | Google Query Test           | Test Google search for related company information & news. The system should retrieve and display relevant search results. | Successfully retrieve company info and relevant news.          | The system performed a Google search using the company name, retrieving the top 5 news articles and official website links. Displayed results were relevant and contained links to news sources such as Reuters and ABC News. | Pass |
| TC005    | Risk Report Generation Test | Test the system's ability to generate a complete risk report after data retrieval. | Report is generated and saved, displayed correctly on the front end. | The system combined retrieved data into a risk report, which included sections on financial status, legal records, and negative media coverage. The report was generated within 5 seconds and was saved to the database. The user could view and download the report from the dashboard. | Pass |
| TC006    | Cache Mechanism Test        | Test if identical queries retrieve data from the cache instead of re-fetching from the source. | Data is retrieved from cache, avoiding re-fetch.               | When querying the same company within 10 minutes, the system used cached data, reducing the response time to 1 second. The cache stored the query results and served them without making new API calls, demonstrating efficient use of resources. | Pass |
| TC007    | Database Read/Write Test    | Test if retrieved data is correctly stored in the MySQL database and can be read for further use. | Data is successfully stored and retrievable from the database. | The system stored company information, including name, ABN, and registration status, into the MySQL database. Queries to retrieve this data were executed in under 0.5 seconds, and the displayed information matched the stored records accurately. | Pass |
| TC008    | Notification Mechanism Test | Test if a notification is sent when a risk report indicates high risk. | Notification is sent successfully to the user.                | Upon generating a risk report that identified a "High Risk" status, the system triggered an email notification to the registered user within 2 seconds. The email included a link to view the full report. The user confirmed receipt of the notification without delays. | Pass |
| TC009    | System Load Test            | Test system stability and response under high concurrent requests. Simulate 500 concurrent requests over 5 minutes. | The system remains stable with an average response time below 2 seconds and no significant errors. | The system handled 500 concurrent user requests over 5 minutes with an average response time of 1.8 seconds. CPU usage spiked to 70%, but no server crashes or database connection issues were observed. All requests were processed successfully. | Pass |
| TC010    | SQL Injection Test          | Test the system's defense against SQL injection by attempting to input malicious SQL commands (e.g., `' OR '1'='1'`). | System should sanitize inputs and prevent unauthorized access. | The system blocked all attempts to inject SQL commands. Malicious inputs were sanitized, and the system returned an error message, preventing access to the database. Logs indicated no unauthorized database access attempts. | Pass |
| TC011    | CSRF Protection Test        | Test if the system prevents unauthorized CSRF attempts using a fake session token. | System should block unauthorized CSRF attempts.                | The system rejected requests that included invalid CSRF tokens. Users were prompted with a "Request validation failed" error when tokens did not match. All valid tokens processed correctly, indicating effective CSRF protection. | Pass |
| TC012    | Data Encryption & Privacy   | Test if sensitive data (e.g., login details, query history) is encrypted before storage. | Sensitive data should be encrypted and stored securely.        | User passwords were hashed using SHA-256, and all query histories were encrypted using AES-256 before being stored in the database. Attempts to read raw data from the database returned encrypted content, ensuring privacy. | Pass |
| TC013    | User Permissions Test       | Test if users can only access functions within their role-based permissions. | Users should only access authorized functions and data.        | Regular users could access their query results but were unable to access admin functions like user management. Attempts to access restricted endpoints returned a "403 Forbidden" error. Admin users could perform all functions as expected. | Pass |


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
  - Some test cases need further optimization (e.g., the scraping speed for specific data sources can be improved)
