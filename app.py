"""
Greeting + Live Clock — a tiny Flask backend.

This is a real server-side app: every time the page loads (or the browser
asks /api/time), the server works out the current time and the right
greeting, then sends it back. That's what makes it a "backend" rather than
a plain static page.
"""

from datetime import datetime, timezone
from flask import Flask, render_template, jsonify

app = Flask(__name__)


def greeting_for_hour(hour: int) -> str:
    """Return a friendly greeting based on the hour of the day (0-23)."""
    if hour < 12:
        return "Good morning"
    if hour < 18:
        return "Good afternoon"
    return "Good evening"


def current_info() -> dict:
    """Build a small dictionary describing 'now' on the server (in UTC)."""
    now = datetime.now(timezone.utc)
    return {
        "greeting": greeting_for_hour(now.hour),
        "time": now.strftime("%H:%M:%S"),
        "date": now.strftime("%A, %d %B %Y"),
        "iso": now.isoformat(),
    }


@app.route("/")
def home():
    """The main web page."""
    return render_template("index.html", **current_info())


@app.route("/api/time")
def api_time():
    """A tiny JSON API the page calls once a second to update the clock."""
    return jsonify(current_info())


if __name__ == "__main__":
    # Local development only. On Render, gunicorn runs the app instead.
    app.run(host="0.0.0.0", port=5000, debug=True)
