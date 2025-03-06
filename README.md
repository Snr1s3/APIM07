# APIM07

sudo docker start 2a20900c68f0 
sudo /home/ubuntu/APIM07/API/myenv/bin/uvicorn APIM07.API.main:app --host 0.0.0.0 --reload --port 443 --ssl-keyfile /home/ubuntu/APIM07/API/ssl/key.pem --ssl-certfile /home/ubuntu/APIM07/API/ssl/cert.pem