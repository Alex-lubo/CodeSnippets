HOW TO Setup PBE Server DEV envrionment(on ubuntu):


Step 1: Install docker

Please install the latest version of docker.
(reference URL: https://docs.docker.com/engine/installation/linux/ubuntulinux/)

// ensure APT works with https and CA certificates are installed.
	`~ sudo apt-get update`  
	`~ sudo apt-get install apt-transport-https ca-certificates`  

// Add the new GPG key
	`~ sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D`

	`~ sudo echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" | sudo tee /etc/apt/sources.list.d/docker.list`
	~ sudo apt-get update

// Verify the APT is pulling the right repository
	~ sudo apt-cache policy docker-engine

// install docker
	~ sudo apt-get install docker-engine

Step 2: Create a group called docker and add user into the docker group

	~ sudo usermod -a -G docker $USER
warning: need to log out

Step 3: Run docker

	~ sudo service docker restart

Step 4: Install fig

(Reference URL: http://www.fig.sh/install.html)

	~ sudo curl http://jenkins-butler.nj.trantect.com:8080/job/fig/lastSuccessfulBuild/artifact/dist/fig -o /usr/local/bin/fig
	~ sudo chmod +rx /usr/local/bin/fig

Step 5: Install iojs

	// install nvm , see https://github.com/creationix/nvm
	~ curl -sL https://deb.nodesource.com/setup_iojs_2.x | sudo bash -apt-get install iojs
or
	~ nvm install iojs_2.x

Step 6: Checkout code

	~ git clone ssh://git@gitlab_address:10022/JY/xinjingyun.git

Step 7: install modules

	~ cd xinjingyun
	~ sudo npm install -g bower
	~ make npm

Step 8: install FE modules

	~ cd pbe-reborn
	~ bower install

(if emit bower-art-resolver error:
	~ sudo npm install bower-art-resolver

 if  npm install canvas error:
	~ sudo apt-get install --no-install-recommends -y libssl-dev libcairo2-dev libjpeg8-dev libpango1.0-dev libgif-dev build-essential g++

 if npm install grpc error:
	~ sudo apt-get install --no-install-recommends -y libssl-dev libcairo2-dev libjpeg8-dev libpango1.0-dev libgif-dev build-essential g++
	~ sudo apt-get install libgrpc-dev
）	

Step 9: Pull base images

	~ curl http://jenkins-butler.nj.trantect.com:8080/view/JingYun/job/Jingyun_gocd_Docker_beta/lastSuccessfulBuild/artifact/build/butler-server.tar.gz | docker load

Step 9: Start up

	~ fig -p butler up -d
	~ fig -p butler logs web

then open browser and connect to 127.0.0.1:3000



HOW TO Run PBE Server test：


Option 1: Run Front-end Test

	~ ./run_karma_test.sh
	~ ./run_mocha_controller_test.sh

Option 2： Run Back-end Test

	~ ./run run_all_backend_tests.sh
