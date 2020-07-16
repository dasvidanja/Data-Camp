# Draw 100000 samples from Normal distribution with stds of interest: samples_std1, samples_std3, samples_std10
samples_std1= np.random.normal(20,1, size= 100000)

samples_std3= np.random.normal(20,3,size= 100000)

samples_std10= np.random.normal(20,10,size= 100000)

# Make histograms
_=plt.hist(samples_std1, normed=True, histtype='step', bins=100)
_=plt.hist(samples_std3, normed=True, histtype='step', bins=100)
_=plt.hist(samples_std10, normed=True, histtype='step', bins=100)

# Make a legend, set limits and show plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'))
plt.ylim(-0.01, 0.42)
plt.show()


# Generate CDFs
x_std1, y_std1 = ecdf(samples_std1)

x_std3, y_std3 = ecdf(samples_std3)

x_std10, y_std10 = ecdf(samples_std10)


# Plot CDFs
_=plt.plot(x_std1, y_std1, marker = ".", linestyle= 'none')
_=plt.plot(x_std3, y_std3, marker = ".", linestyle= 'none')
_=plt.plot(x_std10, y_std10, marker = ".", linestyle= 'none')

# Make a legend and show the plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'), loc='lower right')
plt.show()


#Theoretical CDF vs Data CDF (to check normality assumption)
# Compute mean and standard deviation: mu, sigma
mu= np.mean(belmont_no_outliers) 
sigma= np.std(belmont_no_outliers) 

# Sample out of a normal distribution with this mu and sigma: samples
samples = np.random.normal(mu, sigma, size = 10000)

# Get the CDF of the samples and of the data
x_theor, y_theor= ecdf(samples)
x,y = ecdf(belmont_no_outliers)


# Plot the CDFs and show the plot
_ = plt.plot(x_theor, y_theor)
_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.xlabel('Belmont winning time (sec.)')
_ = plt.ylabel('CDF')
plt.show()

#Calculate Probability
'''What are the chances of a horse matching or beating Secretariat's record?'''
# Take a million samples out of the Normal distribution: samples
samples = np.random.normal(mu, sigma, size= 1000000)

# Compute the fraction that are faster than 144 seconds: prob
prob = sum(samples<=144)/1000000

count=0
#Can use for loop as well
for x in samples:
    if x<=144:
        count +=1
prob2= count/1000000
print(prob2)
# Print the result
print('Probability of besting Secretariat:',prob)
