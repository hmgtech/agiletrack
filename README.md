# AgileTrack

AgileTrack is a project management tool designed to help teams manage their tasks and projects efficiently. This README file provides information about setting up and using AgileTrack.

App Link: https://agiletrack.guptahitesh.me/

## Table of Contents
- [Frontend](#frontend)
  - [Installation](#frontend-installation)
  - [Usage](#frontend-usage)
  - [Features](#frontend-features)
- [Backend](#backend)
  - [Technologies Used](#backend-technologies-used)
  - [Installation](#backend-installation)
  - [Usage](#backend-usage)
- [Contributing](#contributing)
- [License](#backend-license)

## Frontend

### Frontend Installation

To install AgileTrack frontend, follow these steps:

1. Clone the repository: `git clone <repository_link>`
2. Navigate to the project directory: `cd frontend`
3. Install dependencies: `npm install`

### Frontend Usage

To start the application, run the following command:

```bash
npm run start
```

This will launch the application in development mode.

To build the application for production, run:

```bash
npm run build
```

### Frontend Features

- **Kanban Board**: Visualize your workflow using a Kanban board.
- **User Authentication**: Secure user authentication system.
- **Board Management**: Add, view, and manage boards for your projects.
- **Responsive Design**: Accessible and optimized for various devices.

### Frontend License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Backend

### Backend Technologies Used

- Python
- Flask
- MySQL
- JWT (JSON Web Tokens)
- Boto3 (AWS SDK for Python)
- SMTP (Simple Mail Transfer Protocol)

### Backend Installation

To install AgileTrack backend, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/hmgtech/agiletrack
cd backend
```

2. Install dependencies:

```bash
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

```bash
python app.py
```

### Backend Usage

- User Signup: Send a POST request to `/signup` with JSON payload containing `name`, `email`, and `password`.
- User Login: Send a POST request to `/login` with JSON payload containing `email` and `password`.
- Board Management: Use `/add_board`, `/update_board`, `/share_board`, `/get_boards` endpoints to manage boards.

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## Backend License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
