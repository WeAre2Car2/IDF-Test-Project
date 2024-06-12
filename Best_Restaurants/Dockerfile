FROM python:3.10.5

FROM python:3.10.5

WORKDIR /Best_Restaurants

RUN pip install serpapi
RUN pip install flask

COPY . .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]