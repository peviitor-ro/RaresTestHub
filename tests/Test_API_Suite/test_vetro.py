from tests.utils import TestUtils
from sites.vetro import vetroScraper
import pytest
import allure

company_name = 'vetro'

@pytest.fixture(scope="module", autouse=True)
def get_job_details():
    """
    Fixture for scraping process from the career section.
    """
    scraper_data = vetroScraper().return_data()
    scraped_jobs_data = TestUtils.scrape_jobs(scraper_data[0])
    peviitor_jobs_data = TestUtils.scrape_peviitor(scraper_data[1], 'România')
    return scraped_jobs_data, peviitor_jobs_data
    

# Utility function for checking missing items
def get_missing_items(list_a, list_b):
    return [item for item in list_a if item not in list_b][:40]

# Check function for job titles
def check_job_titles(expected_titles, actual_titles):
    missing_titles = get_missing_items(expected_titles, actual_titles)

    if missing_titles:
        msg = f"Peviitor is having extra job titles: {missing_titles}"
    else:
        missing_titles = get_missing_items(actual_titles, expected_titles)
        msg = f"Peviitor is missing job titles: {missing_titles}"

    allure.step(msg)
    assert expected_titles == actual_titles, msg

# Check function for job cities
def check_job_cities(expected_cities, actual_cities):
    missing_cities = get_missing_items(expected_cities, actual_cities)

    if missing_cities:
        msg = f"Peviitor is having extra job cities: {missing_cities}"
    else:
        missing_cities = get_missing_items(actual_cities, expected_cities)
        msg = f"Peviitor is missing job cities: {missing_cities}"

    allure.step(msg)
    assert expected_cities == actual_cities, msg

# Check function for job countries
def check_job_countries(expected_countries, actual_countries):
    missing_countries = get_missing_items(expected_countries, actual_countries)

    if missing_countries:
        msg = f"Peviitor is having extra job countries: {missing_countries}"
    else:
        missing_countries = get_missing_items(actual_countries, expected_countries)
        msg = f"Peviitor is missing job countries: {missing_countries}"

    allure.step(msg)
    assert expected_countries == actual_countries, msg

# Check function for job links
def check_job_links(expected_links, actual_links):
    missing_links = get_missing_items(expected_links, actual_links)

    if missing_links:
        msg = f"Peviitor is having extra job links: {missing_links}"
    else:
        missing_links = get_missing_items(actual_links, expected_links)
        msg = f"Peviitor is missing job links: {missing_links}"

    allure.step(msg)
    assert expected_links == actual_links, msg

# Test functions

@pytest.mark.regression
@pytest.mark.API
def test_vetro_title_api(get_job_details):
    allure.dynamic.title(f"Test job titles from the {company_name} website against Peviitor API Response")

    scraped_jobs_data, peviitor_jobs_data = get_job_details
    with allure.step("Step 1: Get job titles from the scraper"):
        job_titles_scraper = sorted(scraped_jobs_data[0])
    
    with allure.step("Step 2: Get job titles from the Peviitor API"):
        job_titles_peviitor = sorted(peviitor_jobs_data[0])

    with allure.step("Step 3: Compare job titles from scraper response against Peviitor API Response"):
        allure.attach(f"Expected Results: {job_titles_scraper}", name="Expected Results")
        allure.attach(f"Actual Results: {job_titles_peviitor}", name="Actual Results")
        check_job_titles(job_titles_scraper, job_titles_peviitor)

@pytest.mark.regression
@pytest.mark.API
def test_vetro_city_api(get_job_details):
    allure.dynamic.title(f"Test job cities from the {company_name} website against Peviitor API Response")

    scraped_jobs_data, peviitor_jobs_data = get_job_details
    with allure.step("Step 1: Get job cities from the scraper"):
        job_cities_scraper = sorted(scraped_jobs_data[1])
        
    with allure.step("Step 2: Get job cities from the Peviitor API"):
        job_cities_peviitor = sorted(peviitor_jobs_data[1])

    with allure.step("Step 3: Compare job cities from scraper response against Peviitor API Response"):
        allure.attach(f"Expected Results: {job_cities_scraper}", name="Expected Results")
        allure.attach(f"Actual Results: {job_cities_peviitor}", name="Actual Results")
        check_job_cities(job_cities_scraper, job_cities_peviitor)

@pytest.mark.regression
@pytest.mark.API
def test_vetro_country_api(get_job_details):
    allure.dynamic.title(f"Test job countries from the {company_name} website against Peviitor API Response")

    scraped_jobs_data, peviitor_jobs_data = get_job_details
    with allure.step("Step 1: Get job countries from the scraper"):
        job_countries_scraper = sorted(scraped_jobs_data[2])
    with allure.step("Step 2: Get job countries from the Peviitor API"):
        job_countries_peviitor = sorted(peviitor_jobs_data[2])

    with allure.step("Step 3: Compare job countries from scraper response against Peviitor API Response"):
        allure.attach(f"Expected Results: {job_countries_scraper}", name="Expected Results")
        allure.attach(f"Actual Results: {job_countries_peviitor}", name="Actual Results")
        check_job_countries(job_countries_scraper, job_countries_peviitor)

@pytest.mark.regression
@pytest.mark.API
def test_vetro_link_api(get_job_details):
    allure.dynamic.title(f"Test job links from the {company_name} website against Peviitor API Response")

    scraped_jobs_data, peviitor_jobs_data = get_job_details
    with allure.step("Step 1: Get job links from the scraper"):
        job_links_scraper = sorted(scraped_jobs_data[3])
    with allure.step("Step 2: Get job links from the Peviitor API"):
        job_links_peviitor = sorted(peviitor_jobs_data[3])

    with allure.step("Step 3: Compare job links from scraper response against Peviitor API Response"):
        allure.attach(f"Expected Results: {job_links_scraper}", name="Expected Results")
        allure.attach(f"Actual Results: {job_links_peviitor}", name="Actual Results")
        check_job_links(job_links_scraper, job_links_peviitor)