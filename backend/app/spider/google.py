import requests

class RiskChecker:
    def __init__(self, api_key, search_engine_id):
        """
        初始化RiskChecker类
        :param api_key: Google API Key
        :param search_engine_id: Google Search Engine ID
        """
        self.api_key = api_key
        self.search_engine_id = search_engine_id
        self.risk_types = [
            "scandal", 
            "controversy",  
            "refuse to comment",  
            "silent",  
            "fault", 
            "fail",  
            "decline to comment", 
            "allegations",  
            "bribery",  
            "corruption",  
            "military",  
            "defence",  
            "defense",  
            "arms",  
            "arms exports",  
            "financial loss", 
            "bankrupt",  
            "liquidator",  
            "administration",  
            "fraud",  
            "compliance action", 
            "money laundering", 
            "modern slavery",  
            "labour practices",  
            "human rights violations", 
            "exports violations", 
            "environmental violations", 
            "pollution", 
            "oil spill",  
            "chemical spill", 
            "ethical concerns",  
            "toxic waste", 
            "lawsuit", 
            "court proceeding",  
            "patent lawsuit",  
            "class action lawsuit", 
            "IP infringement",  
            "compliance breach",  
            "regulatory breach",  
            "privacy breach" 
        ]

    def google_search(self, query):

        url = f"https://www.googleapis.com/customsearch/v1?key={self.api_key}&cx={self.search_engine_id}&q={query}"
        response = requests.get(url)
        results = response.json()

        search_results = []
        if 'items' in results:
            for item in results['items']:
                result = {
                    "title": item.get('title'),
                    "link": item.get('link'),
                    "snippet": item.get('snippet')
                }
                search_results.append(result)

        return search_results

    def check_company_risks(self, company_name):

        all_results = {}

        for risk in self.risk_types:
            query = f"{company_name} {risk}"
            search_results = self.google_search(query)
            all_results[risk] = search_results

        return all_results



api_key = ''
search_engine_id = ''
risk_checker = RiskChecker(api_key, search_engine_id)


bhp_risk_results = risk_checker.check_company_risks("BHP")

