total = 52

# Probability of drawing a king
p_a = 4 / total

# Probability of drawing a face card
p_b = 12 / total

# Probability of drawing a face card given it is a king
p_b_given_a = 1

# Bayes' Theorem
p_a_given_b = (p_b_given_a * p_a) / p_b

print("Probability of drawing a King:", p_a)
print("Probability of drawing a Face Card:", p_b)
print("Probability of King given Face Card:", p_a_given_b)
