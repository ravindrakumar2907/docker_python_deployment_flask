FROM python:2.7.17

WORKDIR /usr/src/app

EXPOSE 5000

COPY demo.py ./demo.py

COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN ls -al

CMD [ "python", "./demo.py" ]

#ENTRYPOINT ["dotnet", "WebApp.dll"]