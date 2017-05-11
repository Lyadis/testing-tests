FROM lyadis/mvn-worker

RUN apt-get update && apt-get install -y python-pip libxml2-dev libxslt1-dev python-dev python-lxml


