#This is deployment script for demo.py
echo "Going to stop py-app1..."
docker stop py-app1
echo "stoped py-app1..."
echo "Going to start py-app1 application"
#syntax
# docker run -it -p outside-port:inside-port -v outside-path : inside path --name container-name docker-image-name or id
docker start py-app1