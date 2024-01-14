from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def extract_text_from_span_box(driver):
    # Find the span elements containing each letter in the box
    span_elements = driver.find_elements(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div[2]/div/span')

    # Extract text from each span element
    extracted_text = ''.join([span.text if span.text != '' else ' ' for span in span_elements])

    return extracted_text


def main():
    url = "https://humanbenchmark.com/tests/typing"

    chrome_options = webdriver.ChromeOptions()
    driver_path = "./chromedriver"
    chrome_options.add_argument("executable_path=" + driver_path)

    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the web application
    driver.get(url)

    try:
        # Wait for the span elements to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div[2]/div/span')))

        # Extract text from the span box
        extracted_text = extract_text_from_span_box(driver)

        # Output the extracted text
        print("Extracted Text:", extracted_text)

        # Find the certain box where you want to write the text
        target_box = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div[2]/div')

        # Write the extracted text into the box
        target_box.send_keys(extracted_text)

        time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Close the webdriver
        driver.quit()


if __name__ == "__main__":
    main()
