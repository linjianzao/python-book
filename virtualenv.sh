sudo pip install virtualenv
cd ~
mkdir env
cd env
virtualenv --no-site-packages localenv
source env/localenv/bin/activate

#退出
deactivate 
