FROM python:3
WORKDIR /usr/src/app
ADD requirements.txt ./
RUN pip install --upgrade pip && \
    pip install numpy && \
    pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "./app.py" ]
