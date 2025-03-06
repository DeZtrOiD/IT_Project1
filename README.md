# IT проект, 1 курс
Нейросеть [YOLO 11n](https://github.com/ultralytics/ultralytics)

  ## Установка необходмых модулей Python
  Для установки необходмых модулей Python используйте команду:
  ```
  pip install -r requirements.txt
  ```
<details><summary>Полный список необходимых модулей Python</summary>
  altair==5.5.0 <br>
  attrs==25.1.0 <br>
  blinker==1.9.0 <br>
  cachetools==5.5.2 <br>
  certifi==2025.1.31 <br>
  charset-normalizer==3.4.1 <br>
  click==8.1.8 <br>
  colorama==0.4.6 <br>
  contourpy==1.3.1 <br>
  cycler==0.12.1 <br>
  filelock==3.17.0 <br>
  fonttools==4.56.0 <br>
  fsspec==2025.2.0 <br>
  gitdb==4.0.12 <br>
  GitPython==3.1.44 <br>
  idna==3.10 <br>
  Jinja2==3.1.6 <br>
  jsonschema==4.23.0 <br>
  jsonschema-specifications==2024.10.1 <br>
  kiwisolver==1.4.8 <br>
  MarkupSafe==3.0.2 <br>
  matplotlib==3.10.1 <br>
  mpmath==1.3.0 <br>
  narwhals==1.29.0 <br>
  networkx==3.4.2 <br>
  numpy==2.1.1 <br>
  opencv-python==4.11.0.86 <br>
  packaging==24.2 <br>
  pandas==2.2.3 <br>
  pillow==11.1.0 <br>
  protobuf==5.29.3 <br>
  psutil==7.0.0 <br>
  py-cpuinfo==9.0.0 <br>
  pyarrow==19.0.1 <br>
  pydeck==0.9.1 <br>
  pyparsing==3.2.1 <br>
  python-dateutil==2.9.0.post0 <br>
  pytz==2025.1 <br>
  PyYAML==6.0.2 <br>
  referencing==0.36.2 <br>
  requests==2.32.3 <br>
  rpds-py==0.23.1 <br>
  scipy==1.15.2 <br>
  seaborn==0.13.2 <br>
  setuptools==75.8.2 <br>
  six==1.17.0 <br>
  smmap==5.0.2 <br>
  streamlit==1.43.0 <br>
  sympy==1.13.1 <br>
  tenacity==9.0.0 <br>
  toml==0.10.2 <br>
  torch==2.6.0 <br>
  torchvision==0.21.0 <br>
  tornado==6.4.2 <br>
  tqdm==4.67.1 <br>
  typing_extensions==4.12.2 <br>
  tzdata==2025.1 <br>
  ultralytics==8.3.84 <br>
  ultralytics-thop==2.0.14 <br>
  urllib3==2.3.0 <br>
  watchdog==6.0.0
</details>

## Установка пакетов
Для работы приложения также необходим пакет ***libgl1*** (необходим для модуля *opencv*):
```
sudo apt install libgl1
```

## Запуск приложения
Для запуска приложения необходимо использовать комманду:
```
streamlit run streamlit_app.py
```
И после открыть полученную ссылку в браузере.
