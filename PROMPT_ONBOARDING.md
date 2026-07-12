# PROMPT_ONBOARDING.md — engineer prompt for the onboarding / journey / help work

This is the reusable prompt that drove the first round of changes after user
testing (tested with Luca's siblings). It addresses three pieces of feedback:
(1) no page explaining what the app is, (2) no sense of the overall journey /
where you are, (3) no simple help. Paste the block below into a fresh Claude
Code session opened in this project folder to run it again or continue it.

---

You are an expert front-end engineer working in the MSA Script Builder repo — a
single self-contained web app. Work spec-first and in small steps. The owner,
Luca, is a non-coder with dyslexia/ADHD: explain in plain language, keep messages
short, do ONE step at a time, and never push to `main` or take any outward action
without his explicit OK. If a product choice is unclear, ask him — don't guess.

## 0. Read before you touch anything
Read these fully, then give me a 3-line summary of what the app is and how the
code is organized:
- SPEC.md (the source of truth), DECISIONS.md, CONTEXT.md, REQUIREMENTS.md, README.md
- app/index.html (the ENTIRE app — one file, inline CSS/JS)
- api/chat.py (the Vercel middleman) and app/server.py (the local dev server)

Facts about the current app (verify against the code):
- One page, staff-operated. Screens live in app/index.html and toggle by id/class:
  a header with a 🏠 Home button; a home screen ("Start a new movie" / "Your
  movies"); a brainstorm chat; a "Step cards 🗂️" button that unlocks when the
  story is ready; a curation / "Check the cards" screen (#curateMode); and a
  full-screen kid card mode (#cardMode). There's a staff-reminder banner.
- Design system: the "anthropic.com" aesthetic already in the file — warm cream
  paper, ink text. Accessibility matters: big text, emoji, 🔊 read-aloud (browser
  speech), minimal reading (dyslexia- and pre-reader-friendly).
- Deployment: pushing to `main` auto-deploys to production at
  https://msa-director-project.vercel.app. Pushing any OTHER branch makes a
  private Vercel PREVIEW deploy (only Luca, logged in, can see it). api/chat.py
  serves app/index.html, so front-end edits ship automatically — do NOT touch
  api/chat.py.
- Safety rules (non-negotiable): staff-mediated only (kids never chat with the AI),
  zero child data (no names/photos/audio/video/accounts), reading level ~age 6,
  used with staff present.

## The persona (make this explicit in the product)
The user is a STAFF MEMBER at Märchen Sagen Academy using the app TOGETHER WITH
kids aged 4–10, ALWAYS SUPERVISED. Staff types and reads aloud; kids decide the
story but never touch the AI directly.

## 1. The job — address 3 pieces of real testing feedback
FRONT-END-ONLY additions: no new Claude/API calls, no backend change, no child
data. Do NOT redesign existing screens; add to them in the existing style.

Feature A — A context / landing view. New users don't know what the app is. Add a
clear welcome view that explains, in plain language: what the Script Builder is,
who it's for (staff + kids, always supervised), and the whole flow —
1) Brainstorm the story together → 2) Build & edit the script with staff →
3) Make the step cards → then 4) Film in the studio. Integrate it sensibly with
the existing home screen (no jarring extra gate). Make it skippable and returnable.

Feature B — A journey progress indicator. Show the overall meta-steps and WHERE
YOU ARE right now: Brainstorm → Script → Cards (the 3 steps this app covers, all
required before filming), then a clear "🎥 Film in the studio" as the off-app
finish. It must update as the user moves through phases and read clearly for a
non-technical adult.

Feature C — A simple Help icon. Add a small "?" button (e.g. next to the 🏠 in the
header) that opens a simple Q&A guide, split into two groups:
- For staff/supervisor: e.g. "How do I start?", "How do I change the script?",
  "What if a kid gets stuck?", "Is anything about the kids saved?"
- For kids (short, 🔊 read-aloud friendly): e.g. "What are we making?",
  "What happens next?", "Whose turn is it?"
Keep answers short and in the app's warm voice.

## 2. Process — spec-first, small steps, branch only
1. Create a new git branch (e.g. `feature/onboarding-journey-help`). Do NOT
   commit to `main`.
2. FIRST update SPEC.md: fold these 3 features and the persona clarification into
   the right sections, in SPEC's existing plain voice. Show me the SPEC changes
   and PAUSE for my approval before writing any app code.
3. Add a DECISIONS.md entry (the repo logs every real decision — follow the
   existing template).
4. Implement in app/index.html, ONE feature at a time. Before each, tell me in one
   or two plain sentences what you're about to do. Keep everything self-contained
   (inline CSS/JS, no new libraries). Don't break any existing feature.
5. Test locally and tell me exactly what you checked: run `python3 app/server.py`,
   open http://localhost:8000 (it runs in free "practice mode" with no API key —
   perfect for checking new UI without spending money). Verify the landing view,
   the journey indicator updating across phases, and the help panel — and confirm
   brainstorm → cards → curation → kid mode all still work.
6. Commit to the branch and push the BRANCH (this makes a Vercel preview). Give me
   the preview link. Do NOT merge to `main`.
7. Only when I say it looks good, merge the branch into `main` (that deploys live).

## Definition of done
- SPEC.md and DECISIONS.md updated and committed on the branch.
- All three features work and match the existing look and accessibility.
- Every existing feature still works (brainstorm, publish, cards, stash/curate,
  kid mode, read-aloud, save/reopen).
- Nothing about children is collected or stored; staff-mediated model intact.
- Goes live only after my explicit approval to merge to main.
