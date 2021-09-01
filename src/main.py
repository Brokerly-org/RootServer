from uvicorn import run

from api import app


def main():
    run(app=app, host="127.0.0.1", port=9982)


if __name__ == "__main__":
    main()
