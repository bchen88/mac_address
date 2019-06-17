FROM python:2.7

ADD GetMacAddress.py /

RUN pip install requests

ENTRYPOINT ["python", "GetMacAddress.py"]
