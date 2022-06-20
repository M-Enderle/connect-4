FROM python:3.10-alpine

# copy application into the container
RUN pip install termtables
COPY * usr/
RUN mkdir save_games

# run connect4
CMD ["python3", "usr/main.py"]
