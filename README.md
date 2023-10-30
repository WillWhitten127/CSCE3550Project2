# CSCE3550Project2
This project is in python3

It is best to run on linux. The distro I used was debbian 12 bullseye

Explaining the code:

app.py:
    Imports Configuration:
        The necessary libraries and modules are imported.
        The Flask app is initialized.
        The SQLite database file (keys.db) path is specified.
Help Functions:
    get_db():
        This function establishes a connection to the SQLite database (keys.db) and returns the connection object.

    generate_rsa_key():
        For demonstration purposes, this function returns a dummy RSA private key string. In a real-world scenario, you would use a library, such as cryptography, to generate an actual RSA private key.

Routes and Endpoints:
    /generate-key (POST):
        Calls the generate_rsa_key() function to get an RSA key.
        Saves this key to the SQLite database with the current timestamp.
        Returns a message indicating the key has been generated and saved.

    /save-key (POST):
        Reads an RSA private key from the incoming JSON request.
        Saves this key to the SQLite database with the current timestamp.
        Returns a message indicating the key has been saved.

    /auth (POST):
        Checks for the presence of the "expired" query parameter.
        Depending on the "expired" parameter, it reads either an expired or unexpired RSA private key from the database.
        Generates a JWT token signed with the retrieved RSA key and sets an expiration time for the token (1 hour).
        Returns the JWT token and the used RSA key in the response.

    /.well-known/jwks.json (GET):
        Retrieves all RSA private keys from the SQLite database.
        Constructs a JWKS (JSON Web Key Set) response from these keys. (For simplicity, this demonstration uses the keys directly, but a proper JWKS would contain specific key attributes and metadata).
        Returns the JWKS response.

    Root (/) (GET):
        A simple endpoint that returns a greeting message. This is often used as a health check or a basic landing point for applications.

Execution:
    if name == 'main'::
        If the script is run directly (not imported as a module), the Flask app is started in debug mode. This allows for live reloading and provides detailed error messages.

databasesetup.py:
The script begins by importing the sqlite3 library, which allows for interaction with SQLite databases in Python.
The script defines the setup_database function, which is responsible for connecting to the SQLite database
The table, named keys, contains three columns:
    id: A unique identifier for each entry (key).
    key: The actual RSA key (or dummy key in our mockup).
    timestamp: The time when the key was added to the database.
The function ends by committing any changes and closing the connection to the database.


Steps to install and run:
1. sudo apt-get install python3-venv
2. pip install Flask
3. pip install PyJWT

Run the code:
4. source venv/bin/activate
5. python databasesetup.py
6. python app.py

http://127.0.0.1:5000/

Stop the process:
deactivate
 
