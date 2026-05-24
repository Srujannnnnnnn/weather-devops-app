import json

# We create a static data structure that represents our weather information
weather_data = {
    "status": "online",
    "message": "Welcome to the DevOps Weather Portal!",
    "city": "Mysuru",
    "temperature": "30°C",
    "condition": "Sunny"
}

# This script generates a beautiful HTML index file when run by the pipeline
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Weather Dashboard</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
        .card {{ background: white; padding: 30px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); text-align: center; max-width: 400px; width: 100%; }}
        h1 {{ color: #1a73e8; margin-bottom: 5px; }}
        .status {{ color: #34a853; font-weight: bold; margin-bottom: 20px; }}
        .temp {{ font-size: 48px; color: #202124; font-weight: bold; margin: 15px 0; }}
        .city {{ font-size: 20px; color: #5f6368; }}
        .footer {{ margin-top: 25px; font-size: 12px; color: #aaaeB3; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>{weather_data['city']} Weather</h1>
        <div class="status">● {weather_data['status']}</div>
        <div class="temp">{weather_data['temperature']}</div>
        <p>Condition: <strong>{weather_data['condition']}</strong></p>
        <p style="color: #666;">{weather_data['message']}</p>
        <div class="footer">Deployed Automatically via GitHub Actions CI/CD</div>
    </div>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)

print("index.html created successfully!")