FROM python:3.11-slim

WORKDIR /app
COPY . .

# Install Chrome + WebDriver
RUN apt-get update && \
    apt-get install -y wget chromium && \
    wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip -d /usr/bin/ && \
    rm chromedriver_linux64.zip

RUN pip install -r requirements.txt

CMD ["pytest", "tests/", "-v", "--html=report.html"]
