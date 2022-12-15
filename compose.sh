# 需要在根目录使用（即包含frontend、backend...的目录）
# 运行sh ./compose.sh start指令
git pull origin dev
docker stop $(docker ps -q)
cd ./frontend
sudo rm -rf ./dist/
npm run build
sudo rm -rf ../compose/nginx/dist/
cp -r ./dist/ ../compose/nginx/
cd ..
sudo docker-compose build
sudo docker-compose up