from DrissionPage import ChromiumPage, ChromiumOptions

class ASICSearcher:
    def __init__(self):

        self.options = ChromiumOptions()
        self.options.set_argument('--no-sandbox')
        self.options.headless(True)
        self.page = ChromiumPage(self.options)

    def search_asic(self, query):

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
        for row in table_eles.filter.displayed():  
            row_data = []
            span_eles = row.eles('t:span')
            for cell in span_eles: 
                row_data.append(cell.text)
            result_data.append(row_data)
        
        return result_data

    def close(self):

        self.page.close()


searcher = ASICSearcher()


query = 'BHP'
results = searcher.search_asic(query)


for row in results:
    print(row)


searcher.close()
