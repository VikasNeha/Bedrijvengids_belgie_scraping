from PageEvents.siteEvents import SiteEvents
import config
from Utilities.myLogger import logger
from PageEvents import inputContent


def doScrape():
    browser = SiteEvents()

    logger.info("Opening Browser...")
    browser.navigate(config.baseURL)
    logger.info("...Browser Opened")

    logger.info("Entering Parameters...")
    browser.fill_search_parameters()
    logger.info("...Parameters Entered")

    logger.info("Scraping Results...")
    browser.scrape_all_results()
    logger.info("... Results Scraped")

    if len(config.Results) == 0:
        logger.info("No Results")
        return "NO_RESULTS"

    logger.info("Writing CSV...")
    inputContent.write_csv_results()
    logger.info("...CSV Written")

    return 1