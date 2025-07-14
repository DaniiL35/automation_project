from selenium.webdriver.common.by import By

amount = (By.ID, "etAmount")
term = (By.ID, "etTerm")
rate = (By.ID, "etRate")
calculate = (By.ID, "btnCalculate")
save = (By.ID, "btnSave")
repayment = (By.ID, "tvRepayment")
intrest = (By.ID, "TvIntrestOnly")


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver

    def get_amount(self):
        return self.driver.find_element_by_id([amount[0], amount[1]])

    def get_term(self):
        return self.driver.find_element_by_id(term[0], term[1])

    def get_rate(self):
        return self.driver.find_element_by_id(rate[0], rate[1])

    def get_calculate_button(self):
        return self.driver.find_element_by_id(calculate[0], calculate[1])

    def get_save_button(self):
        return self.driver.find_element_by_id(save[0], save[1])

    def get_repayment(self):
        return self.driver.find_element_by_id(repayment[0], repayment[1])

    def get_interest(self):
        return self.driver.find_element_by_id(intrest[0], intrest[1])
