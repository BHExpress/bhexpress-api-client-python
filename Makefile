all: dist

dist:
	python3 setup.py sdist

upload: dist
	twine upload dist/*

install-dev:
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

tests: install-dev
	python tests/run.py

tests-readonly:
	python3 tests/run.py bhe.boletas.test_listar_bhes
	python3 tests/run.py bhe.boletas.test_calcular_monto_bruto
	python3 tests/run.py bhe.boletas.test_calcular_monto_liquido
	python3 tests/run.py bhe.receptores.test_listar_receptores
	python3 tests/run.py bhe.servicios.test_listar_servicios

docs:
	sphinx-apidoc -o docs bhexpress && sphinx-build -b html docs docs/_build/html

clean:
	rm -rf dist bhexpress.egg-info bhexpress/__pycache__ bhexpress/*.pyc
