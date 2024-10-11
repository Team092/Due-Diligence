import requests
import pandas as pd

class AustralianCompanySearcher:
    def __init__(self):

        self.api_url = "https://api.ror.org/v2/organizations"

    def get_australian_companies(self, query):

        url = f"{self.api_url}?query={query}"
        res = requests.get(url)
        data = res.json()

        company_data = []


        for company in data.get('items', []):

            is_australia_related = False
            if company.get('locations'):
                for location in company['locations']:
                    if location['geonames_details']['country_name'] == "Australia":
                        is_australia_related = True
                        break


            if is_australia_related:
                company_info = {
                    'name': company['names'][0]['value'],
                    'id': company['id'],
                    'established': company.get('established', 'NA'),
                    'links': [link['value'] for link in company.get('links', [])],
                    'locations': [(location['geonames_details']['country_name'], location['geonames_details']['name']) for location in company.get('locations', [])],
                    'relationships': [(rel['type'], rel['label']) for rel in company.get('relationships', [])]
                }
                company_data.append(company_info)


        df = pd.DataFrame(company_data)
        
        return df


searcher = AustralianCompanySearcher()
query = 'BHP'
result_df = searcher.get_australian_companies(query)

