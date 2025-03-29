# Dockerfile
# Usa uma imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código do projeto para o container
COPY . .

# Expõe a porta que o Flask usa (padrão: 5000)
EXPOSE 5000

# Comando para executar a aplicação
CMD ["python", "todo_project/run.py", "--host=0.0.0.0"]

