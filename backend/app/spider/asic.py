from DrissionPage import ChromiumPage, ChromiumOptions

class ASICSearcher:
    def __init__(self):
        """
        初始化ASICSearcher类，配置ChromiumPage的选项。
        """
        self.options = ChromiumOptions()
        self.options.set_argument('--no-sandbox')
        self.options.headless(True)
        self.page = ChromiumPage(self.options)

    def search_asic(self, query):
        """
        在ASIC页面搜索指定的公司名称，并返回搜索结果
        :param query: 公司名称或查询关键字
        :return: 返回搜索结果，列表形式
        """
        url = "https://connectonline.asic.gov.au/RegistrySearch/faces/landing/SearchRegisters.jspx"
        self.page.get(url)

        select_element = self.page.ele('#bnConnectionTemplate:r1:0:searchPanelLanding:dc1:s1:searchTypesLovId::content')
        select_element.click()
        select_element.select.by_value(1)
        is_selected = select_element.select.selected_option
        input_element = self.page.ele('#bnConnectionTemplate:r1:0:searchPanelLanding:dc1:s1:searchForTextId::content')
        input_element.clear()
        input_element.input(query)

        go_ele = self.page.ele('#bnConnectionTemplate:r1:0:searchPanelLanding:dc1:s1:searchButtonId')
        go_ele.click()

        table_eles = self.page.eles('@class=af_table_data-row')
        result_data = []
        for row in table_eles.filter.displayed():  # 筛选显示的行
            row_data = []
            span_eles = row.eles('t:span')
            for cell in span_eles:  # 筛选显示的列
                row_data.append(cell.text)
            result_data.append(row_data)
        
        return result_data

    def close(self):
        """
        关闭浏览器
        """
        self.page.close()

# 使用示例
searcher = ASICSearcher()

# 调用封装的函数并传入查询关键字
query = 'BHP'
results = searcher.search_asic(query)

# 处理结果
for row in results:
    print(row)

# 完成后关闭浏览器
searcher.close()
