from splinter import Browser

url = "https://www.twilio.com/voice"

def put_call_request(mob, c_code="+91"):
    mob = c_code + str(mob)

    with Browser() as browser:
        browser.visit(url)
        inp = browser.find_by_xpath('//input[@role="number"]')
        btn = browser.find_by_xpath('//button[text()="Call my phone"]')
        inp.first.value = mob
        btn.first.click()

put_call_request("9708323700")
