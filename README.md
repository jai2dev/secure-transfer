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
