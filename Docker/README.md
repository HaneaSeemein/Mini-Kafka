# To build docker images
-sudo docker build -t broker1_image .
-sudo docker build -t broker2_image .
-sudo docker build -t broker3_image .
-sudo docker build -t zookeeper_image .

# To get rid of sudo
-sudo groupadd docker
-sudo usermod -aG docker $USER

# to run the containers with networking with one another (run in the folder of docker-compose.yml)
docker-compose up -d 

Then run the containers using
docker run <image_name>
