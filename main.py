from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#initialize the webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
output=list()

# navigate to the URL to scrape
driver.get('https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787')
count=0
# setup wait for the element(s) to become available
wait = WebDriverWait(driver, 100)
for row in range (1,5):
    data = list()
    row=str(row)
    if int(row)==1 and count==0:
        # Different X_path for 1st row
        element=wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="table_id"]/tbody/tr[' +row+ ']/td[2]/a/b')))
        count=count+1
    else:
        # Different X_path for further row
        row=int(row)
        row=row-1
        row=str(row)

        element=wait.until(EC.visibility_of_element_located((By.XPATH,'// *[ @ id = "' +row+ '"] / td[2] / a / b')))
        ActionChains(driver).move_to_element(element).perform()


    data.append(element.text)
    # append quest name
    element.click()

    element1 =wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[1]/td[2]')))
    # append closing date
    data.append(element1.text)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[1]/td[2]')))
    element2 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[3]/td[2]')))
    ActionChains(driver).move_to_element(element2).perform()
    element2 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[3]/td[2]')))
    element3 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="current_project"]/div/div[3]/div/table/tbody/tr[2]/td[2]')))
    ActionChains(driver).move_to_element(element3).perform()
    element3 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="current_project"]/div/div[3]/div/table/tbody/tr[2]/td[2]')))
    # append EST. Values
    data.append(element2.text)
    # append description
    data.append(element3.text)
    #append the list into the output list
    output.append(data)
    searchpostings = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="topMain"]/li[1]/a')))
    searchpostings.click()


# close the webdriver
driver.quit()

# print the output
print(output)
