# Ares
teste de leitura e escrita via mqtt

# Como executar (Windows)
1. Instale o [mosquitto](https://mosquitto.org/download/)

execute os comandos abaixo no CMD na pasta do projeto

2. Cria ambiente virtual python (opcional)
```cmd
python -m venv .venv
.venv\Scripts\activate
```
3. instale as dependências e execute os scripts
```cmd
pip install -r requirements.txt
python publisher.py
python subscriber.py server.py
python server.py
```
4. No navegador, acesse 127.0.0.1:8007

