# Telegram Bot for Training Studio

## Overview
This project is a Telegram bot designed for a training studio. The bot allows users to interact with the studio, learn about services, complete a questionnaire, select training directions, and manage bookings. It also includes an admin panel for managing user data and sending notifications.

## Features
- **User Interaction**: Users can learn about services, answer introductory questions, and select training options.
- **Payment Integration**: A placeholder for payment processing is included.
- **Database Management**: All user responses are stored in a SQLite database.
- **Admin Panel**: Admins can manage user data and send messages to users.
- **1C Integration**: Placeholder for future integration with 1C.
- **Dashboard**: A dashboard for the manager to view statistics and user engagement.

## Project Structure
```
project/
├── admin_panel/          # Admin panel functionalities
├── bot/                  # Bot functionalities
├── database/             # Database models and management
├── services/             # External service integrations
├── utils/                # Utility functions
├── .dockerignore         # Files to ignore in Docker
├── .env                  # Environment variables
├── .gitignore            # Files to ignore in Git
├── config.py             # Configuration settings
├── database.db           # SQLite database file
├── docker-compose.yml     # Docker configurations
├── Dockerfile            # Docker image build instructions
├── main.py               # Entry point of the application
└── requirements.txt      # Project dependencies
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd project
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Set up environment variables in the `.env` file.

## Running the Bot
To run the bot, execute the following command:
```
python main.py
```

## License
This project is licensed under the MIT License.