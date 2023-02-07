Introduction :

This python script generates a `highly secure password`, encrypts it and stores it in a file for each user. The password is `regeneratable` and `encrypted` using `SHA256`. The user must specify the purpose for the password generation in a single word and it will be added to the `filename` in the format "username_purpose.txt".

Requirements :

    - Python 3.x
    - os
    - hashlib
    - random
    - string
  
Usage :

    1- Run the script in a terminal or command prompt.
    2- Enter your desired username.
    3- Enter the purpose for password generation in a single word (e.g. linkedin, facebook, instagram).
    
    - The script will generate a password and ask if you like it. If not, you can regenerate another password until you are satisfied.
    - The encrypted password, username, purpose and the generated password will be stored in a file in the "your_passwords" folder.

Conclusion :

This script is a simple solution for `generating`, `encrypting` and `storing passwords` in a `secure` manner. It is easy to use and allows the user to regenerate a new password if they are not satisfied with the one generated. The encrypted password and user `details` are stored in a separate file for each user, making it easy to manage `multiple passwords`.
