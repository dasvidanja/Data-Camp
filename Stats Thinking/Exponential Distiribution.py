'''The Exponential distribution describes the waiting times between rare events, and Secretariat (fastest horse in history) is rare!'''

#Two successive Poisson Events
def successive_poisson(tau1, tau2, size=1):
    """Compute time for arrival of 2 successive Poisson processes."""
    # Draw samples out of first exponential distribution: t1
    t1 = np.random.exponential(tau1,size=tau1)

    # Draw samples out of second exponential distribution: t2
    t2 = np.random.exponential(tau2,size=tau2)

    return t1 + t2

# Draw samples of waiting times: waiting_times
waiting_times= successive_poisson(764, 715,100000)

# Make the histogram
_= plt.hist(waiting_times, bins= 100, normed = True, histtype='step')


# Label axes
_=plt.xlabel('Games played')
_=plt.ylabel('Probability of rare events')


# Show the plot
_=plt.show()
