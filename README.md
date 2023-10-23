# secure-transfer

## A cloud based application for secure transfer of text files using diffie hellman and AES algorithm

## Code Explanation

The implementation can be explained in two parts
* Main application (Cloud)
* stand-alone-application

### stand-alone-application

* Using the standalone app the user can encrypt or decrypt the file.
* The file is encrypted using AES algorithm.
* *Menu* option also helps to navigate through the menu to upload and download files</br></br>

**/stand-alone-application/DH.py**:  This file deals with generating keys using diffie-hellman. It generates three keys: Private Key, Public Key, Secret Key (used for encryption and decryption)</br>
**/stand-alone-application/ENCDEC.py**: This file is used for encoding and decoding using AES algorithm.</br>
**/stand-alone-application/secure.py**: This file acts as a mediator and connect the main program with other code files.</br>
**/stand-alone-application/main.py**: This file deals with the GUI.</br>

#### How to run the standalone app?
1) First install all the required packages from the requirement.txt file.
2) Open a terminal, and type python3 main.py in stand-alone-application. Use this file to generate encoded file and decode the file.

### web-application

Once file is encrypted it has to be uploaded on an online directory. Another directory is needed where public-key of all the users is stored.</br>
**/app.py** Contains the website in **python-flask** which acts like a directory.
