from selenium import webdriver


def test_scores_service(application_url):
    try:
        driver = webdriver.Safari()
        driver.get(application_url)
        score = driver.find_element(by="id", value="score").text
        if 1 <= int(score) <= 1000:
            return 1
        else:
            return 0
    except BaseException as e:
        # print(e)
        driver.close()
        return 0
    finally:
        driver.close()


def main_function():
    return test_scores_service('http://localhost:8080/score')


main_function()
