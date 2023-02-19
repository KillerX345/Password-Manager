# Password-Manager
This is a simple password manager program written in Python. It allows users to store and retrieve passwords for various accounts. The passwords are stored in a file named "passwords.json" which is encrypted using the Fernet encryption scheme from the cryptography library.
The program allows users to perform the following tasks:

    Add a new password by entering a username and password. The program checks the strength of the password and provides feedback on how to create a stronger password.
    Retrieve a password for a given username.
    Generate a random password of a specified length.
    Decrypt and display the passwords stored in the encrypted file.
    Quit the program.
