from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time


def extract_text_from_span_box(driver):
    # Find the span elements containing each letter in the box
    span_elements = driver.find_elements_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[2]/div/span')

    # Extract text from each span element
    extracted_text = ''.join([span.text for span in span_elements])

    return extracted_text


def main():
    url = "https://humanbenchmark.com/tests/typing"

    chrome_options = webdriver.ChromeOptions()
    driver_path = "./chromedriver"
    chrome_options.add_argument("executable_path=" + driver_path)

    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the web application
    driver.get(url)

    # Wait for the page to load (you might need to adjust the sleep duration)
    time.sleep(3)

    try:
        # Extract text from the span box
        extracted_text = extract_text_from_span_box(driver)

        # Output the extracted text
        print("Extracted Text:", extracted_text)

        # Find the certain box where you want to write the text
        target_box = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[2]/div')

        # Clear the existing text in the box
        target_box.clear()

        # Write the extracted text into the box (remove spaces)
        target_box.send_keys(extracted_text.replace(" ", ""))

        # Press Enter (optional, you can remove this if not needed)
        target_box.send_keys(Keys.ENTER)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Close the webdriver
        driver.quit()


if __name__ == "__main__":
    main()
