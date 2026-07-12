# DECISIONS.md — Decision Log (living document)

Every real decision gets an entry. This log is: (1) the honest record behind
"what would you do differently," (2) essay raw material, (3) interview prep,
(4) public proof in the GitHub repo that the process was spec-driven and mine.

Keep entries short. Plain language. Written so Luca can read one aloud in an
interview and sound exactly like himself.

---

## Entry template
**#N — [short title]** · [date]
- **Decision:** what we chose.
- **Options considered:** what else was on the table.
- **Why:** the reasoning, in 2–3 sentences.
- **What would change my mind:** the assumption this rests on.
- **Outcome (fill in later):** what actually happened.

---

**#0 — Spec-driven approach with an 11-day runway** · 2026-07-04
- **Decision:** Run the project as research → JTBD → options → decision → spec →
  build, with all state in versioned markdown files (Claude Project + GitHub),
  not in any single conversation.
- **Options considered:** Jump straight into building something; keep everything
  in one long chat thread.
- **Why:** The application explicitly rewards scoping, honest reasoning, and
  "what you'd do differently" — the process is the portfolio. And with ADHD/EF
  challenges, external files beat working memory every time.
- **What would change my mind:** If by end of Day 3 the spec isn't locked,
  process gets cut before scope does.
- **Outcome:** _pending_

---

**#1 — Voice-first reframe: amplify authorship, not compliance** · 2026-07-04
- **Decision:** The project's purpose is reframed from "help kids follow
  production steps" to "shorten the distance between a child's imagination and
  their finished story." Every concept is now also scored on authorship/voice
  fit, and the north star + design test ("does this give the child MORE
  authorship?") were added to CONTEXT.md and REQUIREMENTS.md.
- **Options considered:** Keep the pure step-chunker framing (strongest ADHD
  evidence, easiest build, but ethos-neutral — it optimizes compliance with a
  process rather than serving MSA's mission of self-expression and each child
  finding their own voice).
- **Why:** MSA's mission is emotional and creative growth through storytelling;
  Anthropic's is AI serving humanity's long-term well-being. The aligned move is
  AI carrying the mechanical load so kids keep the human part. Also honest:
  the EF science (point of performance, chunking, visual schedules) still fully
  applies — the reframe changes what the tool is FOR, not what makes it work.
- **What would change my mind:** If Phase 1 discovery with MSA staff shows the
  voice-first concepts are too heavy for a 5-day build, fall back to the
  storyboard-only slice or the plain chunker — explicitly permitted in Step 4.
- **Outcome:** _pending_

---

**#2 — Step cards include camera, lights, and sound setup** · 2026-07-08
- **Decision:** Every step card shows not just what to say to the kids, but
  three short setup tips: 🎥 camera, 💡 lights, 🎤 sound — written for a
  non-expert adult.
- **Options considered:** Plain scene descriptions (what Claude gave first);
  story-only cards leaving production details to staff experience.
- **Why:** I tested the brainstorm myself and realized the scene list didn't
  actually help anyone FILM anything. The gap the tool fills is getting from
  story to studio — so each card has to answer "how do we set this shot up?"
  for a staff member who isn't a filmmaker.
- **What would change my mind:** If MSA staff testing shows the setup tips are
  ignored or too generic, simplify back to story-only cards.
- **Outcome:** _pending_ — test with staff at MSA

---

**#3 — Added saving step cards + a home page** · 2026-07-08
- **Decision:** Step cards can be saved with a movie name and reopened from a
  home page. Saved on that computer's browser only — no accounts, no cloud.
- **Options considered:** Keep V1 with nothing saved (what the spec planned);
  save to a server (rejected: adds accounts and privacy risk for zero V1 gain).
- **Why:** The spec parked "saving libraries of past scripts" as a nice-to-have
  IF the build went fast — and it did. Staff need this in practice: a filming
  session spans days, and losing the cards between sessions would make the tool
  annoying. The spec's condition is met: saved cards contain only the story,
  never anything about kids.
- **What would change my mind:** If saving confuses staff during testing, or
  anything child-identifying ever ends up in cards, remove it.
- **Outcome:** _pending_

---

**#4 — Adopted Dan Roam's "Show and Tell" as the storytelling backbone** · 2026-07-08
- **Decision:** The brainstorm partner follows Roam's three rules (tell the
  truth, tell it with a story, tell it with pictures). The card maker
  structures every card set like Roam's PUMA: head (big question as the
  opening title card), spine (one scene per card), legs (the camera/lights/
  sound/edit tips), tail (ending + the one feeling the audience takes home).
- **Options considered:** Keep the looser hero-problem-fix-ending structure;
  invent our own framework from scratch.
- **Why:** I know this book and its method works. It gives every movie a
  real backbone instead of just a list of scenes — and it fits MSA's mission:
  "tell the truth" IS voice-first storytelling. Copyright handled honestly:
  concepts in our own words, full credit in the README, none of the book's
  text or drawings copied.
- **What would change my mind:** If the PUMA-shaped cards confuse kids or
  staff in testing, drop back to the plain scene list.
- **Outcome:** _pending_

---

**#5 — Staff curation screen with a Stash (not a trash)** · 2026-07-09
- **Decision:** Cards no longer go straight to the kids. Staff first see a
  check screen: fix any words by typing on the card, and skip cards into a
  Stash — parked, never deleted, one tap brings them back. Only kept cards
  reach kid mode. A ✏️ on the kid screen returns to checking.
- **Options considered:** Cards straight to kids (what we had); a delete
  button instead of a stash.
- **Why:** Two reasons lined up. My SPEC always said staff curate cards
  before kids see them (safety rule: staff-mediated). And market research
  on proven tools showed the exact pattern that works: Arc Studio's "Stash"
  is loved because cutting never feels destructive, and Sudowrite's
  use-or-discard flow keeps the human in charge of the AI. Evidence and
  spec agreed, so this jumped the queue.
- **What would change my mind:** If staff skip the checking step in real
  sessions, make it faster or optional.
- **Outcome:** _pending_ — watch staff use it at MSA

---

**#6 — Put the app online with a serverless "middleman"** · 2026-07-12
- **Decision:** Deploy the tool to a public link on Vercel's free tier. A
  small serverless function (`api/chat.py`) sits between the web page and
  Claude and holds the API key. The key lives ONLY in a Vercel setting
  (environment variable) — never in the code, never in GitHub. No accounts
  and no login: anyone with the link can use it, on a desktop browser.
- **Options considered:** Keep it Mac-only (the local `server.py`, which only
  runs on my laptop); put the key straight in the web page (rejected — anyone
  could read it and run up my bill); a paid host.
- **Why:** Reviewers and MSA staff need to open the tool from any computer
  without installing anything. The middleman is what makes "public" safe: the
  page never sees the secret key, it just asks the middleman, and the
  middleman talks to Claude.
- **What would change my mind:** If a public, no-login link gets abused or
  runs up surprise cost, add a simple gate or a spending cap; if the free
  tier's limits get in the way, revisit the host.
- **Outcome:** Live at https://msa-director-project.vercel.app — brainstorm
  chat and step-card generation both tested working from outside. Two lessons
  worth keeping: (1) Vercel's Python system wanted ONE "app" file, so the
  middleman serves both the page and Claude, like the old local server did.
  (2) The first key I pasted into Vercel went in twice with a line break,
  which quietly broke every request; the fix was re-pasting it as a single
  clean line, plus code that now ignores stray line breaks. That key was
  briefly exposed by a debug message during setup, so I deleted it and made
  a fresh one.

---

**#7 — Onboarding, journey map, and help — from first user testing** · 2026-07-12
- **Decision:** After the first testing session (tested with my siblings), add
  three front-end-only features: (1) a welcome / context view that explains what
  the tool is, who it's for (staff + kids, always supervised), and the full path;
  (2) a journey indicator showing the three in-app steps (Brainstorm → Script →
  Cards) and where you are, with filming as the off-app finish; (3) a "?" help
  panel with plain Q&A for staff and simple read-aloud Q&A for kids.
- **Options considered:** Leave the app as-is (but testers couldn't tell what it
  was for or where they were); a written runbook only (doesn't help mid-session);
  a full guided tour / coach-marks (heavier to build, and easy to get in the way).
- **Why:** Real first-time users couldn't tell what the app was, the order of the
  steps, or where they were in it — three faces of the same gap: context and
  wayfinding. These are cheap, static additions (no new Claude calls, no child
  data) that answer the feedback directly without touching the parts that work.
- **What would change my mind:** If the welcome view or help panel gets in the way
  of staff who already know the tool, make them more skippable or off by default.
- **Outcome:** _pending_ — re-test with the same people.

---

**#8 — Separate internal working docs from the public repo** · 2026-07-12
- **Decision:** Before sharing the repo with outside engineers, keep the public repo
  focused on the product and the spec-driven process (SPEC, DECISIONS, MASTER_PLAN,
  REQUIREMENTS, VISION, and the code). Move the internal working docs out: the
  personal briefing, the essay-prep notes and drafts, and the private project-setup
  handoff. Also scrubbed a few personal references (names/accountability routine)
  out of MASTER_PLAN.
- **Options considered:** Share everything as-is; rewrite git history to erase the
  removed files from all past commits.
- **Why:** A public repo read by reviewers, engineers, and product folks should show
  the work and the thinking — not personal details or the meta-strategy behind the
  written answers. The origin story that matters (a dyslexic kid who came back to
  build the tool he wishes he'd had) still lives in the README and Essay 1.
- **What would change my mind:** If deeper privacy is ever needed, rewrite history to
  remove the files entirely; for now the repo was already public, so we removed them
  going forward.
- **Outcome:** _done_ — repo trimmed to the product + process; internal docs kept
  privately.
