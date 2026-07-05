# Greeting & Live Clock 🕒

A tiny example web app with a **real backend**, built to learn how to deploy from GitHub to [Render](https://render.com) for free.

It's a Python [Flask](https://flask.palletsprojects.com/) server that greets you and shows a live clock. The clock updates every second by asking the server for the current time at `/api/time` — which is what makes this a *backend* app rather than a plain static page.

## What's inside

| File | What it does |
|------|--------------|
| `app.py` | The Flask server — defines the web page and the `/api/time` endpoint |
| `templates/index.html` | The web page, with a little JavaScript that fetches the time each second |
| `requirements.txt` | The Python packages Render installs (Flask + gunicorn) |
| `render.yaml` | Tells Render how to build and run the app |
| `.gitignore` | Keeps junk files out of the repo |

## Run it locally

You need Python 3 installed. Then, in this folder:

```bash
# 1. (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 2. Install the dependencies
pip install -r requirements.txt

# 3. Start the app
python app.py
```

Now open **http://localhost:5000** in your browser.

## Deploy it to Render (free)

1. Push this project to a GitHub repository.
2. Sign in to [Render](https://render.com) (you can sign up with your GitHub account).
3. Click **New → Web Service** and connect this repository.
4. Render reads `render.yaml` and fills in the settings for you:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `gunicorn app:app --bind 0.0.0.0:$PORT`
   - **Instance type:** Free
5. Click **Create Web Service** and wait a couple of minutes for the build.
6. Render gives you a live URL like `https://greeting-clock.onrender.com` 🎉

> **Note:** On Render's free tier the app "sleeps" after 15 minutes of no visitors, so the first visit after a while takes ~30–50 seconds to wake up. That's normal.

## How it works

```
Browser  ──GET /──▶  Flask (app.py)  ──renders──▶  index.html
Browser  ──GET /api/time──▶  Flask  ──▶  { "time": "14:23:05", ... }  (JSON, every second)
```

Made as a first backend project. More to come!
