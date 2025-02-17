curl -L "https://www.futunn.com/download/fetch-lasted-link?name=opend-ubuntu" -o Futu_OpenD_latest.tar.gz
tar -xzvf Futu_OpenD_latest.tar.gz
cd Futu_OpenD_latest
find . -name 'FutuOpenD.xml'
find . -name 'AppData.dat'
./FutuOpenD -login_account=100000 -login_pwd=123456 -lang=en