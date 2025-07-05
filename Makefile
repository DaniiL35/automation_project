allure-run:
	( \
		cd test_cases && \
		pytest -s -v --maxfail=10 Test_web.py --alluredir=../allure-results && \
		cd .. && \
		allure serve allure-results \
	)
