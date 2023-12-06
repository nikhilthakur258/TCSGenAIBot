from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://www.example.com")

try:
    # Click on "Upload Files"
    upload_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Upload Files"))
    )
    upload_button.click()

    # Page reloads
    driver.refresh()

    # Click on "Spreadsheet Formats"
    spreadsheet_formats = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Spreadsheet Formats"))
    )
    spreadsheet_formats.click()

    # Buttons "XLS" and "XLSX" should show
    assert WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "XLS"))
    )
    assert WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "XLSX"))
    )

    # Click on "XLSX"
    xlsx_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "XLSX"))
    )
    xlsx_button.click()

    # Select "500kb-sheet.xlsx"
    upload_input = driver.find_element_by_xpath('//input[@type="file"]')
    upload_input.send_keys("path/to/500kb-sheet.xlsx")

    # Upload completes
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "uploaded-files-table"), "500kb-sheet.xlsx")
    )

    # Click on "XLSX" again
    xlsx_button.click()

    # Select "1mb-sheet.xlsx"
    upload_input.send_keys("path/to/1mb-sheet.xlsx")

    # Upload fails
    WebDriverWait(driver, 10).until_not(
        EC.text_to_be_present_in_element((By.ID, "uploaded-files-table"), "1mb-sheet.xlsx")
    )

    # Click on "Login"
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
    )
    login_button.click()

    # Enter credentials and sign in
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_field.send_keys("testuser123")

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_field.send_keys("$Pass123")

    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
    )
    sign_in_button.click()

    # Page reloads
    driver.refresh()

    # Assertions after signing in
    assert WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "uploaded-files-table"), "500kb-sheet.xlsx")
    )

    assert WebDriverWait(driver, 10).until_not(
        EC.text_to_be_present_in_element((By.ID, "uploaded-files-table"), "1mb-sheet.xlsx")
    )

    # Continue with additional steps...

finally:
    # Close the browser window
    driver.quit()
