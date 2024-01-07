from tests.utils import TestUtils
from sites.verla import verlaScraper
import pytest
import allure
import requests

company_name = 'verla'

@pytest.fixture(scope="module", autouse=True)
def get_job_details():
    """
    Fixture for scraping process from the career section.
    """
    scraper_data = verlaScraper().return_data()
    scraped_jobs_data = TestUtils.scrape_jobs(scraper_data[0])
    peviitor_jobs_data = TestUtils.scrape_peviitor(scraper_data[1], 'România')
    return scraped_jobs_data, peviitor_jobs_data
    

# Utility function for checking missing items
def get_missing_items(list_a, list_b):
    return [item for item in list_a if item not in list_b][:20]

# Check function for job titles
def check_job_titles(expected_titles, actual_titles):
    missing_titles = get_missing_items(expected_titles, actual_titles)

    if missing_titles:
        msg = f"Peviitor is having extra job titles: {missing_titles}"
    else:
        missing_titles = get_missing_items(actual_titles, expected_titles)
        msg = f"Peviitor is missing job titles: {missing_titles}"

    if not expected_titles and not actual_titles:
        msg = f"Scraper is not grabbing any job titles"

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

    if not expected_cities and not actual_cities:
        msg = f"Scraper is not grabbing any job cities"

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

    if not expected_countries and not actual_countries:
        msg = f"Scraper is not grabbing any job countries"

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

    if not expected_links and not actual_links:
        msg = f"Scraper is not grabbing any job links"

    allure.step(msg)
    assert expected_links == actual_links, msg

# Test functions

@pytest.mark.regression
@pytest.mark.API
def test_verla_title_api(get_job_details):
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
def test_verla_city_api(get_job_details):
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
def test_verla_country_api(get_job_details):
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
def test_verla_link_api(get_job_details):
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


@pytest.mark.regression
@pytest.mark.API
def test_vetro_status_code_link_api(get_job_details):
    allure.dynamic.title(f"Test http code response on job links for {company_name} website")

    scraped_jobs_data, peviitor_jobs_data = get_job_details
    with allure.step("Step 1: Get job links from the scraper"):
        job_links_scraper = sorted(scraped_jobs_data[3])

    with allure.step("Step 2: Check job links for response code"):
        status_codes_expected_result = [200] * len(job_links_scraper)
        status_codes_actual_result = [requests.get(link).status_code for link in job_links_scraper]
        allure.attach(f"Expected Results: {status_codes_expected_result}", name="Expected Results")
        allure.attach(f"Actual Results: {status_codes_actual_result}", name="Actual Results")
        check_job_links(status_codes_expected_result, status_codes_actual_result)