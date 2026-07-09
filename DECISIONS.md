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
