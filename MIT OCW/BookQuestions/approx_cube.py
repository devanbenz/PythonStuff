cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0

while abs(guess**3  - cube) >= epsilon and guess <= cube:
  guess += increment
  num_guesses += 1

print('Number of guesses: ', num_guesses)

if abs(guess**3 - cube) >= epsilon:
  print('With given properties cube cannot be approximated.')
else:
  print(guess, 'is close to the cube root of' , cube)

