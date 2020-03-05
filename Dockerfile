FROM tiangolo/uwsgi-nginx-flask:python3.7
RUN pip3 install prometheus_client
RUN pip3 install requests
RUN pip3 install flask
RUN pip3 install uwsgi
RUN pip3 install pyyaml
RUN pip3 install flask_prometheus_metrics
RUN pip3 install apscheduler
WORKDIR /app
ADD . /app
CMD python3 wsgi.py
ENV NGINX_WORKER_PROCESSES auto
ENV UWSGI_INI /app/metrics.ini
ADD uwsgi.conf /etc/nginx/conf.d/uwsgi.conf
ENV LISTEN_PORT 7000
EXPOSE 7000/tcp
