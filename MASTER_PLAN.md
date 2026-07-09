# MASTER_PLAN.md — LIVING DOCUMENT (update after every session)

**Goal:** Submit a genuinely strong Claude Corps application before July 17, 2026.
**Reality check:** Monday July 6 → Friday July 17 = **11 days**. At 20–35 hrs/week
that is roughly 45–70 working hours TOTAL. The plan below is sized to that truth.
Submitting July 15–16 (not the deadline day) is the target.

## How to use this file
- Claude: read this at the start of every chat. When status changes, output the
  full updated file so Luca can replace it in project knowledge and commit to GitHub.
- One rule: if a task doesn't serve a REQUIREMENTS.md item, it doesn't happen
  before July 17.

## STATUS BOARD (update these lines only — keep it scannable)
| Item                          | Status      | Notes |
|-------------------------------|-------------|-------|
| AI Fluency course             | ✅ DONE     | completed July 4 — save proof of completion for the certificate doc |
| Claude 101 course             | NOT STARTED |       |
| Certificates combined (1 doc) | NOT STARTED |       |
| GitHub account + repo         | ✅ DONE     | public repo: github.com/lucadewinne-bit/msa-director-project |
| Phase 1: research + spec      | ✅ DONE     | SPEC.md written and committed — the source of truth |
| Staff discovery conversation  | NOT STARTED | ask staff for 15 min EARLY this week |
| Phase 2: build V1             | IN PROGRESS | walking skeleton LIVE end-to-end: page → server → real Claude → answer on screen. Next: brainstorm → script → publish flow |
| Test with kids/staff at MSA   | NOT STARTED | schedule the session by Day 3 |
| Staff runbook (1 page)        | NOT STARTED |       |
| Essay 1: community impact     | NOT STARTED |       |
| Essay 2: setback/learning     | NOT STARTED |       |
| Resume polished               | NOT STARTED |       |
| LinkedIn polished             | NOT STARTED |       |
| Final review + SUBMIT         | NOT STARTED | target July 15–16 |

## PHASE MAP (11 days)

### Days 1–3 (Mon Jul 6 – Wed Jul 8): Foundations — course + scoping in parallel
- HEAD START: AI Fluency already completed (July 4) — only Claude 101 remains.
- Day 1 morning: create GitHub account + repo `msa-director-project` (name TBD by
  spec). Commit these .md files. Start Claude 101.
- Day 1–2: finish Claude 101. Course time is also learning time for the project —
  connect what he learns to the build. Use the freed-up hours to go deeper on
  PHASE1_PROMPT.md Step 1 research.
- Day 2–3: run PHASE1_PROMPT.md Steps 1–3 (research, JTBD, options) in parallel
  with the course. Ask MSA staff for the 15-minute discovery conversation NOW and
  book the informal kid/staff test session for ~Day 8–9.
- Day 3: combine both certificates into one document. Phase 1
  Steps 4–5: decide + write SPEC.md. **Spec locked end of Day 3.**

### Days 4–8 (Thu Jul 9 – Mon Jul 13): Build V1
- Day 4 morning: TWO parallel throwaway skeletons of the riskiest interaction,
  90 minutes each, hard stop. Pick one by lunch (log why in DECISIONS.md).
  Afternoon: turn the winner into the walking skeleton — simplest end-to-end
  version that technically works (front-end → Claude API → output), however ugly.
- Day 5: build to spec in small milestones. Each milestone = a commit with a
  plain-language message. Log every real decision in DECISIONS.md.
- Days 6–7: **the last-20% days.** No new features — edge cases, error handling,
  and integration only (what happens when the API fails, the input is empty, a
  kid taps twice, the wifi drops). The whitepaper rule: this 20% takes as long
  as the first 80%; budgeting for it is what separates shipped from almost.
- Day 7: set up the staff feedback workflow (form → sheet). Draft the 1-page
  runbook. Evening: **Essay 1 first draft** (community impact) while build energy
  is high — do not leave both essays to Day 10.
- Day 8: freeze features. Triage by "bad vs. sad": FIX what is broken (bad);
  SHIP what is merely disappointing (sad). Dad's engineers do a review pass
  (advice only). Prepare the 60-second demo. Run the TEST_CHECKLIST end to end.

### Days 9–10 (Tue Jul 14 – Wed Jul 15): Test, essays, polish
- Day 9: informal test at MSA — staff member runs it, kids use it alongside staff.
  Collect feedback via the form. Fix only what's broken, not what's imperfect.
- Day 9–10: essays. Interview-style drafting with Claude from ESSAY_MATERIAL.md —
  Luca talks (voice memos welcome), Claude structures, keeps his voice, handles
  spelling/grammar. Polish resume + LinkedIn the same way.
- Day 10: repo README final pass — the story, links to MSA videos (then vs now),
  spec, decisions, "what I'd do differently."

### Day 11 (Thu Jul 16): Submit
- Run the pre-submission checklist in REQUIREMENTS.md top to bottom.
- Dad does a second-pair-of-eyes pass. Submit. Celebrate properly.

## DAILY OPERATING SYSTEM (this is how the plan survives ADHD)
- **Fixed daily kickoff:** 15 minutes with Dad, same time every day. Its only job
  is to open the Claude Project chat. Once the chat is open, momentum exists.
- In-chat: Claude asks "what got done / how much time now?" → gives ONE next action.
- End of each session: Claude updates the STATUS BOARD; Luca commits to GitHub
  with a one-sentence plain-language explanation of what changed (teach-back rule).
- **STUCK PROTOCOL (the most important rule in this file).** When something won't
  work: after ~4 failed attempts OR ~30 minutes — STOP. Do not thrash. In order:
  (1) revert to the last working commit; (2) open a FRESH chat and describe the
  problem from scratch in plain words; (3) if still stuck, change the approach
  entirely, or park it and take the next milestone; (4) only after all that, ask
  Dad or an engineer. Never push past 45 minutes without changing something.
  Getting stuck is normal; thrashing is the only real enemy.
- Falling behind a day is normal. The recovery move is always the same: shrink
  scope (consult the CUT LIST below and VISION.md's parking lot), never extend
  the date.

## TRIPWIRES & CUT LIST (decide cuts now, calmly — not later, in a panic)
- Tripwire Day 2: AI Fluency not finished → compress Phase 1: skip the full
  options matrix, adopt the lead concept with a one-paragraph justification.
- Tripwire Day 3: MSA test session not booked → fallback: remote test with one
  staff member, or one known child with a parent present; describe honestly.
- Tripwire Day 5: no end-to-end walking skeleton → execute cuts, in this order:
  dashboard → feedback workflow → visual polish → reduce to the single core
  interaction. Cutting checkboxes hurts far less than missing the date.

## PARKING LOT (things deliberately NOT before July 17)
- Everything in VISION.md (open-source platform).
- Dashboard/visualization of feedback — only if Days 9–10 have slack.
- Polish beyond "a staff member can use it without Luca in the room."
