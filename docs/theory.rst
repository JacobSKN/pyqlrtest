QLR Test Theory (Brief)
=======================

The Quandt Likelihood Ratio (QLR) test, also known as the sup-F test, is used to test for a single unknown structural break in a linear regression model.

Consider the linear model:
$$ y_t = X_t'\beta_t + \epsilon_t $$

If there's a structural break at time $\tau$, the coefficients change:
$$ \beta_t = \beta_1 \quad \text{for } t \le \tau $$
$$ \beta_t = \beta_2 \quad \text{for } t > \tau $$

The null hypothesis is that there is no structural break (i.e., $\beta_1 = \beta_2$).
The alternative hypothesis is that there is a break at some unknown point $\tau$.

The QLR test statistic is the maximum of individual Chow F-statistics calculated for each possible breakpoint $\tau$ within a trimmed portion of the sample $[\pi_0 T, (1-\pi_0)T]$, where $T$ is the sample size and $\pi_0$ is the trimming percentage (e.g., 0.15).

$$ QLR = \sup_{\tau \in [\pi_0 T, (1-\pi_0)T]} F(\tau) $$

The $F(\tau)$ statistic for a given breakpoint $\tau$ is:
$$ F(\tau) = \frac{(RSS_0 - (RSS_1(\tau) + RSS_2(\tau)))/k}{(RSS_1(\tau) + RSS_2(\tau))/(T - 2k)} $$
where:
- $RSS_0$ is the residual sum of squares from the model estimated over the full sample (no break).
- $RSS_1(\tau)$ is the RSS from the model estimated for the first segment ($1$ to $\tau$).
- $RSS_2(\tau)$ is the RSS from the model estimated for the second segment ($\tau+1$ to $T$).
- $k$ is the number of regressors in $X_t$.
- $T$ is the total number of observations.

The asymptotic distribution of the QLR statistic is non-standard and depends on the number of regressors ($k$) and the trimming parameter ($\pi_0$). P-values are typically obtained using approximations developed by Hansen (1997, 2000) or critical values from tables by Andrews (1993, 2003).

References
----------
- Andrews, D. W. K. (1993). Tests for parameter instability and structural change with unknown change point. *Econometrica*, 61(4), 821-856.
- Andrews, D. W. K. (2003). Tests for parameter instability and structural change with unknown change point: A corrigendum. *Econometrica*, 71(1), 395-397. (Provides CV tables like Table 1, p.168 for pi0=0.15)
- Hansen, B. E. (1997). Approximate asymptotic p-values for structural-change tests. *Journal of Business & Economic Statistics*, 15(1), 60-67.
- Hansen, B. E. (2000). Erratum: Approximate asymptotic p-values for structural-change tests. *Journal of Business & Economic Statistics*, 18(4), 511.