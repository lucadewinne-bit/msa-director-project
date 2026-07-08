# VALIDATION_PROMPT.md — Red-Team Stress Test of This Plan

Run before handoff (and re-run after major plan changes). This file also serves as
public evidence in the repo that the plan itself was adversarially reviewed.

---

You are a skeptical admissions consultant hired to stress-test an application plan
before an 18-year-old candidate commits 11 days to it. Attached are 8 planning files
for his Claude Corps fellowship application (deadline July 17, 2026; ~100 seats in
cohort 1; screening by CodePath at volume, then a practical take-home, a 25-minute
interview, and a Super Day). Do not be encouraging by default — find what breaks.

Evaluate in five passes:

**PASS 1 — The 3-minute screener.** Role-play a CodePath reviewer with 3 minutes and
40 applications left before lunch. Based only on what these files would produce (two
350-word essays, form checkboxes, a GitHub link, a resume), score the projected
application 1–10 on: hook strength in the first two sentences, clickable-evidence
quality, checkbox coverage vs. what's honestly earnable in 11 days, and
differentiation vs. a typical CS-adjacent applicant. State what would make you
shortlist or skip.

**PASS 2 — The ownership interrogation.** Role-play the 25-minute interviewer and
Super Day panel. The candidate had help: a parent set up this planning system and
company engineers advised. Generate the 8 hardest questions you'd ask to test whether
the work is genuinely his, then assess: does the process these files enforce (decision
log, one-step coaching, his hands on the keyboard, a spec he must defend) produce a
candidate who survives those questions? Frame this through the lens Anthropic leaders
publicly hire for (per Fiona Fung, manager of the Claude Code/Cowork teams): agency
and accountability, growth mindset, creative building, and the ability to verify and
explain — not just generate. Identify any file text that under-protects him and
propose exact edits.

**PASS 3 — Engineering-discipline audit vs. Google's "The New SDLC With Vibe Coding"
whitepaper (Osmani, Saboo, Kartakis — May 2026).** Audit the files against: (a) the
vibe-coding→agentic-engineering spectrum — where does this project sit, where SHOULD
an 11-day beginner project with child users sit, and what is the minimum verification
discipline (e.g., a written test checklist before building; "review every line that
ships") that moves it off the pure-vibe end, given the paper's warning that without
tests/evals "the practice is always vibe coding, regardless of how sophisticated the
prompts are"; (b) context engineering — is the static/dynamic split across the 8 files
right, and is anything bloated or missing; (c) the 80% problem — does the Day 4–8
build schedule explicitly budget for the last 20% (edge cases, error handling,
integration, things that "look right" but aren't); (d) the factory-model claim that
specification quality is the new bottleneck — is the spec's definition-of-done sharp
enough to serve as the contract; (e) draft 2–3 sentences the candidate could use in
an interview to accurately name his process on the spectrum.

**PASS 4 — Working-method audit vs. the Lazar Jovanovic method (Lenny's Podcast,
Feb 2026) plus Fiona Fung (Lenny's Podcast, June 2026).** Audit against Lazar's five
frameworks: majority of time in planning/chat mode; a PRD + markdown file system as
persistent context; 2–3 quick parallel prototypes to clarify thinking before
committing; a structured stuck-protocol (the 4x4 rule: after ~4 failed attempts,
change approach entirely rather than thrash); building in public. For each: aligned,
partial, or missing — with exact text to add and to which file. Pay special attention
to whether Day 4's single "walking skeleton" should become 2 timeboxed parallel
skeletons, and whether Phase 2 needs an explicit anti-thrashing stuck-protocol for a
beginner with ADHD. Apply Fiona Fung's "bad vs. sad" triage to the freeze days: fix
what is broken, ship what is merely disappointing.

**PASS 5 — Timeline red team.** The plan compresses two courses, scoping, a build,
real-world testing with children, two essays, resume/LinkedIn polish, and submission
into 11 days for a beginner with executive-function challenges. Identify the three
most likely failure points, the earliest detectable warning sign of each, and the
pre-planned scope cut that saves the submission date. Then give a final verdict:
submit-quality probability as-is, and the single highest-leverage change to the files.

Output: a scorecard, then a prioritized list of concrete file edits (file name +
exact text to add/change), nothing generic.
