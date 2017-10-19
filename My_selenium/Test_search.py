import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#继承unittest标识这是一个测试类 setup为初始化方法
class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python",driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No reults found." not in driver.page_source
    def TearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()