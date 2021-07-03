## How to use

### Step-by-Step commands

#### Make Migrations (Local)
> heroku local:run python manage.py makemigrations dashboard

#### Push to Github
> git add .

> git commit -m "Message"

> git push origin main

#### Migrate
> heroku run python manage.py migrate -a my-dashboard-heroku

#### Run Locally
> heroku local web -f Procfile.windows