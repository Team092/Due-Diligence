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
            "scandal",  # 丑闻
            "controversy",  # 争议
            "refuse to comment",  # 拒绝评论
            "silent",  # 沉默
            "fault",  # 过失
            "fail",  # 失败
            "decline to comment",  # 拒绝评论
            "allegations",  # 指控
            "bribery",  # 贿赂
            "corruption",  # 腐败
            "military",  # 军事
            "defence",  # 国防
            "defense",  # 防御
            "arms",  # 武器
            "arms exports",  # 武器出口
            "financial loss",  # 财务损失
            "bankrupt",  # 破产
            "liquidator",  # 清算人
            "administration",  # 管理
            "fraud",  # 欺诈
            "compliance action",  # 合规行动
            "money laundering",  # 洗钱
            "modern slavery",  # 现代奴隶制
            "labour practices",  # 劳工实践
            "human rights violations",  # 人权侵犯
            "exports violations",  # 出口违规
            "environmental violations",  # 环境违规
            "pollution",  # 污染
            "oil spill",  # 石油泄漏
            "chemical spill",  # 化学品泄漏
            "ethical concerns",  # 道德问题
            "toxic waste",  # 有毒废物
            "lawsuit",  # 诉讼
            "court proceeding",  # 法庭程序
            "patent lawsuit",  # 专利诉讼
            "class action lawsuit",  # 集体诉讼
            "IP infringement",  # 知识产权侵权
            "compliance breach",  # 合规违规
            "regulatory breach",  # 法规违规
            "privacy breach"  # 隐私泄露
        ]

    def google_search(self, query):
        """
        使用Google API执行搜索查询
        :param query: 搜索关键字
        :return: 返回搜索结果
        """
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
        """
        检查给定公司名称的所有风险类型
        :param company_name: 公司名称
        :return: 返回所有风险类型的搜索结果
        """
        all_results = {}

        for risk in self.risk_types:
            query = f"{company_name} {risk}"
            search_results = self.google_search(query)
            all_results[risk] = search_results

        return all_results


# 示例使用

# 初始化RiskChecker类，提供API Key和搜索引擎ID
api_key = ''
search_engine_id = ''
risk_checker = RiskChecker(api_key, search_engine_id)

# 检查BHP公司的所有风险类型
bhp_risk_results = risk_checker.check_company_risks("BHP")

# bhp_risk_results 将包含每个风险类型的搜索结果
