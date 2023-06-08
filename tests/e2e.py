import sys

from selenium import webdriver

def test_scores_service(application_url):
    try:
        driver = webdriver.Safari()
        driver.get(application_url)
        score = driver.find_element(by="id", value="score").text
        return 1 <= int(score) <= 1000
    except BaseException as e:
        # print(e)
        return False
    finally:
        driver.close()


def main_function():
    test = test_scores_service('http://localhost:8080/score')
    result = -1 if test else 0

    sys.exit(result)


exit(main_function())
