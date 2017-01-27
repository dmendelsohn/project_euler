import itertools
import utils

# Decrypt ciphertext
def compute(verbose=False):
	def is_valid_message(text, vocab):
		valid_words = [(word in vocab) for word in text.split(' ')]
		return valid_words.count(True) > valid_words.count(False) # True outnumber False 3:1 or better

	def is_valid_char(x): # Char is taken as int
		return x in [9, 10, 13] or 32 <= x < 127

	ctext = open(utils.INPUT_PATH + 'p059_cipher.txt').read().strip().split(',')
	ctext = list(map(int, ctext))  # Map cipher text to list of ascii values
	N = 3 # Key length
	possible_keys = [range(128)]*N
	for i in range(N): # For each character in key
		for j in range(i,len(ctext),3): # For each character in text encrypted by this part of key
			possible_keys[i] = [k for k in possible_keys[i] if is_valid_char(ctext[j]^k)]
	vocab = utils.get_vocab()
	for key in itertools.product(possible_keys[0], possible_keys[1], possible_keys[2]):
		ptext = ''.join(map(chr, [ctext[i]^key[i%len(key)] for i in range(len(ctext))]))
		if is_valid_message(ptext, vocab):
			if verbose:
				print("Key is %s" % (str(key),))
				print("Decrypted text is '%s'" % (ptext,))
			return sum(map(ord, ptext)), 'Sum of ASCII characters in plain text'
	return -1, 'No decryption found'
