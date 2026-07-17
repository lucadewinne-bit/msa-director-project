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
# To start it, run this in Terminal (from the repo root):
#   python3 app/server.py
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

How to guide every story (inspired by Dan Roam's book "Show and Tell"):
1. TELL THE TRUTH: the best stories come from real feelings. When a kid's
   idea hints at something they love, fear, or dream about, dig into that
   feeling - it's the heart of the movie.
2. TELL IT WITH A STORY: guide toward a drama arc - a hero we care about,
   their world, a problem in the way, a struggle where they try and fail,
   a change where they grow, and an ending that shows who they've become.
3. TELL IT WITH PICTURES: this is a movie, so ask picture questions:
   "What do we SEE when that happens?" If an answer can't be filmed,
   help turn it into something the camera can capture.

Rules you must always follow:
- Keep everything age-appropriate and encouraging.
- Write at about a 6-year-old's reading level. Short sentences.
- Use fun film-set vocabulary (director, scene, action!) when it fits.
- Never ask for or mention children's names or personal details.
  If any appear, gently remind staff: "describe the story, not the kids."
- Plain text only. Never use markdown symbols like ** or # — they show up
  as ugly stars on screen.
- When the story feels complete (hero, place, problem, solution, and ending
  are all decided), retell the full story in a short summary, congratulate
  the director, and end your message with this exact text on its own line:
  [STORY READY]
  Don't use that marker before the story is truly complete.
"""

# ---- Step cards (SPEC.md phase 3) ----
# When staff presses "Make step cards", we ask Claude for the story broken
# into filming steps — each with what to say to the kids, PLUS how to set
# up the camera, lights, and microphone for that scene.
CARD_INSTRUCTIONS = """You are the step-card maker inside the MSA Script Builder,
used at Märchen Sagen Academy where kids ages 4-10 film short movies with staff
(green screen and stop-motion, small indoor studio).

You will get a brainstorm conversation about a story. Turn the story into
5-8 step cards that walk kids and staff through FILMING it, scene by scene.

Structure the cards like the PUMA from Dan Roam's book "Show and Tell"
(head, spine, legs, tail):
- HEAD = the FIRST card: the movie's big question or idea, filmed as the
  opening title shot (example: "Can a clumsy robot find a way to play?").
- SPINE = the middle cards: one scene per card, in story order, each moving
  the hero one step through the struggle.
- LEGS = the setup tips on every card (camera, lights, sound, edit): the
  concrete details that hold that scene up.
- TAIL = the LAST card: the ending shot PLUS the one feeling or message the
  audience should take home from this movie.

For every card give:
- emoji: one fun emoji for the step
- title: a short exciting title (5 words max)
- say: what the staff member reads out loud to the kids. Fun, encouraging,
  reading level about age 6, film-set vocabulary. 1-3 short sentences.
- camera: one short, concrete tip for setting up the camera shot for this
  scene (angle, distance, still or moving). Written for a non-expert adult.
- lights: one short, concrete lighting tip for this scene (bright/dim,
  where to point the lamp, mood).
- sound: one short, concrete microphone/sound tip for this scene (who talks,
  where the mic goes, sound effects the kids can make).
- edit: one short CapCut editing tip for this scene: which sound effect or
  music to add and EXACTLY how to do it in CapCut, step by step. Example:
  "Add a crowd cheer: tap Audio, then Sounds, search 'crowd cheer', tap +
  to drop it on this clip." Written for a total beginner.

Plain text everywhere - no markdown symbols. Never mention children's names."""

CARD_SCHEMA = {
    "type": "object",
    "properties": {
        "cards": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "emoji": {"type": "string"},
                    "title": {"type": "string"},
                    "say": {"type": "string"},
                    "camera": {"type": "string"},
                    "lights": {"type": "string"},
                    "sound": {"type": "string"},
                    "edit": {"type": "string"},
                },
                "required": ["emoji", "title", "say", "camera", "lights", "sound", "edit"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["cards"],
    "additionalProperties": False,
}

# Pretend cards for free practice mode
PRACTICE_CARDS = [
    {
        "emoji": "🎬",
        "title": "Build the set",
        "say": "First we build the place where our story happens! You have ten minutes — build fast like a real movie crew!",
        "camera": "Put the camera on the tripod, facing the set, about two big steps back.",
        "lights": "Turn on the big lamp and point it at the set from the side.",
        "sound": "No microphone yet — this is building time. Play fun music!",
        "edit": "In CapCut: tap Audio, then Sounds, search 'upbeat', and tap + to add fun building music.",
    },
    {
        "emoji": "🎥",
        "title": "Film the first scene",
        "say": "Places, everyone! Our hero enters the scene. Ready... ACTION!",
        "camera": "Keep the camera still. Make sure the whole set fits in the picture.",
        "lights": "Keep the light steady so the picture doesn't flicker.",
        "sound": "Point the microphone at whoever is talking. Everyone else stays quiet!",
        "edit": "In CapCut: tap Audio, then Sound FX, search 'whoosh', and tap + to add it when the hero enters.",
    },
]


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


def ask_claude_for_cards(history):
    """Send the brainstorm to Claude and get back step cards (as a list)."""
    client = anthropic.Anthropic(api_key=read_api_key())
    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=16000,
        thinking={"type": "adaptive"},
        system=CARD_INSTRUCTIONS,
        messages=history + [{
            "role": "user",
            "content": "Now turn this story into step cards for filming.",
        }],
        # This guarantees Claude answers in exactly the card shape we need
        output_config={"format": {"type": "json_schema", "schema": CARD_SCHEMA}},
    )
    text = "".join(block.text for block in response.content if block.type == "text")
    return json.loads(text)["cards"]


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
        try:
            data = json.loads(self.rfile.read(length) or b"{}")
        except (ValueError, TypeError):
            data = {}
        if not isinstance(data, dict):
            data = {}

        wants_cards = data.get("want") == "cards"
        history = data.get("history") or []

        if read_api_key() is None:
            # No key yet -> free practice mode with pretend answers
            if wants_cards:
                reply = {"cards": PRACTICE_CARDS}
            else:
                reply = {"text": practice_reply(history)}
        else:
            try:
                if wants_cards:
                    reply = {"cards": ask_claude_for_cards(history)}
                else:
                    reply = {"text": ask_claude(history)}
            except anthropic.AuthenticationError:
                reply = {"error": "The API key doesn't work. Check api_key.txt."}
            except anthropic.APIError as problem:
                reply = {"error": f"Claude had a problem: {problem.message}"}
            except Exception:
                reply = {"error": "Something went wrong on our side. Please try again."}

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
