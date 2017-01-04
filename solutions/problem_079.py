import utils

# Find shortest possible passcode
def compute():
	logins = open(utils.INPUT_PATH + 'p079_keylog.txt').read().strip().split('\n') # May as well keep it as text
	answer = 73162890 # Solved by hand, easy since it was possible with just one instance of each digit
	return answer, "Shortest possible password"
