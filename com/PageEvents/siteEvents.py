# -*- coding: utf-8 -*-
from webpageEvents import WebpageEvents
import config
from Utilities.constants import IDMODE
from inputContent import Result
from Utilities.myLogger import logger


class SiteEvents(WebpageEvents):
    def __init__(self):
        super(SiteEvents, self).__init__()

    def destroy(self):
        super(SiteEvents, self).destroy()

    def fill_search_parameters(self):
        if config.Arrondissement:
            self.select_option_from_dropdown(IDMODE.NAME, "search_national_arrondissements_id", config.Arrondissement)
        if config.Naam:
            self.enterText(IDMODE.ID, "search_national_name", config.Naam)
        if config.Rubriek:
            self.enterText(IDMODE.ID, "search_national_trade", config.Rubriek)
        if config.Postcode:
            self.enterText(IDMODE.ID, "search_national_zipcode", config.Postcode)
        if config.Gemeente:
            self.enterText(IDMODE.ID, "search_national_city", config.Gemeente)
        self.findElement(IDMODE.ID, "search_national_submit-button").click()

    def scrape_all_results(self):
        i = 1
        while True:
            # scrape results on a page
            self.waitUntilElementIsPresent(IDMODE.XPATH, "//table[@class='list-font-head']")
            self.scrape_results_on_page()

            # go to next page
            nextButtonTable = self.driver.find_element_by_xpath("//table[@class='list-font-head']")
            if ">>" in nextButtonTable.text:
                logger.info("Page " + str(i))
                nextButton = nextButtonTable.find_elements_by_tag_name("td")[2]
                nextButton.find_element_by_tag_name("a").click()
                i += 1
            else:
                break

    def scrape_results_on_page(self):
        resultsTable = self.findElement(IDMODE.CLASS, "table-background-orange")
        trs = resultsTable.find_elements_by_xpath("tbody/tr")
        resultsTable = trs[2]
        resultsTable = resultsTable.find_element_by_tag_name("table")
        resultsTable = resultsTable.find_element_by_tag_name("table")
        resultsTable = resultsTable.find_elements_by_tag_name("tr")[0]
        resultsTable = resultsTable.find_element_by_tag_name("td")
        tables = resultsTable.find_elements_by_tag_name("table")

        table_num = 1

        curr_result = None
        for table in tables:
            if table_num % 3 == 1:
                name_tag = table.find_elements_by_xpath("tbody/tr/td")[0]
                if table_num == 1:
                    if name_tag.text.strip() == "":
                        break
                curr_result = Result()
                curr_result.Name = name_tag.text.strip()
            elif table_num % 3 == 2:
                trs = table.find_elements_by_tag_name("tr")

                row = trs[0]
                row_columns = row.find_elements_by_tag_name("td")
                curr_result.Street = row_columns[0].text.strip()
                curr_result.Phone = row_columns[2].text.strip()
                curr_result.Email = row_columns[4].text.strip()

                row = trs[1]
                row_columns = row.find_elements_by_tag_name("td")
                curr_result.City = row_columns[0].text.strip()

                config.Results.append(curr_result)

            table_num += 1