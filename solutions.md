# Exercise Solutions

## Session 4

Sneeze interaction model:

```python
COORDS = {
		"regressor": ["meds", "alcohol", "meds : alcohol"], 
		"obs_idx": range(len(sneezes))
}
with pm.Model(coords=COORDS) as m_sneeze_inter:

    # weakly informative priors
    a = pm.Normal("intercept", mu=0, sigma=5)
    b = pm.Normal("slopes", mu=0, sigma=1, dims="regressor")
    alpha = pm.Exponential("alpha", 1.0)

    # define linear model
    mu = pm.math.exp(a + b[0] * M + b[1] * A + b[2] * M * A)

    ## likelihood
    y = pm.NegativeBinomial("y", mu=mu, alpha=alpha, observed=S, dims="obs_idx")

    trace_sneeze_inter = pm.sample(random_seed=RANDOM_SEED)
```

Varying intercepts and slopes:

```python
with pm.Model(coords=coords) as varying_intercept_slope:
    floor_idx = pm.Data("floor_idx", floor_measure, dims="obs_id")
    county_idx = pm.Data("county_idx", county, dims="obs_id")

    # Priors
    mu_a = pm.Normal("mu_a", mu=0.0, sigma=10.0)
    sigma_a = pm.Exponential("sigma_a", 1)

    mu_b = pm.Normal("mu_b", mu=0.0, sigma=10.0)
    sigma_b = pm.Exponential("sigma_b", 1)

    # Random intercepts
    alpha = pm.Normal("alpha", mu=mu_a, sigma=sigma_a, dims="county")
    # Random slopes
    beta = pm.Normal("beta", mu=mu_b, sigma=sigma_b, dims="county")

    # Model error
    sigma_y = pm.Exponential("sigma_y", 1)

    # Expected value
    y_hat = alpha[county_idx] + beta[county_idx] * floor_idx

    # Data likelihood
    y_like = pm.Normal("y_like", mu=y_hat, sigma=sigma_y, observed=log_radon, dims="obs_id")
```