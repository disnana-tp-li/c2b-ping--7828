# Ping Analyzer Bot

A Discord bot for measuring and analyzing ping times.

## Setup

1.  **Create a Discord Bot:** Follow the instructions on the Discord Developer Portal to create a new bot and obtain its token.
2.  **Invite the Bot to Your Server:** Use the OAuth2 URL Generator in the Discord Developer Portal to generate an invite link with the `bot` scope and the necessary permissions (e.g., `read messages`, `send messages`, `use slash commands`).
3.  **Clone the Repository:**
    ```bash
    git clone [repository_url]
    cd [repository_directory]
    ```
4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Configure Environment Variables:**
    -   Create a `.env` file in the project root.
    -   Add the following variables to the `.env` file, replacing the placeholders with your actual values:
        ```
        DISCORD_TOKEN=YOUR_BOT_TOKEN
        # Add other environment variables as needed
        ```
6.  **Run the Bot:**
    ```bash
    python main.py
    ```

## Features

-   Real-time ping measurement
-   Averaged ping calculation
-   Configurable ping alert thresholds
-   Ping logging to a specified channel
-   Ping visualization (graphs)
-   Historical ping data retrieval
-   Ping race game
-   Ping challenge game
-   Ping statistics (min, max, avg, stddev)
-   Outlier detection in ping data

## Commands

-   `/ping_check`: Checks the current ping.
-   `/ping_average`: Calculates the average ping over a period.
-   `/ping_alert_threshold`: Sets the ping alert threshold.
-   `/ping_log_channel`: Sets the channel for ping logs.
-   `/ping_visualize`: Visualizes ping data.
-   `/ping_history`: Retrieves historical ping data.
-   `/ping_race`: Starts a ping race game.
-   `/ping_challenge`: Starts a ping challenge game.
-   `/ping_stats`: Displays ping statistics.
-   `/ping_outliers`: Detects ping outliers.

## Deployment

This bot is designed for deployment on platforms like Koyeb.  Ensure that the `keep_alive.py` script is running to keep the bot active.

## Contributing

[Contribution guidelines]

## License

[License information]