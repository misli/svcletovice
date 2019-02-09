ARG LEPRIKON_TAG=latest
FROM leprikon/leprikon:$LEPRIKON_TAG

LABEL maintainer="Jakub Dorňák <jakub.dornak@misli.cz>"

# install other dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# copy files
COPY svcletovice /app/svcletovice
COPY htdocs/__maintenance__.html /app/htdocs/__maintenance__.html
COPY conf/nginx.conf /app/conf/nginx.conf

ENV SITE_MODULE=svcletovice

# run this command at the end of any dockerfile based on this one
RUN leprikon collectstatic --no-input
