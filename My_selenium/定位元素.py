#coding: utf-8
from selenium import webdriver
from time import sleep
import os
if 'HTTP_PROXY' in os.environ: del os.environ['HTTP_PROXY']

text = """<html>
    <head>
      <meta http-equiv="content-type" content="text/html;charset=utf-8" />
      <title>Form</title>
      <script type="text/javascript" async="" src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
      <link href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css" rel="stylesheet" />
      <script src="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/js/bootstrap.min.js"></script>
    </head>
    <body>
      <h3>simple login form</h3>
      <form class="form-horizontal">
        <div class="control-group">
          <label class="control-label" for="inputEmail">Email</label>
          <div class="controls">
            <input type="text" id="inputEmail" placeholder="Email" name="email">
          </div>
        </div>
        <div class="control-group">
          <label class="control-label" for="inputPassword">Password</label>
          <div class="controls">
            <input type="password" id="inputPassword" placeholder="Password" name="password">
          </div>
        </div>
        <div class="control-group">
          <div class="controls">
            <label class="checkbox">
              <input type="checkbox"> Remember me
            </label>
            <button type="submit" class="btn">Sign in</button>
            <a href="#">register</a>
          </div>
        </div>
      </form>
    </body>
  </html>"""
driver = webdriver.Chrome()
driver.get("https://open.163.com/special/openadvice/")
sleep(3)
checkboxs =driver.find_elements_by_name('checkbox')
for checkbox in checkboxs:
    checkbox.click()
driver.find_element_by_id('otheradvice').send_keys("Hello world")
driver.find_element_by_xpath('//*[@id="adviceForm"]/div[3]/input').click()
