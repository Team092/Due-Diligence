# Security Report: Due Diligence Automation System

## Project Overview
The development of the Due Diligence Automation System aims to help users automate the retrieval of business information and conduct risk assessments. Throughout this process, the system needs to handle a large amount of sensitive data, including financial information, legal records, and user query history. Ensuring the security of the system is a critical aspect of the project. By implementing various security measures, the system demonstrates robust security in data protection, access control, and network security.

## Project Security Issues
1. **Data Protection and Privacy**: Since the system handles large amounts of company data and user query information, some of which may be sensitive, ensuring the secure storage and transmission of data is a major concern. Unencrypted data storage or transmission could lead to data breaches, potentially compromising user privacy and damaging the reputation of the companies involved.

2. **SQL Injection Attacks**: The system frequently interacts with a database, storing user query records, company information, and risk assessment results. If user inputs are not properly sanitized, attackers could exploit the system through SQL injection attacks, potentially accessing or altering sensitive information in the database.

3. **CSRF (Cross-Site Request Forgery)**: Users interact with the system by submitting queries and performing actions based on returned data. Without adequate CSRF protection, attackers might trick users into submitting unauthorized requests while they are logged in, potentially leading to unintended malicious actions on the system.

4. **Access Control**: The system has different types of users, including regular users and administrators. Regular users should only be able to access functions that are within their scope, while administrators have broader permissions. Weak access control mechanisms could result in low-privilege users gaining access to high-privilege functions, posing a security risk.

## Solutions and Implementation
1. **Data Encryption**: To protect sensitive data, the system employs encryption during both data storage and transmission. All user query records and sensitive information are encrypted using AES before storage, and HTTPS is used for data transmission to ensure that data is not intercepted during transfer. Additionally, sensitive information such as passwords is hashed using algorithms like SHA-256 before being stored in the database, ensuring that even if the database is compromised, attackers cannot access plaintext information.

2. **SQL Injection Prevention**: The system uses parameterized queries and an ORM (Object Relational Mapping) framework to handle user inputs, ensuring that all input parameters in database queries are properly sanitized. This effectively prevents attackers from injecting malicious SQL statements to steal or manipulate data. Additionally, input validation is performed to filter out special characters, reducing the risk of code injection during data entry.

3. **CSRF Protection Mechanism**: The system generates a unique CSRF token when users submit forms and validates the token upon request submission. The request is processed only if the token in the request matches the server-generated token, preventing attackers from using a logged-in user's session to perform unauthorized actions. This mechanism ensures the legitimacy of user actions and effectively defends against CSRF attacks.

4. **Access Control and Role Management**: The system uses Role-Based Access Control (RBAC) to manage user permissions with precision. Regular users can access query and report viewing functions, while administrators have access to more sensitive functions like system settings and user management. The system verifies user identity with each request, ensuring that users can only access resources within their scope. Additionally, user permissions are regularly reviewed to ensure proper configuration.

## Conclusion
During the design and implementation of the Due Diligence Automation System, multiple security measures have been applied to ensure the overall security of the system. By addressing potential risks such as data protection, SQL injection, CSRF attacks, and access control, the system employs encryption, input validation, and access management to effectively minimize the risks of data breaches and security attacks. As the system continues to evolve, the team remains committed to maintaining a high level of security through regular audits and updates, ensuring that the system remains resilient against new threats.
