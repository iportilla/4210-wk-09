# Startup idea — Loopback
**Category:** AI / SaaS · B2B
**Stage:** Concept
**Date:** March 2026

---

## One-liner

Loopback is an AI meeting intelligence platform that turns recurring internal meetings into a living knowledge base — automatically surfacing past decisions, unresolved blockers, and context drift before every call.

---

## The problem

Teams have too many meetings and remember too little of what was decided in them. The average knowledge worker spends 21 hours per week in meetings. Less than 30% of decisions made in those meetings are documented anywhere retrievable. The result: the same conversations happen repeatedly, onboarding takes longer than it should, and institutional knowledge lives in the heads of the people who've been around longest.

Existing tools — Notion, Confluence, Otter.ai — solve pieces of this. Notion and Confluence require humans to write things down. Otter transcribes but doesn't synthesise or connect. Nothing closes the loop between what was said, what was decided, and what comes up again next week.

---

## The solution

Loopback connects to your calendar, Zoom/Meet/Teams, and your existing docs. It:

1. **Transcribes and summarises** every meeting automatically — decisions, action items, open questions, risks flagged.
2. **Builds a decision graph** — a structured, searchable record of what was decided, by whom, and when, linked to the meeting where it happened.
3. **Prepares a pre-meeting brief** — before any recurring meeting, Loopback surfaces: what was decided last time, which action items are still open, and any new context from your docs or Slack that's relevant.
4. **Detects drift** — when a new discussion contradicts a prior decision, Loopback flags it in real time ("In your March 3 planning session, the team agreed not to pursue paid acquisition in Q2").

The core insight: the value isn't in the transcript. It's in the connection between meetings over time.

---

## Market

**Primary target:** Engineering, product, and operations teams at Series A–C SaaS companies (50–500 employees).

**Why this segment:**
- High meeting frequency, high decision velocity
- Already paying for Notion, Linear, Slack — accustomed to workflow tooling
- Pain is acute and felt by both ICs and managers

**Market size:**
- ~180,000 SaaS companies globally with 50–500 employees
- Assuming $300 ACV per seat, 10 seats average per account → $540M serviceable addressable market at 10% penetration
- Adjacent expansion into enterprise (legal, consulting, financial services) adds a further ~$2B TAM

---

## Business model

- **Per-seat SaaS:** $25/user/month (billed annually)
- **Team plan:** $199/month for up to 10 seats — designed for early adoption
- **Enterprise:** Custom pricing, SSO, data residency, admin controls

Estimated payback period at current CAC benchmarks: 7–9 months.

---

## Differentiation

| | Loopback | Otter.ai | Notion AI | Fireflies |
|---|---|---|---|---|
| Auto-transcription | ✓ | ✓ | ✗ | ✓ |
| Decision graph | ✓ | ✗ | ✗ | ✗ |
| Pre-meeting brief | ✓ | ✗ | ✗ | ✗ |
| Drift detection | ✓ | ✗ | ✗ | ✗ |
| Cross-meeting memory | ✓ | ✗ | Partial | ✗ |

The moat is longitudinal memory. The longer a team uses Loopback, the more valuable the decision graph becomes — a classic data network effect that compounds with time.

---

## Risks & open questions

- **Privacy concern:** Meeting recording is sensitive. Will need granular controls, clear data handling policies, and likely SOC 2 Type II before enterprise sales.
- **Calendar / conferencing integrations:** Dependent on API access from Zoom, Google, Microsoft. Platform risk if these are restricted.
- **Adoption flywheel:** Value increases with team-wide adoption. Individual sign-up may not be enough — need a champion-led or admin-led motion.
- **Open question:** Is the pre-meeting brief the right wedge, or is search ("what did we decide about X?") a more natural entry point?

---

## Why now

- LLMs have made high-quality meeting summarisation cheap and accurate enough to be production-grade.
- Remote and hybrid work has dramatically increased meeting load while reducing informal knowledge transfer.
- Teams are actively looking to reduce meeting time — Loopback makes that possible without losing the institutional knowledge that meetings currently carry.

---

## Next steps (if pursuing)

- [ ] Validate decision graph concept with 10 potential users (PMs, engineering leads)
- [ ] Build a no-code prototype using Whisper + GPT-4o + Notion API
- [ ] Define the minimum lovable product: pre-meeting brief only, no real-time features
- [ ] Identify 3–5 pilot companies willing to trial for 90 days

---

*Internal concept document. Not for distribution.*
