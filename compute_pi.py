# compute_pi.py
def compute_pi(n):
    pi = 2
    for i in range(1, n):
        pi *= 4 * i ** 2 / (4 * i ** 2 - 1)
    return pi


pi = compute_pi(1000)
display(f"π is approximately {pi:.3f}", target="pi_out")
