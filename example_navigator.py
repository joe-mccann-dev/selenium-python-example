import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class ExampleNavigator(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_navigate_careers_page(self):
        driver = self.driver
        driver.get("http://techspacesolutions.com")
        self.assertIn("TechSpace", driver.title)
        careers_link = driver.find_element(By.LINK_TEXT, "Careers")
        careers_link.click()
        self.assertIn("Currently we have openings in the following areas", driver.page_source)

        apply_link = driver.find_element(By.LINK_TEXT, "Click here to Apply")
        href = apply_link.get_attribute('href')
        self.assertIn(href, "mailto:careers@techspacesolutions.com")

    def test_navigate_contact_us_page(self):
        driver = self.driver
        driver.get("http://techspacesolutions.com/contactus.html")
        contact_us_text = driver.find_element(By.CSS_SELECTOR, ".cntus_txt").text
        self.assertIn(contact_us_text, "5 Independence Way, Suite 135,\nPrinceton NJ – 08540\nPhone : (732) 640 1204")
        
    def tearDown(self):
        self.driver.close()
    

if __name__ == "__main__":
    unittest.main()
