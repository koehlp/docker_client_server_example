# docker_client_server_example


####Run docker server
cd flask_server \
sudo docker build --no-cache -t flask_server . \
sudo docker run --name flask_server --rm -it flask_server

The server will print its ip. 

####Run docker request client

cd docker_request_client \
sudo docker build -t clireq --no-cache -f Dockerfile . \
sudo docker run  -e server_ip="put in server ip" clireq



