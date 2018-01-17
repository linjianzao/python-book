sudo pip install virtualenv
cd ~
mkdir env
cd env
virtualenv --no-site-packages localenv
source env/localenv/bin/activate

#退出
deactivate 


#注意：后续在虚拟环境里运行pip的时候 都不要加sudo
