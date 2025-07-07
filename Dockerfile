FROM redhat/ubi8
RUN yum install python3 -y && pip install flask
RUN python3 myapp.py

