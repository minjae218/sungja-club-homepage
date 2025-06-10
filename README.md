git init
git add .
git commit -m "🎯 Sungja Club Init"
git branch -M main
git remote add origin https://github.com/너의아이디/sungja-club-homepage.git
git push -u origin main

## Automation Script

The `scripts` folder contains a sample Python script (`pictory_automation.py`) that demonstrates how to automate basic interactions with [pictory.ai](https://pictory.ai). It logs in with your credentials and submits a text script to generate a video.

### Requirements
- Python 3
- Dependencies listed in `scripts/requirements.txt`

### Running the script
Install the dependencies and execute the script:

```bash
pip install -r scripts/requirements.txt
python scripts/pictory_automation.py
```

Update the email, password, and script text inside the file before running.
