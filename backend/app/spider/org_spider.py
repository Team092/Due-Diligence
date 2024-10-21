import requests
import pandas as pd

class AustralianCompanySearcher:
    def __init__(self):
        """
        初始化AustralianCompanySearcher类，不需要参数
        """
        self.api_url = "https://api.ror.org/v2/organizations"

    def get_australian_companies(self, query):
        """
        根据查询关键字从 ROR API 获取公司信息，筛选与澳大利亚相关的公司，并返回结果
        :param query: 要搜索的公司名称或关键字
        :return: 返回与澳大利亚相关的公司信息，DataFrame 形式
        """
        url = f"{self.api_url}?query={query}"
        res = requests.get(url)
        data = res.json()

        # 用于存储结果的列表
        company_data = []

        # 解析每个公司的信息
        for company in data.get('items', []):
            # 检查是否与澳大利亚有关联
            is_australia_related = False
            if company.get('locations'):
                for location in company['locations']:
                    if location['geonames_details']['country_name'] == "Australia":
                        is_australia_related = True
                        break

            # 如果公司与澳大利亚有关联，存储相关信息
            if is_australia_related:
                company_info = {
                    'name': company['names'][0]['value'],
                    'id': company['id'],
                    'established': company.get('established', '无信息'),
                    'links': [link['value'] for link in company.get('links', [])],
                    'locations': [(location['geonames_details']['country_name'], location['geonames_details']['name']) for location in company.get('locations', [])],
                    'relationships': [(rel['type'], rel['label']) for rel in company.get('relationships', [])]
                }
                company_data.append(company_info)

        # 将结果转换为 Pandas DataFrame
        df = pd.DataFrame(company_data)
        
        return df

# 示例使用
searcher = AustralianCompanySearcher()
query = 'BHP'
result_df = searcher.get_australian_companies(query)

# result_df 现在包含搜索结果，结果可以在此之后进一步处理
