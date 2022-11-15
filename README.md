# TDL_Tarefas
    Todo List - Gerêncie suas Tarefas


# Instalação 

1. Download do Repositório do Github

    git clone https://github.com/Erysilva98/TDL_Tarefas.git
#
2. Instalando a virtual Env

    *Use o CMD ou Terminal

    https://packaging.python.org/pt_BR/latest/guides/installing-using-pip-and-virtual-environments/

    py -m pip install --upgrade pip

    py -m pip install --user virtualenv
#
# Ativando ambiente virtual 

3. Sistema Windows: 

    > Acesse a Pasta do Projeto pelo CMD

    - Ativando ENV:

        .\winTdl\Scripts\activate

    - Instalando Dependências

        py -m pip install requests

        py -m pip install --upgrade requests

        py -m pip install -r requirements.txt
    
    - Iniciando o Projeto TDL

        python main.py

    - Desativando ENV:

        *Use apenas quando desejar encerrar o Projeto

        deactivate

# 

4. Sistema Linux/MacOs:

    > Acesse a Pasta do Projeto pelo Terminal 
    
    - Ativando ENV:

        source tdl/bin/activate

    - Instalando Dependências

        python -m pip install requests

        python -m pip install --upgrade requests

        python -m pip install -r requirements.txt
        
    - Iniciando o Projeto TDL

        python main.py

    - Desativando ENV:

        *Use apenas quando desejar encerrar o Projeto

        deactivate
