<h1>Some automated tests for <i>planetainstrument.ru</i> website</h1>

---

<p align="center">
    <img width="200" height="200" src="img/logo.png">
</p>

<h2><img width="40" align="center" src="img/description.png"> Description</h2>
<li><a href="#tools">Tools</a></li>
<li><a href="#tests">Tests</a></li>
<li><a href="#run-tests">Run tests</a></li>
<li><a href="#test-example">Example of passing test</a></li>
<li><a href="#telegram-notification">Telegram notifications</a></li>

---

<h2 id="tools"><img width="40" align="center" src="img/tools.png"> Tools</h2>
<div align="center">
    <img title="Pytest" width="40" src="img/pytest.png">
    <img title="Python" width="40" src="img/python.png">
    <img title="Selenium" width="40" src="img/selenium.png">
    <img title="Selene" width="40" src="img/selene.png">
    <img title="PyCharm" width="40" src="img/pycharm.png">
    <img title="Jenkins" width="40" height="40" src="img/jenkins.png">
    <img title="Selenoid" width="40" src="img/selenoid.png">
    <img title="Allure" width="40" src="img/allure.png">
    <img title="Github" width="40" src="img/github.png">
    <img title="Telegram" width="40" src="img/telegram.png">
</div>
<p>Autotests are written in <b>Python</b> using <b>Selenide</b> for <i>UI tests</i></p>
<p>Tests are run from <b>Jenkins</b></p>
<p><b>Selenoid</b> is used to launch the browser</p>
<p><b>Allure report</b> is generated and sent to telegram</p>

---

<h2 id="tests"><img width="40" align="center" src="img/tests.png"> Tests</h2>

<p><img width="20" align="center" src="img/checkbox.png" alt="checkbox"> Adding item to cart test</p>
<p><img width="20" align="center" src="img/checkbox.png" alt="checkbox"> Authorization with valid parameters test</p>
<p><img width="20" align="center" src="img/checkbox.png" alt="checkbox"> Main page test</p>
<p><img width="20" align="center" src="img/checkbox.png" alt="checkbox"> Sorting products by price starting from cheap test</p>
<p><img width="20" align="center" src="img/checkbox.png" alt="checkbox"> Wishlist test</p>


---

<h2 id="run-tests"><img width="40" align="center" src="img/run-tests.png" alt="run"> Run tests</h2>

<pre>
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    pytest ${TESTS_FOLDER} --browser_version=${BROWSER_VERSION}
</pre>
<p><b>Parameters</b>: 
    <li>BROWSER_VERSION - browser version in which the tests will be run</li>
</p>

---

<p>To run tests in Jenkins you need to click on <b>Build with Parameters</b> button</p>
<img src="img/build.png" alt="build">
<p>Сhoose parameters (<i>BROWSER_VERSION, ENVIRONMENT, COMMENT</i>) and click on <b>"Build"</b> button</p>
<img src="img/parameters.png" alt="parameters">
<p>After passing the tests report will be generated, you can see it by clicking on the <b>Allure report</b></p>
<img src="img/allure-report.png" alt="allure-report">
<img src="img/allure-result.png" alt="allure-result">

---

<h2 id="test-example"><img width="40" align="center" src="img/example.png" alt="exapmle">Example of adding product to cart test</h2>
<img src="img/test-example.gif" alt="test">

---

<h2 id="telegram-notification"><img width="40" align="center" src="img/notification.png" alt="exapmle">Telegram notifications</h2>
<img src="img/report-telegram.png" alt="report-telegram">
