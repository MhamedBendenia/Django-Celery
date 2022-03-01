# Django-Celery

A basic Django Project with docker-compose to scrape Google Play Store reviews for a specific app. After scraping the results, they will be stored in the database.


Tools: Docker, Django, Celery, RabbitMQ, PostgreSQL


## Configuration

In the “hello_again/settings.py” file, modify the ID of the desired application as following

```bash
APP_ID = 'com.helloagain.helloagaindemo'
```

## Usage
You need to have docker installed in your system (https://www.docker.com/get-started)

Run the following command in the Terminal
```bash
docker-compose up
```

## Test
To ensure that the scrawler is working well, run the following commands

```bash
sudo docker exec -it <celery_container_id> bash
python manage.py test
```