FROM python

RUN mkdir -p /app
WORKDIR /app
COPY . .

RUN python3 -m pip install --upgrade \
    pip \
    wheel

RUN pip install -r requirements.txt

CMD [ "python3", "-m", "WebStreamer" ]
