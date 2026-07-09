# MSA Script Builder — WALKING SKELETON (Milestone 1 in SPEC.md)
#
# What this file does, in plain words:
#   1. It runs a tiny web server on this computer.
#   2. It shows the page in app/index.html in your browser.
#   3. When staff types a message on that page, this file sends it to
#      Claude (the AI) and sends Claude's answer back to the page.
#
# That's the whole "walking skeleton": page -> Claude -> answer on screen.
#
# To start it, run this in Terminal:
#   python3 "/Users/owendewinne/MSA Director Project/app/server.py"
# Then open  http://localhost:8000  in your browser.

import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

import anthropic

# ---- Where things live ----
APP_FOLDER = Path(__file__).parent               # the "app" folder
KEY_FILE = APP_FOLDER.parent / "api_key.txt"     # the secret key file (never goes to GitHub)

# ---- How Claude should behave (from SPEC.md safety rules) ----
CLAUDE_INSTRUCTIONS = """You are the brainstorm partner inside the MSA Script Builder,
a tool used at Märchen Sagen Academy, where kids ages 4-10 make short films.

A staff member is typing to you. Kids never talk to you directly.
The staff member reads your questions out loud to the kids and types their answers back.

Your job right now: help turn a kid's vague story idea into a solid story
by asking ONE fun, simple question at a time.

Rules you must always follow:
- Keep everything age-appropriate and encouraging.
- Write at about a 6-year-old's reading level. Short sentences.
- Use fun film-set vocabulary (director, scene, action!) when it fits.
- Never ask for or mention children's names or personal details.
  If any appear, gently remind staff: "describe the story, not the kids."
"""


# ---- Practice mode (free) ----
# Used when there is no API key yet. The app answers with pretend
# questions so we can build and test every screen without paying.
# The moment a real key is in api_key.txt, real Claude takes over.
PRACTICE_REPLIES = [
    "Ooh, I love it! 🎬 Every great movie starts with a hero.\nWho is the main character of this story?",
    "Great choice, director! 🌟\nWhere does the story happen? A castle? A school? Outer space?",
    "Wonderful! Now the exciting part...\nWhat goes WRONG? Every good story has a problem to solve!",
    "Oh no! 😱 That's a great problem.\nHow does our hero try to fix it? What's their big plan?",
    "Amazing! And here's my last big question...\nHow does the story END? Happy? Funny? A surprise?",
    "🎉 That's a whole story! When the REAL Claude is connected, "
    "I'll help you turn this into a script. For now: CUT! Great practicing!",
]


def practice_reply(history):
    """Pick the next pretend reply, based on how far the conversation is."""
    turns = sum(1 for message in history if message["role"] == "user")
    reply = PRACTICE_REPLIES[min(turns - 1, len(PRACTICE_REPLIES) - 1)]
    return "🎭 PRACTICE MODE (free, not real Claude)\n\n" + reply


def read_api_key():
    """Read the secret key from api_key.txt. Returns None if it's not set up yet."""
    try:
        key = KEY_FILE.read_text().strip()
    except FileNotFoundError:
        return None
    if not key.startswith("sk-ant-"):
        return None  # still the placeholder text, not a real key
    return key


def ask_claude(history):
    """Send the conversation to Claude and return Claude's reply as text."""
    client = anthropic.Anthropic(api_key=read_api_key())
    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=16000,
        thinking={"type": "adaptive"},
        system=CLAUDE_INSTRUCTIONS,
        messages=history,
    )
    # Claude's reply can have several parts; we collect the text parts.
    return "".join(block.text for block in response.content if block.type == "text")


class RequestHandler(BaseHTTPRequestHandler):
    """Answers the two things the browser asks for: the page, and Claude replies."""

    def do_GET(self):
        # The browser asks for the page -> send index.html
        page = (APP_FOLDER / "index.html").read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(page)

    def do_POST(self):
        # The page sends the conversation -> we ask Claude -> send back the reply
        length = int(self.headers.get("Content-Length", 0))
        data = json.loads(self.rfile.read(length))

        if read_api_key() is None:
            # No key yet -> free practice mode with pretend answers
            reply = {"text": practice_reply(data["history"])}
        else:
            try:
                reply = {"text": ask_claude(data["history"])}
            except anthropic.AuthenticationError:
                reply = {"error": "The API key doesn't work. Check api_key.txt."}
            except anthropic.APIError as problem:
                reply = {"error": f"Claude had a problem: {problem.message}"}

        body = json.dumps(reply).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass  # keep the Terminal window quiet


if __name__ == "__main__":
    print("MSA Script Builder skeleton is running!")
    print("Open this in your browser:  http://localhost:8000")
    print("(Press Ctrl+C here to stop it.)")
    HTTPServer(("127.0.0.1", 8000), RequestHandler).serve_forever()
