# secure-transfer

## A cloud based application for secure transfer of files using diffie hellman and AES algorithm

## Code Explanation

This implementation can be explained in two parts
* stand-alone-application
* web-application

### stand-alone-application

![stand-alone-application](/dump/images/GUI.PNG)

* This portion deals with encryption and decryption of file
* The file is encrypted using AES algorithm
* *Menu* option also helps to toggle the menu to upload and download files</br></br>

**src/stand-alone-application/DH.py**:  This file deals with generating keys using diffie-hellman. It generates three keys: Private Key, Public Key, Secret Key (used for encryption and decryption)</br>
**src/stand-alone-application/ENCDEC.py**: This file is used for encoding and decoding using AES algorithm.</br>
**src/stand-alone-application/thrain.py**: This file acts as a mediator and connect the main program with other code files.</br>
**src/stand-alone-application/main.py**: This file deals with the GUI. It is the main file [yeah, trust me!].</br>

### web-application
![web-application](/dump/images/home.png)


Once file is encrypted it has to be uploaded on an online directory. Another directory is needed where public-key of all the users is stored. Thus, we built an online directory and hosted it on cloud. The unique thing about hosting is that dynamic files are being generated while adding a new user or uploading a text file. Thus, we needed a cloud service which could run the program and incorporate the dynamic files. We tried free services like pivotal and heroku but then amazon AWS came to our rescue.</br>
**src/web-application/app.py** Contains the website in **python-flask** which acts like a directory.

### Hosting on AWS

* fork this repository
* create an amazon EC2 instance.
* Select and create **Amazon Linux AMI 2018.03.0 (HVM), SSD Volume Type**
* While creating the machine, toggle to menu *Configure Security Group* menu.
* Here, enable port SSH, HTTP, RDP and in port, change *Source* to **Anywhere**
* Download and keep the **publicKeyPair.pem file**
* Install *putty* and *puttygen*
* Open puttygen, select the publicKeyPair.pem and generate a private key. Now, save it as **Save private key**
* Open the AWS machine dashboard ad copy the *IPv4 Public IP* of the instance created
* Open putty
* In putty, copy the IP in *Host Name(or IP address)*
* In putty, toggle the SSH>Auth and here, select the *private key* you generated.
* Click open and voila! The terminal of instance opens
* -----------------------------------------------------
* Enter "login as:" ec2-user
* Enter following command
* $sudo bash
* $yum install python-pip
* $yum install git
* $pip install flask
* Now, clone the forked repository on local machine
* In src/web-application/app.py, comment on line 169 and uncomment line 168
* Update the github repository
* On the terminal of instance, clone the repository and enter command
* $python app.py
