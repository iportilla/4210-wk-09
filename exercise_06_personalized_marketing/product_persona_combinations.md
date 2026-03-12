# Product + persona combinations
**Document type:** Content strategy framework
**Product:** Loopback / Arclight AI
**Author:** Marketing & Product
**Date:** March 2026
**Status:** Working document

---

## Why persona × product combinations matter

Most product marketing treats the product as fixed and the persona as an audience to reach. A more useful frame is to treat each product × persona combination as its own value proposition — because the same product solves different problems for different people, in different language, with different proof points.

Loopback has one core capability: longitudinal meeting intelligence. But what that means to a VP of Engineering is different from what it means to a Chief of Staff, which is different again from what it means to an IT Administrator evaluating security. The feature set is the same. The value story, the objection set, and the language that lands are completely different.

Mapping these combinations explicitly produces three things: sharper messaging, better sales qualification, and clearer product prioritisation.

---

## The products

### Loopback (core platform)
AI meeting intelligence that builds a decision graph across recurring meetings — automatically capturing what was decided, flagging when new discussions contradict prior decisions, and surfacing context before every call.

**Core jobs to be done:**
- Preserve institutional knowledge across personnel changes
- Reduce time wasted relitigating past decisions
- Accelerate onboarding for new team members
- Give leaders visibility into how decisions are being made below them

### Loopback Smart Handoff (feature)
One-click generation of a contextual project handoff document, synthesised from meeting history, connected docs, and open action items.

**Core jobs to be done:**
- Transfer project ownership without knowledge loss
- Reduce the cost of team transitions and departures
- Give incoming owners a reliable starting point, not a pile of Slack threads

### Arclight Nova Dashboard (platform)
AI-powered work context dashboard that connects to your tool stack and surfaces the state of work — decisions made, blockers live, progress against goals — without requiring manual reporting.

**Core jobs to be done:**
- Give leaders real-time visibility without status meetings
- Reduce the reporting burden on individual contributors
- Create a single source of truth across fragmented tools

---

## The personas

### Persona A — The Engineering Lead
**Role:** Engineering Manager or Director, 8–20 person team
**Goals:** Ship reliably, reduce interruptions, protect team focus, make good architectural decisions that age well
**Frustrations:** Decisions made without them that affect their team; context lost when engineers move between projects; too much time in meetings, not enough in code
**Relationship to the product:** Power user of the decision graph; values the pre-meeting brief for sprint planning and architecture reviews; cares about integrations with Linear and GitHub
**Buying role:** Champion — rarely the budget owner, but their endorsement is required

---

### Persona B — The Chief of Staff
**Role:** Chief of Staff or Senior Operations Lead, works directly with C-suite
**Goals:** Keep the leadership team aligned and moving fast; make sure decisions stick and are followed up on; manage information flow across the organisation
**Frustrations:** Decisions made in one room that contradict decisions made in another; executives who don't remember what they committed to; no system of record for organisational decisions
**Relationship to the product:** The persona most naturally aligned with Loopback's core thesis — their entire job is organisational memory and decision accountability
**Buying role:** Often the Approver; sometimes the Driver of the evaluation process

---

### Persona C — The IT Administrator
**Role:** IT Manager or Director, responsible for procurement, security, and tool governance
**Goals:** Maintain security posture; reduce tool sprawl; ensure compliance with data handling policies; avoid incidents caused by unsanctioned software
**Frustrations:** Teams adopting tools without IT sign-off; unclear data retention policies from vendors; SSO integrations that break; being brought in at the end of a procurement process rather than the beginning
**Relationship to the product:** Not a user of the product's core value; evaluates on security, compliance, and integration reliability — the SSO incident at Meridian is exactly the kind of thing that makes this persona distrust a vendor
**Buying role:** Blocker or enabler — rarely initiates, but can kill a deal

---

### Persona D — The New Team Member
**Role:** Any new hire in their first 30–90 days
**Goals:** Get up to speed quickly; understand how decisions are made; avoid making proposals that contradict established positions; build credibility fast
**Frustrations:** No reliable way to understand the history of a project; institutional knowledge lives in people who are too busy to share it; feeling behind
**Relationship to the product:** End beneficiary of the decision graph and Smart Handoff — not a buyer, but the persona whose experience most strongly validates the product's value to their manager
**Buying role:** Influenced party — their positive experience creates internal advocates and supports renewal

---

## Product × persona matrix

The matrix below maps each product to each persona: what the core value frame is, what the primary proof point should be, and what objection is most likely to arise.

| | Engineering Lead | Chief of Staff | IT Administrator | New Team Member |
|---|---|---|---|---|
| **Loopback (decision graph)** | "Stop relitigating architecture decisions" | "The organisational memory you've been trying to build manually" | "SOC 2 Type II, SSO, configurable retention" | "Understand 6 months of context in an afternoon" |
| **Smart Handoff** | "Hand off a project without a 3-hour knowledge dump" | "Make departures survivable" | "Data scoped to the project, not the whole org" | "Get a reliable starting point, not a pile of Slack" |
| **Nova Dashboard** | "Status visibility without status meetings" | "One view of everything leadership needs to know" | "Centralised integration governance" | "See how your work fits into the bigger picture" |

---

## Persona-specific messaging examples

### Loopback → Engineering Lead

**Headline:** Stop losing architectural decisions to turnover and time.

**Body:** Every engineering team makes hundreds of decisions a year about how to build and what to build next. Most of them live in meeting notes no one can find, in the heads of engineers who've since moved teams, or nowhere at all. Loopback builds a searchable decision graph from your recurring meetings — so when someone asks "why did we choose this approach?", the answer is one query away.

**Proof point:** Teams using Loopback reduce time spent re-explaining context in handoffs by an average of 40%. Engineers report spending less time in recurring syncs because decisions from the previous session are surfaced automatically at the start of the next one.

**Objection:** *"We already take notes in Notion."*
**Response:** Notes capture what happened. Loopback captures what was decided and connects it to future conversations — so when the same topic resurfaces three months later, it knows. Notion doesn't.

---

### Loopback → Chief of Staff

**Headline:** The organisational memory system you've been building by hand.

**Body:** A Chief of Staff's core function is often described as "making the leadership team effective." In practice, a significant portion of that job is institutional memory — knowing what was decided, who committed to what, and whether this week's proposal contradicts something agreed to last quarter. Loopback automates that function. It builds a structured record of decisions across every meeting, surfaces contradictions in real time, and prepares every recurring meeting with a brief that shows what was decided last time and what's still open.

**Proof point:** Chiefs of Staff who pilot Loopback consistently report that the pre-meeting brief alone saves 2–3 hours per week in preparation time and reduces the frequency of "we already decided this" moments by over half.

**Objection:** *"Our executives won't want their meetings recorded."*
**Response:** Loopback works with recording or without — it can ingest notes, transcripts from existing tools, or async voice memos. Recording is one input, not a requirement.

---

### Loopback → IT Administrator

**Headline:** Meeting intelligence that IT can actually approve.

**Body:** Most tools that touch your meeting data are designed for the people in the room, not for the people responsible for your security posture. Loopback is built with IT in mind: SOC 2 Type II certified, SSO via SAML 2.0 with major IdPs, configurable data retention and deletion policies, and a data processing agreement that covers GDPR and CCPA requirements out of the box. We don't train AI models on your meeting data without explicit consent. Your data stays yours.

**Proof point:** Loopback completes IT security reviews in an average of 6 business days. We maintain a security trust portal at security.loopback.ai with up-to-date compliance documentation, penetration test summaries, and subprocessor information.

**Objection:** *"We had an SSO issue with your onboarding before."*
**Response:** Acknowledged directly. The SSO issue in our February rollout at a similar-sized account was caused by a misconfiguration in our pre-launch checklist — we've since updated our technical onboarding process to include an IdP dry run two weeks before go-live. We'd be glad to walk you through the updated process before we touch your environment.

---

### Smart Handoff → New Team Member

**Headline:** Six months of context in an afternoon.

**Body:** Starting a new role or picking up a project mid-flight means spending weeks piecing together history from Slack threads, half-finished Notion docs, and whoever still remembers what happened. Smart Handoff generates a structured briefing document from the project's meeting and decision history — what was decided, what's currently open, who owns what, and where to start. It's the onboarding doc that no one ever had time to write.

**Proof point:** New team members with a Smart Handoff document available reach independent contribution 40% faster than those who don't — measured by time to first unassisted pull request or unassisted client interaction, depending on role.

**Objection:** *"I'd rather just talk to the previous owner."*
**Response:** You should — and Smart Handoff makes that conversation better. Instead of spending 2 hours covering basics, you can use the time to ask the questions the document couldn't answer.

---

## Implications for product and marketing

### Product prioritisation
The IT Administrator persona is a blocking persona — they cannot drive adoption but they can prevent it. Investing in the security review experience (trust portal, SSO reliability, a dedicated IT onboarding track) is not a product luxury; it is a sales velocity investment.

The New Team Member persona is an amplification persona — they do not buy but their experience creates internal advocacy. Features that serve them (better decision search, faster brief generation, clearer project history UI) directly influence renewal and expansion.

### Content strategy
Content mapped to the Engineering Lead and Chief of Staff personas should dominate the top of funnel — these are the people actively searching for the problem Loopback solves. Content for IT Administrators should live in the trust portal and in the sales process, not in public SEO content. Content for New Team Members is best delivered inside the product itself, not through marketing channels.

### Sales motion
The combination Engineering Lead (champion) + Chief of Staff (approver) is the highest-converting buying team. Deals where IT is brought in before the champion is fully sold tend to stall. Deals where IT is ignored until late tend to die in legal review. The optimal sequence: land the Engineering Lead or Chief of Staff, build internal momentum, then proactively surface the IT Administrator track — ideally by sending them directly to security.loopback.ai before they ask.

---

*Working document. Internal use only.*
