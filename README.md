## Power

Power in hypothesis testing measures the probability of correctly rejecting a null hypothesis when it is false. In other words, it quantifies the ability of a statistical test to detect an effect or relationship if it genuinely exists.

To calculate power for a hypothesis test four main parameters need to be considered:

1.  Effect Size ($d$): Cohen's $d$ is a common measure of effect size comparing means and represents the standardized difference between the means of two groups (e.g., treatment group and control group) divided by the pooled standard deviation. It quantifies the strength of the phenomenon relative to the variability in the population.

2.  Significance Level ($\alpha$): This is the probability of making a Type I error, which is the rejection of a true null hypothesis. It is typically set to a pre-defined level, often 0.05, indicating a 5% chance of false positive

3.  Population Standard Deviation ($\sigma$): The standard deviation of the entire population under study. In practice, this parameter is often unknown and estimated from the sample data.

4.  Sample Size of Both Groups ($n$ and $m$): The number of observations or participants in each group.

## Computing power for a two-sample t-test

To compute power, the first step is to estimate the pooled standard deviation ($s$) between the two groups:

$$
s = \sqrt{\frac{(n_X-1)s_X+(n_Y -1)s_Y}{n_X+n_Y - 2}} 
$$

where $s_X$ and $s_Y$ are the sample variances of groups $X$ and $Y$ respectively.

Next, we calculate the effect size ($d$) using the formula:

$$
d = \frac{\bar{X}-\bar{Y}}{s}
$$

where $\bar{X}$ and $\bar{Y}$ are the sample means of groups $X$ and $Y$ respectively.

It is crucial to note that these calculations are based on certain assumptions. For the two-sample t-test, assume that:

-   The two groups are independent.

-   The variances of the two groups are equal (homogeneity of variances).

-   The data is approximately normally distributed. For samples \> 30 the normality assumption holds on account of the central limit theorem.

Alternatives for when these assumptions do not hold are Welchs t test and other non-parametric tests.

These assumptions should be checked prior to continuation of this step.

To determine the power, we need to find the probability that the effect size ($d$) falls into the rejection region, given by:

$$
P(\vert d\vert > z(\frac{\alpha}{2})) = P(d > z(\frac{\alpha}{2})) + P(d < -z(\frac{\alpha}{2})) 
$$

where $z(\frac{\alpha}{2})$ is the critical z-score corresponding to the significance level $\alpha$ (divided by 2 for a two-tailed test). This value can be obtained from the cumulative normal distribution $\phi$.

To explore the relationship between effect size, power and significance level please refer to this link for an [interactive app] and this one for the corresponding [Github repository]

**Power in the Context of Metabolomic Data**

Given the correlations and high dimensionality in metabolomic data, traditional methods of estimating sample size based on test power are not generally used. Instead, most approaches turn to simulations to estimate power, particularly when dealing with such complex datasets.

In this context, power is often equated with "sensitivity" or the "true positive rate", and is defined as:

$$
Power = \frac{True Positives(TP)}{True Positives(TP)+False Negatives(FN)}
$$

Here, power represents the proportion of genuine effects that the test accurately identifies as statistically significant. In simpler terms, it's the likelihood that the test will correctly spot a real difference or effect when it exists.

## References and further reading

-   Cohen, J., 1977. The Concepts of Power Analysis, in: Statistical Power Analysis for the Behavioral Sciences. Elsevier, pp. 1â€“17. https://doi.org/10.1016/B978-0-12-179060-8.50006-2

- Cohen, J., 1977. The t Test for Means, in: Statistical Power Analysis for the Behavioral Sciences. Elsevier, pp. 19â€“74. https://doi.org/10.1016/B978-0-12-179060-8.50007-4
