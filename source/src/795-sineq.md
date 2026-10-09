## Inequality and redistribution {#sineq}

> **DEFINITIONS.**\
> **Equality** means everyone has the same income or wealth; **equity** means a distribution judged to be fair, which need not be equal.\
> **Income** is a flow received over a period; **wealth** is a stock of assets owned at a moment.\
> **Absolute poverty**: income too low to buy the basic necessities of life.\
> **Relative poverty**: income below a fraction of the typical income in a society; the UK measure is below 60 per cent of median household income.\
> **Lorenz curve**: the share of total income received by the poorest fraction of the population, plotted against that fraction.\
> **Gini coefficient**: a measure of inequality from 0 (complete equality) to 1 (one person has everything).\
> **Average tax rate**: tax paid as a share of income; **marginal tax rate**: the share of an extra pound taken in tax.\
> **Progressive tax**: the average rate rises with income; **proportional**: it is constant; **regressive**: it falls.

Section {sec:s11} measured the size of the pie and said nothing about how it is divided. The division can be drawn. Rank the population from poorest to richest and let $\ell(p)$ be the share of total income received by the poorest fraction $p$. If everyone had the same income, the poorest 20 per cent would have 20 per cent of income, and $\ell(p) = p$, the 45-degree line. With any inequality the curve sags below that line, because the poorest 20 per cent receive less than 20 per cent. The Gini coefficient measures the sag. It is the area between the line of equality and the Lorenz curve, A in Figure {fig:lorenz}, as a fraction of the whole triangle under the line of equality, which has area one half:

$$\text{Gini} = \frac{A}{A + B} = \frac{\tfrac{1}{2} - \int_{0}^{1}\ell(p)\,dp}{\tfrac{1}{2}} = 1 - 2\int_{0}^{1}\ell(p)\,dp\quad(\#egini)$$

The integral is the area $B$ under the Lorenz curve, the same use of an integral to add up a curve as the surplus of ({eq:e30}). A Lorenz curve $\ell(p) = p^{2}$, in which the poorest half of the population receives a quarter of income, has $\int_{0}^{1}p^{2}dp = 1/3$ and a Gini coefficient of $1 - 2/3 = 1/3$. A more unequal distribution, $\ell(p) = p^{3}$, gives $1 - 2/4 = 1/2$. UK disposable income has had a Gini coefficient of roughly 0.3 to 0.35 in recent years. Wealth is far more unequally distributed than income, because wealth accumulates from income that is saved and passed on.

![Figure {fig:lorenz}. Lorenz curves. The Gini coefficient is area A divided by the whole triangle A + B; the curve $\ell(p) = p^{2}$ gives a Gini of 1/3 and $\ell(p) = p^{3}$ gives 1/2.](figs/lorenz.png)

Inequality in market incomes comes from differences in what people own and in what their labour earns. Section {sec:slab} explained the second: wages reflect marginal revenue products, so differences in skills, education and the demand for particular work produce differences in pay, and employer power can push wages below marginal revenue product. Ownership of capital and land, and its transmission between generations, explains much of the rest. Technological change that raises the productivity of skilled workers more than others, and globalisation that exposes some workers to competition from abroad, have widened market-income inequality in many rich countries.

Governments redistribute through taxes and transfers. Whether a tax is progressive is a question about its average rate, and section {sec:s2}'s lemma about marginal and average quantities settles it. If $T(Y)$ is the tax paid on income $Y$, the average rate is $T/Y$ and the marginal rate is $dT/dY$, and by the quotient rule

$$\frac{d}{dY}\left( \frac{T}{Y} \right) = \frac{1}{Y}\left( \frac{dT}{dY} - \frac{T}{Y} \right)\quad(\#eprog)$$

The average rate rises with income, making the tax progressive, exactly when the marginal rate is above the average rate. A tax with a tax-free allowance and a single rate above it is therefore progressive: with an allowance of £12,570 and a rate of 20 per cent, someone earning £20,000 pays £1,486, an average rate of 7.4 per cent, while someone earning £50,000 pays an average rate of 15 per cent, even though both face the same marginal rate of 20 per cent. Confusing the two rates is the commonest error in this topic. Indirect taxes such as VAT are regressive in their impact, because lower-income households spend a larger share of their income.

Redistribution has costs as well as benefits. Higher marginal tax rates weaken the incentive to work, train and invest, the Laffer argument of section {sec:s23} applied to a single tax, and benefits that are withdrawn as earnings rise create high effective marginal rates for the low-paid. How much efficiency to give up for how much equity is a value judgement, not a theorem, and economics can measure the trade-off but cannot settle it.

> **ASSUMPTIONS.**\
> The Lorenz curve ranks households by income in one period; incomes that vary over a lifetime look more unequal in a single year than over a whole life.\
> The tax example ignores National Insurance and the withdrawal of the personal allowance at high incomes.
