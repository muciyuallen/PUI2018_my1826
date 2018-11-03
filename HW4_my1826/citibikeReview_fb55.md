# IDEA
ok, but you should spend a few words saying what motivates it and why it is interesting!

# Null Hypothesis:

The average duration of biketrips taken by women is not significantly different from that by men.

No: this would be the NH corresponding to "man take longer or shorter trips than women". your NH should be 
"The average duration of biketrips taken by women is longer or the same from that by men."

# DATA 

the data is processed fine to support the question

#TEST 

this is a difference between means of samples, so the t test would work. however the distributions are not Gaussian. 
the t-test assumes Gaussianity and your distributions are not Gaussian. a non parametric test for difference of means is the Mann-Whitney U test (https://www.healthknowledge.org.uk/public-health-textbook/research-methods/1b-statistical-methods/parametric-nonparametric-tests)
since the samples is large, the t-test may be ok 

here is a list of assumptions the t-test makes https://www.investopedia.com/ask/answers/073115/what-assumptions-are-made-when-conducting-ttest.asp
