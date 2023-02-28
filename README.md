![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
# Take Home 

## Quick Start 

Create the virtual enviroment with Poetry

```sh
$ poetry shell
```

Then install the dependencies

```sh
$ poetry install
```

To start the server run the command bellow

```sh
$ uvicorn app.main:app
```

Alternavily, if you want to make changes and don`t wanna to down the server and up again, run the commmand bellow

```sh
uvicorn app.main:app --reload
```

And after executing the previous command you can use all the resources FastAPI provide to us.

- Swagger: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

The endpoints of this project are `/balance`, `/event` and `/reset`

The `/balance` returns the balance from an `account_id` passed as `query_params` e.g: `/balance?account_id=100`

The `/event` get some functionalities, like `deposit`, `withdraw` and `transfer`, you can see the expected body in the docs mensioned before.

And thats all, thanks!