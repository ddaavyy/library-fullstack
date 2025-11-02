FROM python:3.11-alpine

# Definindo o diretório de trabalho
WORKDIR /app

# Copiar arquivos de requisitos e instalar dependências
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Criar o ambiente virtual
RUN python3 -m venv /app/venv

# Ativar o ambiente virtual
ENV PATH="/app/venv/bin:$PATH"

# Copiar o restante do código para dentro do contêiner
COPY . .

# Expõe a porta 8000 para o Django
EXPOSE 8000

# Comando para rodar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
