# Business model innovation
**Document type:** Strategic framework
**Author:** Strategy & Operations
**Organisation:** Arclight AI
**Date:** March 2026
**Status:** Working document

---

## What business model innovation is

Most companies compete by improving their product. Business model innovation is different — it means changing *how* the company creates, delivers, and captures value, not just what it sells. A company with a mediocre product and a great business model will often outperform a company with a great product and a conventional one.

The distinction matters because product improvements are increasingly easy to copy. Business model advantages — embedded workflows, switching costs, network effects, pricing structures — are structurally harder to replicate.

Business model innovation is not a one-time exercise. It is a capability: the ability to systematically examine how value flows through the business, identify where the current model leaves money on the table or creates unnecessary friction, and design alternatives that serve customers better while improving unit economics.

---

## The components of a business model

A business model answers four questions:

**1. Who do we create value for?**
The customer segment — not just a demographic, but a set of jobs to be done, problems to solve, and outcomes to enable. Business model innovation often begins with noticing that the stated customer and the actual value recipient are different people.

**2. What value do we create?**
The value proposition — the specific combination of outcomes, features, and experience that makes a customer choose you over alternatives, including doing nothing.

**3. How do we deliver it?**
The operating model — the activities, resources, partnerships, and channels that produce and distribute the value. This is where most execution lives and where most costs are incurred.

**4. How do we capture value?**
The revenue model — pricing structure, payment timing, monetisation logic, and the relationship between value delivered and revenue recognised.

Most businesses have implicit answers to all four questions. Business model innovation makes those answers explicit and asks whether they are still the right ones.

---

## Where innovation typically happens

### Redefining the customer

The most underexplored lever. Who is the buyer, who is the user, who bears the cost of the problem you solve, and who benefits from the solution? These are often different people, and pricing to the wrong one leaves money on the table.

*Example:* Loopback's initial instinct was to sell to individual knowledge workers. But the pain of lost institutional knowledge is felt most acutely by executives and team leads — and the budget sits with IT or Operations. Reframing the customer from "the person in the meeting" to "the person accountable for team effectiveness" changes the sales motion, the pricing logic, and the product emphasis entirely.

### Shifting from product to outcome

Customers do not want software. They want the result the software enables. Pricing and positioning that speaks to outcomes — time saved, decisions retained, onboarding shortened — commands a premium and creates a different relationship than feature-based selling.

*Implication for Arclight:* Instead of selling "seats on the Nova Dashboard", what if we sold "decisions documented per quarter" or guaranteed a time-to-value SLA and refunded if unmet? Outcome-based models require more confidence in delivery but attract customers who are outcome-oriented buyers.

### Unbundling and rebundling

Existing markets are often bundled in ways that serve incumbents rather than customers. Innovation can come from stripping away everything except the core job to be done (unbundling) or from combining previously separate things into a new whole (rebundling).

*Example:* The Launch Programme (rule 6, service offering) is a rebundle: onboarding, configuration, training, and early CS are typically separate line items or absorbed as cost of sales. Packaging them as a named, priced product changes the customer's perception from "vendor support" to "implementation partner" — and turns a cost centre into a revenue line.

### Changing the pricing axis

Revenue models are often inherited from industry convention rather than designed. The right pricing axis aligns the company's incentives with the customer's value realisation.

Common axes and their logic:

| Pricing axis | Best when… | Risk |
|---|---|---|
| Per seat | Value scales with users | Customers cap seats to manage costs |
| Per usage | Value scales with consumption | Unpredictable revenue; customers avoid heavy use |
| Per outcome | Value is clearly measurable | Hard to attribute; requires trust |
| Flat subscription | Value is broad and hard to meter | Leaves revenue on table for high-usage accounts |
| Freemium | Acquisition cost is high; viral loops exist | Free tier cannibalises paid if not designed carefully |

Arclight's current per-seat model works but creates an incentive for customers to minimise licensed seats. A usage-based component — priced per meeting processed or per decision record stored — would align revenue more directly with value and reduce the tension between sales and customer success on seat counts.

### Platform and ecosystem models

A platform model changes the business from a producer of value to an orchestrator of value created by others. Network effects — where the platform becomes more valuable as more participants join — are the most durable competitive moat available to a software business.

For Loopback, this might mean: opening an API that allows third-party developers to build on the decision graph, creating an ecosystem of integrations, templates, and industry-specific applications that Loopback does not have to build itself. The platform earns value from ecosystem activity; the ecosystem grows the platform's reach.

Platform models require a different build strategy (openness, developer experience, trust), a different revenue model (often a take rate or API call fee rather than pure seat licensing), and a different measure of success (ecosystem health metrics alongside ARR).

---

## A framework for evaluating model alternatives

When assessing a new business model option, apply five tests:

### 1. Desirability
Do customers actually want this? Would they pay for it, switch to it, or refer others because of it? Desirability is validated through customer conversations, willingness-to-pay research, and pilot conversion rates — not internal enthusiasm.

### 2. Viability
Does it produce sustainable economics? Model the unit economics of the alternative: contribution margin, CAC, payback period, LTV. A business model that customers love but that cannot be delivered profitably is a charity, not a business.

### 3. Feasibility
Can we build and operate it with our current or achievable capabilities? Some business models are theoretically attractive but require capabilities the company does not have and cannot realistically develop — operational complexity, regulatory expertise, infrastructure.

### 4. Defensibility
Does the new model create structural advantages that compound over time? Network effects, data advantages, switching costs, and ecosystem lock-in are the most valuable. Price-based advantages are the least.

### 5. Coherence
Does the new model reinforce the existing model or undermine it? Businesses that run two conflicting models simultaneously — different pricing, different channels, different customer relationships — often find that the models cannibalise each other rather than complement.

---

## The innovation process

Business model innovation rarely arrives fully formed. It follows a process:

**1. Map the current model explicitly.** Most teams have only an implicit understanding of how their business model works. Write it down across all four dimensions. Surface the assumptions embedded in it.

**2. Stress-test the assumptions.** Which assumptions is the current model most dependent on? What happens if they no longer hold? (e.g. "We assume per-seat pricing scales with enterprise value" — does it?)

**3. Generate alternatives deliberately.** Use the levers above — customer redefinition, pricing axis shift, unbundling, platform — to generate at least three distinct model alternatives. Resist the pull toward the most incremental option.

**4. Prototype and test.** Business model changes can be piloted before full commitment. A new pricing structure can be tested with a cohort of new customers. A new customer segment can be approached with a dedicated sales motion. Design the smallest test that produces signal.

**5. Sequence the transition.** Moving from one business model to another is rarely a clean cut. Map the transition: what must change first, what can change in parallel, what must wait, and what legacy commitments must be honoured through the shift.

---

## Arclight AI — current model assessment

| Dimension | Current state | Key assumption | Vulnerability |
|---|---|---|---|
| Customer | Mid-market SaaS teams, PM/Ops buyer | Buyer and user are aligned | Mismatch emerging in enterprise: IT buys, PMs use |
| Value proposition | AI-powered work context, decision tracking | Teams want to document decisions | Teams want to *retrieve* decisions — subtly different |
| Operating model | Self-serve + CS-led for enterprise | CS scales linearly with ARR | CS cost grows faster than revenue without automation |
| Revenue model | Per seat, annual subscription | Seat count correlates with value | High-value accounts minimise seats; low-value accounts over-license |

**Priority innovation opportunity:** Introduce a usage-based pricing component (meetings processed or decisions stored per month) alongside seat licensing. Pilot with 5 new Enterprise accounts in Q2. Measure impact on ACV, expansion MRR, and CS burden.

---

## Further reading

- *Business Model Generation* — Osterwalder & Pigneur
- *The Innovator's Dilemma* — Clayton Christensen
- *Escape Velocity* — Geoffrey Moore
- *The Cold Start Problem* — Andrew Chen (on network effects and platform models)

---

*Working document. Internal use only.*
