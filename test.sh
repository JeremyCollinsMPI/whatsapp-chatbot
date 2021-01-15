docker build -t jeremycollinsmpi/chatbot .
backer_ip=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' backer)
docker run -it --rm -v $PWD:/src -p 5000:5000 -e backer_ip=$backer_ip --name chatbot jeremycollinsmpi/chatbot python test.py