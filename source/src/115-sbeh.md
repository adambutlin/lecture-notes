## Behavioural economics {#sbeh}

> **DEFINITIONS.**\
> **Bounded rationality**: decision-making limited by the information, time and mental effort available, so that people settle for a good choice rather than the best one.\
> **Bounded self-control**: knowing what is best and failing to do it, typically by favouring the present over the future.\
> **Bounded selfishness**: caring about other people's outcomes and about fairness, not only one's own consumption.\
> **Heuristic (rule of thumb)**: a shortcut that saves effort at the cost of occasional error.\
> **Anchoring**: judging a value by adjusting from an initial number, even an irrelevant one.\
> **Availability bias**: judging how likely something is by how easily examples come to mind.\
> **Framing**: a choice changing with the way identical options are described.\
> **Loss aversion**: a loss weighing more heavily than a gain of the same size.\
> **Choice architecture**: the way options are presented, including **default choices** (what happens if nobody acts), **restricted choice** (fewer options) and **mandated choice** (people must actively decide).\
> **Nudge**: a change in choice architecture that alters behaviour without forbidding any option or changing prices.

Section {sec:s1} built demand on a household that ranks bundles consistently, knows what it wants, and calculates its best choice. Each of those is an assumption that can be tested, and behavioural economics is the study of where they fail and what follows. It does not replace the model of section {sec:s1}. It identifies which of that model's assumptions breaks in a particular setting, and so which of its predictions should not be trusted there.

Consistency over time is the cleanest case, because it can be written down. A household that discounts the future at a constant rate values £1 received $t$ days from now at $\delta^{t}$ pounds today, for some $\delta$ just below one. Its preference between two dated payments never depends on when it is asked. Experiments repeatedly find something different. Offered £100 today or £110 tomorrow, many people take the £100; offered £100 in 30 days or £110 in 31 days, the same people wait for the £110. The two choices are the same one-day trade, moved a month into the future. A discount function that treats the present as special reproduces the pattern:

$$D(0) = 1,\quad\quad D(t) = 0.7 \times 0.99^{t}\quad\text{for } t \geq 1\quad(\#ebeta)$$

$D(t)$ is the value today of £1 received in $t$ days. Today against tomorrow, £100 beats $110 \times 0.7 \times 0.99 = £76$. A month ahead, $100 \times 0.7 \times 0.99^{30} = £52$ loses to $110 \times 0.7 \times 0.99^{31} = £56$. The household plans to wait, and when day 30 arrives and the earlier payment has become "today", it changes its mind. That is bounded self-control expressed as a single number: the factor 0.7 that applies to every future date and to none of the present. It explains under-saving for retirement, unused gym memberships and the appeal of commitment devices, which are ways for the planning self to bind the self that will later face the choice.

Loss aversion is the second case with a precise shape. People evaluate outcomes as gains and losses relative to a reference point, usually what they already have or expect, rather than as final levels of wealth, and losses count for roughly twice as much as gains of the same size. Figure {fig:lossav} draws a value function with that property. Its kink at the reference point is what the smooth utility function of section {sec:s1} cannot produce, and it explains why people refuse a fair bet of winning or losing £100, why sellers ask more for an object than they would have paid for it, and why the same policy described as "avoiding a loss" wins more support than when it is described as "securing a gain", which is framing.

![Figure {fig:lossav}. A value function with loss aversion. Outcomes are measured as gains and losses from a reference point, the curve is steeper for losses than for gains, and it is kinked at the reference point.](figs/lossav.png)

The remaining failures are documented more than modelled. Heuristics save effort and are usually sensible, but they leave fingerprints: a shop's "was £80, now £40" sets an anchor that makes £40 look cheap whatever the good is worth, and vivid news of plane crashes makes flying seem more dangerous than driving, which is availability. Bounded selfishness shows up when people give to charity, punish unfairness at a cost to themselves, or refuse a low but positive offer in a bargaining experiment.

If behaviour depends on how choices are presented, then presentation is a policy instrument. The best-known example is automatic enrolment into workplace pensions in the UK, introduced in 2012: employees are enrolled unless they opt out, rather than left out unless they opt in. Nothing about the pension changed except the default, and participation rose sharply. Restricted choice (removing confusing tariffs), mandated choice (organ donation registers that require a yes or no) and well-timed information (energy bills that compare a household with its neighbours) work the same way. A nudge leaves every option open and every price unchanged, which is why it is attractive to governments, and it acts only on people whose behaviour was driven by the presentation in the first place.

> **ASSUMPTIONS.**\
> The discount function ({eq:ebeta}) and the factor of two in loss aversion are typical experimental findings, not constants of nature, and both vary between people and settings.\
> Behavioural findings are departures from a benchmark. Without the model of section {sec:s1} there would be nothing to depart from, so the two are complements rather than rivals.\
> A nudge assumes the designer knows better than the person nudged which choice serves that person. Governments are subject to the same biases they set out to correct, and choice architecture can be used by firms to exploit biases as easily as by governments to offset them.
