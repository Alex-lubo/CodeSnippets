1. Log into your machine as a user with sudo or root privileges.

2. Open a terminal window.

3. Update package information, ensure that APT works with the https method, and that CA certificates are installed.

	$ sudo apt-get update
	$ sudo apt-get install apt-transport-https ca-certificates

4. Add the new GPG key. This commands downloads the key with the ID 58118E89F3A912897C070ADBF76221572C52609D from the keyserver hkp://ha.pool.sks-keyservers.net:80 and adds it to the adv keychain. For more info, see the output of man apt-key.

	$ sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
	
5. Find the entry in the table below which corresponds to your Ubuntu version. This determines where APT will search for Docker packages. When possible, run a long-term support (LTS) edition of Ubuntu.
		   Ubuntu version 	Repository
		Precise   12.04 (LTS) 	deb https://apt.dockerproject.org/repo ubuntu-precise main
		Trusty    14.04 (LTS) 	deb https://apt.dockerproject.org/repo ubuntu-trusty main
		Wily      15.10 	deb https://apt.dockerproject.org/repo ubuntu-wily main
		Xenial    16.04 (LTS) 	deb https://apt.dockerproject.org/repo ubuntu-xenial main

    Note: Docker does not provide packages for all architectures. Binary artifacts are built nightly, and you can download them from https://master.dockerproject.org. To install docker on a multi-architecture system, add an [arch=...] clause to the entry. Refer to Debian Multiarch wiki for details.

6. Run the following command, substituting the entry for your operating system for the placeholder <REPO>.

	$ echo "<REPO>" | sudo tee /etc/apt/sources.list.d/docker.list

7. Update the APT package index.

	$ sudo apt-get update

8. Verify that APT is pulling from the right repository.

When you run the following command, an entry is returned for each version of Docker that is available for you to install. Each entry should have the URL https://apt.dockerproject.org/repo/. The version currently installed is marked with ***.The output below is truncated.

	$ apt-cache policy docker-engine

	  docker-engine:
	    Installed: 1.12.2-0~trusty
	    Candidate: 1.12.2-0~trusty
	    Version table:
	   *** 1.12.2-0~trusty 0
		  500 https://apt.dockerproject.org/repo/ ubuntu-trusty/main amd64 Packages
		  100 /var/lib/dpkg/status
	       1.12.1-0~trusty 0
		  500 https://apt.dockerproject.org/repo/ ubuntu-trusty/main amd64 Packages
	       1.12.0-0~trusty 0
		  500 https://apt.dockerproject.org/repo/ ubuntu-trusty/main amd64 Packages


