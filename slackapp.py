from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import pytz

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day of the week
    current_day = datetime.now(pytz.UTC).strftime('%A')

    # Get current UTC time with a +/-2 minute window
    current_time = datetime.now(pytz.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Define the GitHub repository URL and file name
    github_repo_url = "https://github.com/emmyxo/Slack"
    file_name = "slackapp.py"  # Use the specific file name "slackapp.py"

    # Construct the GitHub file URL
    github_file_url = f"{github_repo_url}/blob/main/{file_name}"

    # Create the response JSON
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)  # Changed to port 8081
