TEST_PATH=./test/

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force  {} +

test: clean
	python3 $(TEST_PATH)/test_integracion_lazy.py
