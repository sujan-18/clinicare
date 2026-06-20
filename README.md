\# CliniCare



CliniCare is a backend system for managing clinic appointments online.

&#x20;It allows patients to book appointments with doctors without needing 

to visit the hospital physically or be restricted by clinic hours.

&#x20;Patients can describe their health concerns when booking, and doctors

&#x20;can manage their appointments through their own dashboard.



\## Tech Stack

\- \*\*Backend Framework:\*\* Django

\- \*\*Database:\*\* PostgreSQL

\- \*\*API:\*\* Django REST Framework

\- \*\*Environment Management:\*\* python-decouple

\- \*\*Version Control:\*\* Git \& GitHub



\## Setup Instructions



1\. Clone the repository

```bash

git clone https://github.com/YOUR\_USERNAME/clinicare.git

cd clinicare

```



2\. Create a virtual environment

```bash

python -m venv env

```



3\. Activate the virtual environment

```bash

env\\Scripts\\activate

```



4\. Install dependencies

```bash

pip install -r requirements.txt

```



5\. Set up PostgreSQL database

```sql

CREATE DATABASE clinicare\_db;

CREATE USER clinicare\_user WITH PASSWORD 'your\_password';

GRANT ALL PRIVILEGES ON DATABASE clinicare\_db TO clinicare\_user;

GRANT ALL ON SCHEMA public TO clinicare\_user;

ALTER DATABASE clinicare\_db OWNER TO clinicare\_user;

```



6\. Create a `.env` file in the project root with the following content

DB\_NAME=clinicare\_db



DB\_USER=clinicare\_user



DB\_PASSWORD=your\_password



DB\_HOST=localhost



DB\_PORT=5432



7\. Run migrations

```bash

python manage.py migrate

```



8\. Run the development server

```bash

python manage.py runserver

```



