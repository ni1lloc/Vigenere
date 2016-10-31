#!usr/bin/python

#a simple encoder/decoder for Vigenere code
#by m1lloc


def decrypt(pwd, key):
	kl = []
	for i in range(len(key)):
		kl.append(ord(key[i])-ord('a'))

	tl = []
	for i in range(len(pwd)):
		t = ord(pwd[i])-ord('a')
		t = t - kl[i%len(key)]
		t = t % 26
		tl.append(chr(t+ord('a')))
	return tl

def encrypt(ori, key):
	kl = []
	for i in range(len(key)):
		kl.append(ord(key[i])-ord('a'))
	tl = []
	for i in range(len(ori)):
		t = ord(ori[i])-ord('a')
		t = t + kl[i%len(key)]
		t = t % 26
		tl.append(chr(t+ord('a')))
	return tl
