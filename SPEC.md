# SPEC.md — MSA Script Builder (V1)

**Status: LIVING DOCUMENT.** This spec can change as the build teaches us things.
Every change gets a DECISIONS.md entry. The spec serves the build, not the other way around.

---

## The problem

Kids ages 4–10 at Märchen Sagen Academy have big story ideas but can't structure
them alone — that's executive functioning, and it's the hardest part. The gap
isn't filming (MSA is great at that). The gap is getting from "vague idea in a
kid's head" to "locked script ready to shoot." Kids drift, freeze, or stall in
that gap. MSA's rule — no green screen or stop-motion until the story is locked —
makes this THE bottleneck of every production.

## Who it's for

- **Kids (4–10):** the storytellers. They see questions and scripts on screen
  (read aloud), they decide everything — but they never chat with the AI directly.
- **Staff:** the translator. Staff types into the tool, reads Claude's questions
  to the kids, types the kids' answers back, and curates the final step cards.
  The app is always used by a staff member together with the kids — always
  supervised, never by a child alone.
- **The AI (Claude):** the co-writer. Asks questions, drafts, revises. Never
  talks to a child directly, never sees a child's name.

## The four-phase model (the tool covers 1–3)

1. **💡 Brainstorm** — kid pitches a vague idea; staff and Claude riff in an
   OPEN conversation (no fixed number of questions, no fixed branches) until
   the story feels solid.
2. **📝 Script** — Claude writes the full kid-friendly screenplay from the
   brainstorm. Staff can ask for any change, any number of times, in
   conversation. When it's right: **PUBLISH** (the script locks).
3. **🗂️ Step cards** — Claude breaks the published script into visual,
   audio-narrated step cards. Staff CURATES: keep, skip, simplify, or add
   cards. Only the curated set goes to the kids.
4. **🎥 Film** — happens in the real studio with MSA's existing cameras and
   workflow. **The app never records, stores, or uploads any video or audio
   of children. Ever. This is permanent, not just out-of-scope for V1.**

## What V1 does

- One web app, staff-operated, used on a laptop/tablet in the room with kids.
- Open chat with Claude for Brainstorm and Script phases (staff types).
- Kid-facing display mode: big text, emoji, 🔊 read-aloud (browser speech),
  minimal reading — dyslexia- and pre-reader-friendly.
- PUBLISH button that locks the script.
- Step-card generation from the published script, with staff curation
  (keep / skip / edit per card).
- Kid-facing step-card mode for the studio: one card at a time, first/then,
  optional visual timers, nameless role slots (tap to claim, no names).
- A welcome / context view on the home screen (added after first user testing):
  in plain language, what the Script Builder is, who it's for (staff and kids
  together, always supervised), and the whole path — Brainstorm → Script →
  Step cards → Film in the studio. Skippable and returnable, so it helps
  first-timers without slowing people who already know the tool.
- A journey indicator shown while working: the three in-app steps
  (Brainstorm → Script → Cards, all required before filming) with a clear
  marker of where you are right now, and "🎥 Film in the studio" as the
  off-app finish line.
- A "?" help button: a simple question-and-answer guide, split into questions
  for staff (how to start, change the script, help a stuck kid, what's saved
  about children) and questions for kids (short and 🔊 read-aloud: what are we
  making, what happens next, whose turn is it).

## What V1 deliberately does NOT do (see VISION.md for the future)

- No recording, playback, or upload of any media.
- No child accounts, logins, names, or stored conversations about specific kids.
- No parent-facing views.
- No multi-organization features.
- No saving libraries of past scripts (nice-to-have; only if the build goes fast —
  and if added, scripts must contain zero child-identifying info).

## Safety rules (non-negotiable)

1. Staff-mediated only: Claude ↔ staff ↔ kids. No direct child–AI chat.
2. Zero child data: no names, no photos, no video, no audio, no accounts.
   The UI reminds staff: "describe the story, not the kids."
3. Kid-facing content rules baked into every prompt: age-appropriate,
   encouraging, reading level ~age 6, film-set vocabulary for fun.
4. Used with staff present. The runbook states this.

## Success criteria

- One staff member runs a full brainstorm → script → publish → step cards
  session **without Luca in the room**, using only the 1-page runbook.
- Kids follow the curated step cards through a real studio session.
- A production goes from vague pitch to published script in one sitting.
- Demoable in 60 seconds: type a pitch → riff twice → publish → show a card.

## Tech shape (plain language)

- **Front end:** one simple web page (HTML/CSS/JS or a small React app).
  Two display modes: staff mode (chat + curation) and kid mode (big cards).
- **Brain:** Claude API. Three prompt jobs: (1) brainstorm partner,
  (2) screenplay writer, (3) script → step-card converter (returns JSON the
  page can render).
- **State:** lives in the page while the session runs. Nothing about children
  is stored anywhere.
- **Feedback loop:** simple staff feedback form → spreadsheet (the
  two-tools workflow requirement).

## Build sequence (small milestones, in order — no dates, just steps)

1. **Walking skeleton:** one page, one input, one live Claude call, response
   on screen. Proves the plumbing.
2. Brainstorm chat: messages stack, conversation carries history.
3. Script phase: "write the script" button → screenplay renders kid-readable.
4. PUBLISH: locks the script, moves to card generation.
5. Step cards: Claude returns JSON cards → staff curation screen (keep/skip/edit).
6. Kid mode: big card view with read-aloud, timers, role slots.
7. Runbook (1 page) + staff feedback form.
8. Freeze. Bug-fix only. Prepare the 60-second demo.

Riskiest assumption: **Claude can reliably turn a messy brainstorm into a
script and cards that staff finds usable with minimal editing.** The walking
skeleton plus milestone 5 test exactly this, earliest possible.

## Where this fits the application

Discover → build → enable → leave it running: staff conversation shaped the
concept, Luca builds it, the runbook enables MSA, and the tool keeps working
after handoff. Built by someone who was one of these kids — the tool he
wishes he'd had.
