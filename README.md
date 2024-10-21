# IT-project-Team92

## Tech Stack:
+ Python 3.12
+ FastAPI: For building high-performance Web APIs.
+ Tortoise ORM: For interacting with the database.
+ Pydantic: For data validation and serialization.
+ JWT: For user authentication and authorization.
+ Docker: For containerizing the application, simplifying deployment and development.

## Project Structure
```plaintext
.
├── app
│   ├── api                    # Routes and views
│   │   ├── admin.py           # Admin-related routes
│   │   ├── auth.py            # User authentication-related routes
│   │   ├── __init__.py        # Route initialization
│   ├── config.py              # Configuration file, manages environment variables
│   ├── db
│   │   ├── init_db.py         # Database initialization
│   ├── main.py                # Application entry point
│   ├── models                 # Database model definitions
│   │   ├── company.py         # Company model
│   │   ├── __init__.py        # Model initialization
│   │   ├── risk.py            # Risk assessment-related models
│   │   └── user.py            # User model
│   ├── schemas                # Pydantic models for data validation
│   │   ├── __init__.py
│   │   └── user.py            # Pydantic models related to users
│   └── utils                  # Utility tools and helper functions
│       ├── security.py        # Security-related functions (e.g., password hashing)
│       └── token.py           # JWT token-related functions
├── docker-compose.yml         # Docker Compose configuration file
├── Dockerfile                 # Docker image build file
├── requirements.txt           # Python dependencies list
└── tests                      # Test cases
    ├── conftest.py
    ├── __init__.py
    └── test_user.py           # User-related tests
```

## Installation & Running
### Prerequisites
- Docker
- Docker Compose

### Clone the Project
```bash
git clone https://github.com/RoyX0423/IT-project-Team92.git
cd IT-project-Team92/backend
```

### Running with Docker

1. Build and start services
```bash
docker compose up --build -d # Build and start all services in Docker, and run in the background
```
For real-time debugging of the backend service, run the backend service separately in Docker
```bash
docker compose up web # Start the web service in Docker and run in the foreground
```

2. The database management service will run at http://localhost:8000, no additional database management software is required.
3. Swagger UI will provide API documentation at http://localhost:8001/docs.

## Features Overview
### User Management
- [x] User Registration: POST /users/register
- [x] User Login: POST /users/login
- [x] Get Current User Information: GET /users/me
- [x] Change Password: PUT /users/password

### Admin Features
- [x] Admin Dashboard: GET /admin/admin-dashboard
- [x] View All Users: GET /admin/users

### Work Log for September 11, 2024

#### 1. **ASIC Query System Development**

Completed the development of an ASIC (Australian Securities and Investments Commission) query system based on DrissionPage. The system automates the process of interacting with the ASIC website using the ChromiumPage browser simulator. The specific tasks involved:
- Automated access to the ASIC search page, with a focus on selecting the "Organisation & Business Names" option from the drop-down menu.
- Input the target company name into the search field, triggered the search button, and then parsed the resulting table data. Filtered the visible rows and extracted the text from each column in those rows.
- Wrapped the functionality into an `ASICSearcher` class with two primary methods:
  - `search_asic(query)`: Accepts a query keyword, executes the search, and returns the matching results for the company name.
  - `close()`: Closes the browser instance after the search is completed, releasing resources.
- Tested the system with the search keyword `BHP`, verified the correctness of the program, and successfully extracted the ASIC registration data related to the company.

#### 2. **Google Custom Search API Integration**

Developed a system to perform company risk type checks using Google Custom Search API. Details of the implementation include:
- Developed a `RiskChecker` class to search for different risk types for companies using Google search. Key risk types include scandal, controversy, bribery, corruption, lawsuit, etc.
- `google_search(query)`: Executes the query using Google API, returning the title, link, and snippet of each result for further processing.
- `check_company_risks(company_name)`: Executes searches for multiple risk types for a given company name, returning a dictionary where the keys are risk types and the values are lists of search results.
- Tested risk checks for the company `BHP`, confirming that relevant Google search results were returned for each risk type.

#### 3. **Australian Company Information Query System**

Developed a system to query Australian company information based on the ROR API. The system allows the user to search for companies by name or keyword, filtering out those related to Australia. Specific tasks involved:
- Implemented functionality to retrieve company data from the ROR API and filter companies whose geographical location is "Australia."
- Structured the data into a Pandas DataFrame, including company name, ID, establishment date, company website links, and relationships with other entities.
- The `AustralianCompanySearcher` class provides the method `get_australian_companies(query)` to automatically retrieve and return the relevant companies. Tests were successful.
- Used `BHP` as the query keyword and successfully extracted information about Australian companies related to BHP.

#### 4. **Due Diligence Information System Analysis and Integration**

Analyzed the types of risks, information sources, and query channels involved in the due diligence process, and integrated these requirements into the developed query systems. Specific tasks included:
- Mapped multiple risk types from the due diligence process to the developed query tools (e.g., Google search, ASIC query, ROR API) and automated their retrieval.
- Built an automated company background checking system that covers aspects like company verification, reputational risk, commercial information, and legal risk, utilizing Google Custom Search API, ASIC registration checks, and other data sources based on the actual needs of due diligence.

#### 5. **System Testing and Optimization**

Performed integration testing and optimization on the developed systems:
- Conducted multiple tests on the Google Custom Search API to ensure that searches for different risk types returned expected results, especially when using various company names (e.g., BHP, Rio Tinto).
- Conducted extensive tests on the ASIC query system to ensure stable access to the ASIC website and proper extraction of search results.
- Optimized the API response time for the company information query system to ensure high performance during large-scale data queries.

#### 6. **Summary and Future Plans**
- The completed tasks include the core functionality for the due diligence system, involving company information queries and risk checks based on ASIC, Google Custom Search API, and ROR API.
- The next step is to further optimize the integration of search results, ensuring that risk information is automatically generated in final reports, and categorized by different risk weights. The system's functionality will also be extended to cover company information queries in other countries.


# Test Case: Check Specific Risk Type "Scandal" for Apple Company

| **Test Case ID** | TC001 |
|------------------|-------|
| **Test Title**   | Check specific risk type "scandal" for a company |
| **Precondition** | 1. Valid Google API Key and Search Engine ID<br>2. Internet connection established |
| **Test Steps**   | 1. Initialize the `RiskChecker` class with the provided API Key and Search Engine ID<br>2. Call the `check_single_risk` method, passing "Apple" as the company name and "scandal" as the risk type<br>3. Retrieve the search results |
| **Input Data**   | Company Name: "Apple"<br>Risk Type: "scandal" |
| **Expected Result** | The system returns search results related to the "scandal" risk type for Apple, with at least one result mentioning "batterygate" |
| **Actual Result**   | The system returned multiple results related to Apple "batterygate" scandal, including titles like "Apple sending iPhone 'batterygate' settlement payments" |
| **Status**       | Pass |

## Detailed Steps:

1. **Initialize `RiskChecker`**:
   - Input a valid Google API Key and Search Engine ID.
   - `python google.py`

2. **Call `check_single_risk`**:
   - Pass "Apple" as the company name and "scandal" as the risk type.

3. **Expected Result**:
   - The system should return search results related to Apple's scandal, particularly involving the "batterygate" incident.

4. **Actual Result**:
   - The test yielded multiple results about the "batterygate" incident, which confirms the functionality.

## Key Points for Academic Presentation:
- The test case demonstrates that the `RiskChecker` class works as expected when querying specific risks for a company using the Google API.
- It also shows the flexibility of the system to focus on a particular risk type instead of querying all types.

