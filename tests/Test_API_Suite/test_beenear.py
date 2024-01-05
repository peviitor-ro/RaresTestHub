from tests.utils import TestUtils
from sites.beenear import BeenearScraper
import pytest
import allure

def get_jobs_careers():
    """
    Fixture for scraping process from the career section.
    """
    return BeenearScraper().return_data()


scraper_data = get_jobs_careers()
scraped_jobs_data = TestUtils.scrape_jobs(scraper_data[0])

peviitor_jobs_data = TestUtils.scrape_peviitor(scraper_data[1], 'România')

company_name = 'beenear'

@pytest.mark.regression
@pytest.mark.API
def test_beenear_title_api():
    
    allure.dynamic.title(f"Test job titles from the {company_name} website against Peviitor API Response")

    with allure.step("Step 1: Get job titles from the scraper"):
        job_titles_scraper = sorted(scraped_jobs_data[0])
    
    with allure.step("Step 2: Get job titles from the Peviitor API"):
        job_titles_peviitor = sorted(peviitor_jobs_data[0])
    
    missing_job_titles = []
    # Itterate over job titles and if not present on peviitor add to missing job title list
    for job_title in job_titles_scraper:
        if job_title not in job_titles_peviitor:
            missing_job_titles.append(job_title)
    
    with allure.step("Step 3: Compare job titles from scraper response against Peviitor API Response"):
        # If the missing job list is empty it might mean there are more jobs on peviitor than needed
        if missing_job_titles == []:
            missing_job_titles_peviitor = []
            for job_title in job_titles_peviitor:
                if job_title not in job_titles_scraper:
                    missing_job_titles_peviitor.append(job_title)
                    
            # If there are way too many jobs titles only list a couple of them
            if len(missing_job_titles_peviitor) > 20:
                missing_job_titles_peviitor = f"{missing_job_titles_peviitor[:5]} and many more"
                            
            print(f"Expected Results: {job_titles_scraper}\n")
            print(f"Actual Results: {job_titles_peviitor}")
            assert job_titles_scraper == job_titles_peviitor, f"Peviitor is having the following extra jobs titles: {missing_job_titles_peviitor}\n\n"
        else:
            if len(missing_job_titles) > 20:
                missing_job_titles = f"{missing_job_titles[:5]} and many more"
                
            print(f"Expected Results: {job_titles_scraper}\n")
            print(f"Actual Results: {job_titles_peviitor}")
            assert job_titles_scraper == job_titles_peviitor, f"Peviitor is missing the following job titles: {missing_job_titles}\n\n"
            
@pytest.mark.regression
@pytest.mark.API
def test_beenear_city_api():
    
    allure.dynamic.title(f"Test job cities from the {company_name} website against Peviitor API Response")
    
    with allure.step("Step 1: Get job cities from the scraper"):
        job_cities_scraper = sorted(scraped_jobs_data[1])
    
    with allure.step("Step 2: Get job cities from the Peviitor API"):
        job_cities_peviitor = sorted(peviitor_jobs_data[1])
    
    with allure.step("Step 3: Compare job cities from scraper response against Peviitor API Response"):
        print(f"Expected Results: {job_cities_scraper}\n")
        print(f"Actual Results: {job_cities_peviitor}")
        
        if job_cities_scraper != job_cities_peviitor:
            assert job_cities_scraper == job_cities_peviitor, f"Peviitor is having extra jobs cities\n\n"
        else:
            assert job_cities_scraper == job_cities_peviitor, f"Peviitor is missing job cities\n\n"
        
             
@pytest.mark.regression
@pytest.mark.API
def test_beenear_country_api():
    
    allure.dynamic.title(f"Test job countries from the {company_name} website against Peviitor API Response")
    
    with allure.step("Step 1: Get job countries from the scraper"):
        job_countries_scraper = sorted(scraped_jobs_data[2])
    
    with allure.step("Step 2: Get job countries from the Peviitor API"):
        job_countries_peviitor = sorted(peviitor_jobs_data[2])
    
    with allure.step("Step 3: Compare job countries from scraper response against Peviitor API Response"):
        print(f"Expected Results: {job_countries_scraper}\n")
        print(f"Actual Results: {job_countries_peviitor}")
        if job_countries_scraper != job_countries_peviitor:
            assert job_countries_scraper == job_countries_peviitor, f"Peviitor is having extra job countries\n\n"
        else:
            assert job_countries_scraper == job_countries_peviitor, f"Peviitor is missing job countries\n\n"

@pytest.mark.regression
@pytest.mark.API
def test_beenear_link_api():
    
    allure.dynamic.title(f"Test job links from the {company_name} website against Peviitor API Response")
    
    with allure.step("Step 1: Get job links from the scraper"):
        job_links_scraper = sorted(scraped_jobs_data[3])
    
    with allure.step("Step 2: Get job links from the Peviitor API"):
        job_links_peviitor = sorted(peviitor_jobs_data[3])
    
    missing_job_links = []
    
    for job_link in job_links_scraper:
        if job_link not in job_links_peviitor:
            missing_job_links.append(job_link)
    
    with allure.step("Step 3: Compare job links from scraper response against Peviitor API Response"):
        print(f"Expected Results: {job_links_scraper}\n")
        print(f"Actual Results: {job_links_peviitor}")
        if missing_job_links == []:
            missing_job_links_peviitor = []
            if job_link in job_links_peviitor:
                if job_link not in job_links_scraper:
                    missing_job_links_peviitor.append(job_link)
                    
            if len(missing_job_links_peviitor) > 20:
                missing_job_links_peviitor = f"{missing_job_links_peviitor[:5]} and many more"
            assert job_links_scraper == job_links_peviitor, f"Peviitor is having the following extra jobs links: {missing_job_links_peviitor}\n\n"
        else:
            if len(missing_job_links) > 20:
                missing_job_links = f"{missing_job_links[:5]} and many more"
            assert job_links_scraper == job_links_peviitor, f"Peviitor is missing the following job links: {missing_job_links}\n\n"
            
