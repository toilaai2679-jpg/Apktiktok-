BUFF TIM - SOURCE-BASED WEB PORT

This package is a web conversion of the interface/backend pieces that can be
verified statically from buff-tim.py. It does not invent a TikTok buff API.

Verified source components include:
- Python 3.11 version check in the original file
- tkinter-based desktop UI
- check_key function
- block_shortcuts using keyboard
- send_telegram_message using requests.post
- get_current_time
- get_system_info using platform/psutil

The original file's obfuscated payload does not expose a verified TikTok
like/follow/view API in the decoded static code. In particular, the visible
requests reference is inside send_telegram_message. Therefore the web button
is not wired to a fabricated buff endpoint.

Run on Render with:
  gunicorn app:app

For local testing:
  python app.py
