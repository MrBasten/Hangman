FROM python:3.9
# set work directory
WORKDIR /bot
# copy project
COPY . .
RUN pip install -r ./requirements.txt
CMD ["python", "bot_telegram.py"]
