import numpy as np
import statsmodels.api as sm # For generating X with intercept
from qlrtest import qlr_test # Assuming pyqlrtest is installed or in PYTHONPATH
import matplotlib.pyplot as plt # Optional: for plotting

def run_example():
    """
    Demonstrates the use of the qlr_test function with synthetic data.
    """
    # --- 1. Generate Sample Data with a Known Breakpoint ---
    np.random.seed(42) # For reproducibility
    n_obs = 200
    breakpoint_actual = 100  # The true breakpoint index (0-indexed)
    
    # Independent variables: an intercept and a time trend
    # Using sm.add_constant to ensure an intercept column is first, like in many examples.
    X_data = sm.add_constant(np.arange(n_obs, dtype=float), prepend=True)
    # X_data will have shape (n_obs, 2)
    
    # Coefficients before the break
    beta_pre_break = np.array([1.0, 0.2])  # intercept_pre, slope_pre
    # Coefficients after the break (structural change)
    beta_post_break = np.array([5.0, -0.1]) # intercept_post, slope_post
    
    y_data = np.zeros(n_obs)
    
    # Generate data for the first segment
    y_data[:breakpoint_actual] = X_data[:breakpoint_actual, :] @ beta_pre_break
    # Generate data for the second segment
    y_data[breakpoint_actual:] = X_data[breakpoint_actual:, :] @ beta_post_break
    
    # Add some Gaussian noise to the dependent variable
    noise_std_dev = 1.0
    y_data += np.random.normal(0, noise_std_dev, n_obs)

    print(f"Running QLR test on synthetic data with an actual break at index {breakpoint_actual}...")
    print(f"Data characteristics: n_obs={n_obs}, n_regressors(incl. intercept)={X_data.shape[1]}")
    print(f"Coefficients pre-break: {beta_pre_break}")
    print(f"Coefficients post-break: {beta_post_break}")
    
    # --- 2. Run the QLR Test ---
    # Standard trimming is 0.15 (15% from each end of the sample)
    # sig_level for flagging significance, but p-value is the main result.
    qlr_results = qlr_test(y_data, X_data, trim=0.15, sig_level=0.05, return_f_stats_series=True)

    # --- 3. Print Results ---
    print("\nQLR Test Results:")
    print(f"  Maximum F-statistic: {qlr_results['max_f_stat']:.4f}")
    print(f"  Estimated Breakpoint Index: {qlr_results['breakpoint']}") # 0-indexed
    print(f"  P-value: {qlr_results['p_value']:.4f}")
    print(f"  Significant at 5% level: {qlr_results['significant']}")
    print(f"  Approx. 5% Critical Value (for trim=0.15): {qlr_results['approx_critical_value']:.4f}")
    print(f"  Number of observations: {qlr_results['n_observations']}")
    print(f"  Number of parameters (k): {qlr_results['n_parameters']}")


    # --- 4. Plotting example F-stats (Optional) ---
    # Requires matplotlib
    if 'f_stats' in qlr_results and qlr_results['f_stats'] is not None:
        try:
            plt.figure(figsize=(10, 6))
            plt.plot(qlr_results['tested_indices'], qlr_results['f_stats'], marker='.', linestyle='-')
            plt.axvline(qlr_results['breakpoint'], color='r', linestyle='--', 
                        label=f"Estimated Breakpoint: {qlr_results['breakpoint']}")
            if not np.isnan(qlr_results['approx_critical_value']):
                plt.axhline(qlr_results['approx_critical_value'], color='g', linestyle=':', 
                            label=f"Approx. 5% CV: {qlr_results['approx_critical_value']:.2f}")
            
            plt.title('QLR F-statistics across potential breakpoints')
            plt.xlabel('Breakpoint Index')
            plt.ylabel('F-statistic')
            plt.legend()
            plt.grid(True)
            plt.show()
        except ImportError:
            print("\nMatplotlib not installed. Skipping plot.")
        except Exception as e:
            print(f"\nCould not generate plot: {e}")
    else:
        print("\nF-statistic series not returned, skipping plot.")

if __name__ == "__main__":
    run_example()

    # Example similar to the original script's __main__ for quick check
    print("\n--- Running original script's example structure ---")
    n_example = 100
    break_pt_example = 40 # True breakpoint
    # Create X with an intercept and a trend
    X_main_example = sm.add_constant(np.arange(n_example, dtype=float), prepend=True)
    
    beta_pre_ex = np.array([1.0, 0.5])
    beta_post_ex = np.array([5.0, -0.5]) # Clear break in intercept and trend
    errors_ex = np.random.normal(0, 2, n_example) # Increased noise
    y_main_example = np.concatenate((X_main_example[:break_pt_example] @ beta_pre_ex,
                                X_main_example[break_pt_example:] @ beta_post_ex)) + errors_ex

    print(f"Running QLR test on synthetic data (original example type) with break at index {break_pt_example}...")
    qlr_results_main_ex = qlr_test(y_main_example, X_main_example, trim=0.15, sig_level=0.05)

    print("\nOriginal Example QLR Results:")
    print(f"  Max F-stat: {qlr_results_main_ex['max_f_stat']:.4f}")
    print(f"  Breakpoint Index: {qlr_results_main_ex['breakpoint']}")
    print(f"  P-value: {qlr_results_main_ex['p_value']:.4f}")
    print(f"  Significant (0.05): {qlr_results_main_ex['significant']}")