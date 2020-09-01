#This is deployment script for demo.py
echo "Going to stop py-app1..."
docker stop py-app1
echo "stoped py-app1..."
echo "Going to remove py-app1..."
docker rm -f py-app1
echo "removed py-app1..."
echo "Going to remove image  py-app..."
docker rmi -f py-app
echo "removed image py-app..."
echo "Going to build image  py-app..."
docker build . -t py-app
echo "build done image py-app..."
echo "Going to run image  py-app... for py-app1 application"
#syntax
# docker run -it -p outside-port:inside-port -v outside-path : inside path --name container-name docker-image-name or id
docker run -it -p 5000:5000 -v /Users/ravindramore/git/reports/my_docker/python_deployment/:/usr/src/app/ --name py-app1 py-app