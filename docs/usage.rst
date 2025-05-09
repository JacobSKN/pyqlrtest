Usage
=====

Installation
------------

You can install `pyqlrtest` using pip:

.. code-block:: bash

   pip install pyqlrtest 
   # Or, if installing from source:
   # pip install .

Basic Example
-------------

Here's a quick example of how to use `pyqlrtest` to detect a structural break:

.. code-block:: python

   import numpy as np
   import statsmodels.api as sm # For generating X with intercept
   from qlrtest import qlr_test
   import matplotlib.pyplot as plt

   # --- 1. Generate Sample Data with a Known Breakpoint ---
   np.random.seed(42)
   n_obs = 200
   breakpoint_actual = 100
   
   # Independent variable (e.g., time trend) and intercept
   X_true = sm.add_constant(np.arange(n_obs), prepend=True) 
   
   # Coefficients before the break
   beta_pre = np.array([1.0, 0.2])  # intercept, slope
   # Coefficients after the break
   beta_post = np.array([5.0, -0.1]) # intercept changes, slope changes
   
   y_true = np.zeros(n_obs)
   y_true[:breakpoint_actual] = X_true[:breakpoint_actual, :] @ beta_pre
   y_true[breakpoint_actual:] = X_true[breakpoint_actual:, :] @ beta_post
   
   # Add some noise
   y_true += np.random.normal(0, 1.0, n_obs)

   # --- 2. Run the QLR Test ---
   # We provide y and X (which includes the intercept)
   # Set trimming to 15% (standard)
   results = qlr_test(y_true, X_true, trim=0.15, sig_level=0.05, return_f_stats_series=True)

   # --- 3. Print Results ---
   print("QLR Test Results:")
   print(f"  Maximum F-statistic: {results['max_f_stat']:.4f}")
   print(f"  Estimated Breakpoint Index: {results['breakpoint']}")
   print(f"  P-value: {results['p_value']:.4f}")
   print(f"  Significant at 5% level: {results['significant']}")
   print(f"  Approx. 5% Critical Value: {results['approx_critical_value']:.4f}")


   # --- 4. Plot F-statistics (Optional) ---
   if 'f_stats' in results and results['f_stats'] is not None:
       plt.figure(figsize=(10, 6))
       plt.plot(results['tested_indices'], results['f_stats'], marker='.', linestyle='-')
       plt.axvline(results['breakpoint'], color='r', linestyle='--', label=f"Estimated Breakpoint: {results['breakpoint']}")
       plt.axhline(results['approx_critical_value'], color='g', linestyle=':', label=f"Approx. 5% CV: {results['approx_critical_value']:.2f}")
       plt.title('QLR F-statistics across potential breakpoints')
       plt.xlabel('Breakpoint Index')
       plt.ylabel('F-statistic')
       plt.legend()
       plt.grid(True)
       plt.show()

This will output the test statistics and, if `matplotlib` is installed, show a plot of the F-statistics across potential breakpoints.