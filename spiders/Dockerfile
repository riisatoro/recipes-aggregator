FROM python:3.10

WORKDIR /app/

COPY . .

RUN apt-get update
RUN apt-get -y install cron
RUN pip install -r requirements.txt

WORKDIR /app/recipes_scrapper/

# RUN crontab -l | { cat; echo "*/1 * * * * bash /app/runspider.sh"; } | crontab -
