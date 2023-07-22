# Simultaneous-Translator

Este projeto tem como objetivo a criação de um programa que seja capaz de ouvir um áudio em portuguès e realizar sua tradução para o inglês, sendo sua saída um áudio em inglês.

Neste projeto foi utilizado o [Whisper](https://github.com/openai/whisper) para auxiliar no papel de tradução. O Whisper é um modelo de reconhecimento de fala de uso geral. Ele é capaz de ouvir o áudio em um determinado idioma e ralizar sua transcrição e tradução em inglês.

Para rodar este projeto em sua máquina local, é necessário ter instalada a última versão do [Pyhton](https://www.python.org/downloads/release/python-3114/) para que seja possível instalar e executar o Whisper. 

Para rodar este projeto em sua máquina local, também é necessário a instalação do Chocolatey. Caso você esteja utilizando Windows, um tutorial de instalação pode ser visto clicando [aqui](https://docs.chocolatey.org/en-us/choco/setup). Se atende em adicioná-lo ao `PATH` do Windows quado a instalação for finalizada.

Para executar o arquivo, abra o cmd do Windows ou o promp de comando do Linux. Vá até a pasta em que progra está instaldo e execute o arquivo projeto.py utilizando o comando:

> python .\projeto.py