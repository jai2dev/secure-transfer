# secure-transfer

## A cloud based application for secure transfer of files using diffie hellman and AES algorithm

## Code Explanation

This implementation can be explained in two parts
* Main application (Cloud)
* stand-alone-application

### stand-alone-application

* This portion deals with encryption and decryption of file
* The file is encrypted using AES algorithm
* *Menu* option also helps to toggle the menu to upload and download files</br></br>

**/stand-alone-application/DH.py**:  This file deals with generating keys using diffie-hellman. It generates three keys: Private Key, Public Key, Secret Key (used for encryption and decryption)</br>
**/stand-alone-application/ENCDEC.py**: This file is used for encoding and decoding using AES algorithm.</br>
**/stand-alone-application/secure.py**: This file acts as a mediator and connect the main program with other code files.</br>
**/stand-alone-application/main.py**: This file deals with the GUI. Use this file to generate encoded file and decode the file</br>

### web-application

Once file is encrypted it has to be uploaded on an online directory. Another directory is needed where public-key of all the users is stored.</br>
**/app.py** Contains the website in **python-flask** which acts like a directory.


## you can use any hosting platform as long as you know what you are doing

### Hosting on AWS

* fork this repository
* create an amazon EC2 instance.
* Select and create **Amazon Linux AMI 2018.03.0 (HVM), SSD Volume Type**
* While creating the machine, toggle to menu *Configure Security Group* menu.
* Here, enable port SSH, HTTP, RDP and in port, change *Source* to **Anywhere**
* then on the instance page open the terminal and use the following commands
* $sudo bash
* $yum install python-pip
* $yum install git
* $pip install flask
* clone this repo in the instance
* $python app.py 
* open the localhost to run the application (for this instance you can open it using instance's ip address)




** accessing instance using putty
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
* $python app.py
