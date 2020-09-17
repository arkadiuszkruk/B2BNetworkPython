# B2BNetworkPython
Program został napisany w PyCharmie, aby go uruchomić należy posiadać zainstalowanego Pythona oraz PyCharma na swoim komputerze.
Aby program można było uruchomić i dobrze się uruchamiał, należy zainstalować plugin Gherkin w PyCharmie oraz z poziomu konsoli następujące narzędzia:
pip install behave                -instalacja behave
pip install selenium              -instalacja selenium
pip install pytest-bdd            -instalacja pytest
pip install -r requirements.txt   -instalacja requirementsow zawartych w programie
Należy również umieścić w zmiennych systemowych ścieżkę do geckodrivera (Mozilla Firefox) - https://github.com/mozilla/geckodriver/releases tu możemy znaleźć 
plik do porania, do którego należy podać ścieżkę

Aby uruchomić test należy z poziomu aplikacji w konsoli PyCharma wpisać pytest -v -s 
