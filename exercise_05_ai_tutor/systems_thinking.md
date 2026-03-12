# Systems thinking
**Document type:** Conceptual framework and applied guide
**Author:** Strategy & Operations
**Organisation:** Arclight AI
**Date:** March 2026
**Status:** Working document

---

## What systems thinking is

Systems thinking is a way of understanding the world that focuses on relationships, feedback, and interdependence rather than isolated causes and effects.

Linear thinking says: A causes B. Systems thinking says: A causes B, which causes C, which loops back to affect A — and meanwhile, D is running in the background amplifying the whole thing, and we only noticed B because it was the most visible part.

This matters because most of the problems that are genuinely hard to solve — in organisations, markets, products, and policy — are hard precisely because they are systemic. They persist not because no one is trying to fix them, but because the structure of the system keeps regenerating the problem regardless of the intervention.

Systems thinking does not make hard problems easy. It makes the structure of the difficulty visible, which is the prerequisite for doing something about it.

---

## Core concepts

### Stocks and flows

A **stock** is any quantity that accumulates or depletes over time — customers, revenue, technical debt, team morale, institutional knowledge, trust.

A **flow** is the rate at which a stock changes — new customers acquired, revenue recognised, bugs introduced, energy depleted, knowledge lost.

Most management attention goes to flows (what happened this month) when the underlying problem is a stock (what has been accumulating for years). Fixing a flow without understanding the stock it feeds or drains often produces results that disappear quickly.

*Example at Arclight:* The metric "number of support tickets this week" is a flow. The underlying stock is "unresolved product confusion" — a function of onboarding quality, documentation completeness, and UI clarity accumulated over every release. Reducing tickets by faster resolution addresses the flow; improving onboarding addresses the stock.

---

### Feedback loops

Feedback loops are the engine of system behaviour. There are two types:

**Reinforcing loops (R)** amplify change. They are the source of growth and of collapse. A reinforcing loop does not stabilise — it accelerates in one direction until something intervenes.

> More customers → more word of mouth → more customers

> More technical debt → slower development → more shortcuts taken → more technical debt

**Balancing loops (B)** resist change and seek equilibrium. They are the source of stability and of stubbornness. A balancing loop pushes back against deviation from a target state.

> Revenue below target → sales activity increases → revenue recovers toward target

> Team overloaded → work quality drops → bugs increase → pressure to slow down → pace adjusts

Most real systems have multiple feedback loops operating simultaneously, often in tension. Understanding which loops are dominant in a given situation — and what would shift dominance — is the central analytical question in systems thinking.

---

### Delays

Delays are among the most important and most overlooked features of a system. When there is a significant delay between an action and its consequence, several things happen:

- People stop associating the cause with the effect
- Interventions are abandoned before they have time to work
- Overcorrections are made because the feedback from a previous correction has not yet arrived
- Problems are attributed to the wrong cause because the real cause occurred far earlier

*Example:* A decision to invest in documentation quality today will not visibly reduce support ticket volume for 3–6 months. Without systems awareness of this delay, the investment appears not to be working and is abandoned — just before it would have compounded.

The practical rule: in any system with significant delays, expect overshoot and oscillation. Design for it rather than being surprised by it.

---

### System archetypes

Certain feedback structures appear repeatedly across different domains. Recognising them shortens the time from "something is wrong here" to "I understand what's structurally causing this."

**Limits to growth**
A reinforcing loop driving growth runs into a balancing loop that slows it. The natural response — push harder on the growth driver — makes things worse. The leverage is on the limiting constraint, not the growth engine.

*Arclight example:* PLG conversion is growing (reinforcing: more free users → more conversions → more word of mouth), but CS capacity is a binding constraint (balancing: more conversions → more onboarding load → slower time-to-value → lower NRR). Pushing sales harder without resolving CS capacity will accelerate the problem, not the growth.

**Shifting the burden**
A symptomatic fix relieves pressure from a problem without addressing its root cause. Over time, the capacity to address the root cause atrophies — and the system becomes dependent on the symptomatic fix.

*Example:* Using escalations and manual intervention to resolve enterprise onboarding failures (symptomatic fix) instead of improving the onboarding product itself (fundamental fix). The escalation team grows, becomes a dependency, and the onboarding product never gets fixed because the pressure is never felt acutely enough.

**Tragedy of the commons**
Multiple actors share a common resource. Each actor, acting rationally in their own interest, degrades the resource for all. No individual actor has the incentive to restrain their use; collective restraint requires coordination.

*Example:* Shared engineering capacity treated as a common resource by multiple product teams. Each team rationally requests as much as possible. The resource is overcommitted, velocity drops for everyone, and no single team's rational behaviour is the cause — the structure is.

**Eroding goals**
When performance falls short of a goal, there are two options: improve performance, or lower the goal. Lowering the goal is easier and faster. Over time, if this pattern repeats, the goal drifts downward while the gap feels closed.

*Example:* An NRR target of 120% slips to 115% "given market conditions", then to 110% "while we're investing in the product." Each adjustment feels justified. The underlying capability gap — the real reason NRR is not 120% — is never addressed.

---

### Leverage points

Donella Meadows identified a hierarchy of places to intervene in a system, ordered roughly from least to most powerful:

| Leverage point | Example | Power |
|---|---|---|
| Numbers (constants, parameters) | Change a price, a tax rate, a budget | Low |
| Buffer sizes | Increase inventory, cash reserves | Low–Medium |
| Flow rates | Hire faster, ship more frequently | Medium |
| Feedback loop strength | Shorten the time between action and consequence | Medium–High |
| Information flows | Make visible what was hidden | High |
| Rules of the system | Change incentives, regulations, constraints | High |
| Goals of the system | Change what the system is optimising for | Very high |
| Mindsets and paradigms | Change the underlying beliefs that generate the system | Highest |

The counterintuitive implication: most management effort goes into the lowest-leverage interventions (parameters and budgets) while the highest-leverage points — information flows, goals, and mental models — are rarely touched because they are less legible and more politically difficult.

---

## Applied systems thinking — a process

### Step 1: Define the system and its purpose

Every system has a purpose — the outcome it actually produces, not the outcome it was intended to produce. Be precise: what is the system optimising for, and for whom?

Start by identifying: the key stocks, the key actors, and the time horizon over which the behaviour plays out.

### Step 2: Map the causal structure

Build a causal loop diagram: identify the main variables, draw arrows showing causal relationships, label each link as positive (an increase in A increases B) or negative (an increase in A decreases B), and identify the feedback loops.

This is a qualitative exercise. The goal is not precision — it is shared understanding of the structure.

### Step 3: Identify delays

Mark the significant delays in the causal map. Ask: if we act here, how long before we see the consequence? Where are we likely to overcorrect because feedback is slow?

### Step 4: Look for archetypes

Does the structure match a known archetype? If so, what does the archetype predict will happen next, and what does it say about where leverage actually lies?

### Step 5: Identify leverage

Given the causal structure, where are the highest-leverage intervention points? What would change the goals, the information flows, or the feedback loop strength — rather than just adjusting a parameter?

### Step 6: Design interventions with awareness of side effects

Every intervention in a system has side effects. The question is not whether there will be unintended consequences, but which ones and when. Map the likely side effects of any proposed intervention before committing to it.

---

## Arclight AI — a systems map (sketch)

The following describes the key feedback structure driving Arclight's growth and its primary constraint:

**Reinforcing loop R1 — PLG flywheel**
Product quality → free trial conversion → paying customers → word of mouth → new free trials → product quality investment (funded by revenue)

**Reinforcing loop R2 — data advantage**
More customers → more meeting data processed → better AI model performance → better product → more customers

**Balancing loop B1 — CS constraint**
More customers → more onboarding demand → CS team overloaded → slower time-to-value → higher churn → fewer customers

**Balancing loop B2 — enterprise complexity**
Larger enterprise deals → more custom requirements → longer implementation time → higher CS cost per account → margin pressure → fewer resources for product

**Key delay:** Product quality improvements take 2–3 quarters to manifest in NRR data, creating a structural underinvestment in product relative to near-term CS firefighting.

**Highest leverage point identified:** Automate onboarding for the Growth tier (currently manual) to decouple B1 from PLG growth. This removes the binding constraint without adding CS headcount, allowing R1 to accelerate without hitting B1.

**Second-order effect to watch:** Automated onboarding reduces human touchpoints in the 0–30 day window. If this reduces early-stage relationship quality for accounts that later grow to Enterprise size, it may suppress expansion MRR. Monitor expansion rates by onboarding cohort.

---

## Further reading

- *Thinking in Systems* — Donella Meadows
- *The Fifth Discipline* — Peter Senge
- *An Introduction to Systems Thinking* — Barry Richmond
- *Leverage Points: Places to Intervene in a System* — Donella Meadows (essay, freely available)

---

*Working document. Internal use only.*
