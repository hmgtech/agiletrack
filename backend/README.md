# AgileTrack Flask Application

AgileTrack is a Flask application designed to manage agile boards for project tracking. It provides functionalities for user authentication, board management, and email notifications.

## Features

- User Signup and Login: Secure user authentication with JWT tokens.
- Board Management: Create, update, share, and retrieve agile boards.
- Email Notifications: Send invitations to users to join boards via email.

## Technologies Used

- Python
- Flask
- MySQL
- JWT (JSON Web Tokens)
- Boto3 (AWS SDK for Python)
- SMTP (Simple Mail Transfer Protocol)

## Installation

1. Clone the repository:

```
git clone https://git.cs.dal.ca/courses/2024-winter/csci4145-5409/gupta2.git
cd AgileTrack
```


2. Install dependencies:
```
pip install -r requirements.txt
```

3. Set up environment variables:
   
   Create a `.env` file in the project root directory and add the following variables:

```
DBUSERNAME=<your_mysql_username>
PASSWORD=<your_mysql_password>
HOST=<your_mysql_host>
DATABASE=<your_mysql_database>
SECRET_KEY=<your_secret_key_for_jwt>
AWS_ACCESS_KEY_ID=<your_aws_access_key_id>
AWS_SECRET_ACCESS_KEY=<your_aws_secret_access_key>
AWS_SESSION_TOKEN=<your_aws_session_token>
```

4. Run the application:

```
python app.py
```


## Usage

- User Signup: Send a POST request to `/signup` with JSON payload containing `name`, `email`, and `password`.
- User Login: Send a POST request to `/login` with JSON payload containing `email` and `password`.
- Board Management: Use `/add_board`, `/update_board`, `/share_board`, `/get_boards` endpoints to manage boards.

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
