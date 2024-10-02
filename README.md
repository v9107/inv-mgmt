# Blooprint Inventory Management Assignment

- [x] setup user auth with jwt
- [x] API create and retriving jwt token
- [x] API to refresh jwt token
- [x] create models for inventory
- [x] create CRUP API's for inventory models
- [x] use Postgres Database
- [x] setup redis for cashing
- [x] setup logging for the application
- [x] test cases for Item CRUD API's.

## Setups
* PostgreSQL Database
    ``` bash
    docker run --name <container_name> -e POSTGRES_PASSWORD=<password> -d -p 5432:5432 postgres
    ```
* Redis for caching (here I have used docker)
    ``` bash
    docker run --name redis_cache -p 6379:6379 -d redis
    ```
* Install requirements
    ``` bash
    python -m pip install -r ./requirements.txt
    ```
* Add config.py file for storing config and secrets related to applications (sample config.py)
    ```python
    config = {}

    config['DB_NAME'] = '<database_name>'
    config['DB_USER'] = '<database_user>'
    config['DB_PASSWORD'] = '<database_password>'
    config['DB_HOST'] = '<database_host>'
    config['DB_PORT'] = '<database_port>'

    ```

### After settings up database and redis and installing all the required dependency run
``` bash
python ./store/manage.py runserver
```

## Links
- [LinkedIn](https://www.linkedin.com/in/venkatesh-k-20455a204/)
- venkateshkumbhar5700@gmail.com