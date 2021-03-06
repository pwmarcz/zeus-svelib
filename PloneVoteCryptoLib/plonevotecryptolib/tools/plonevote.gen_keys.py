# -*- coding: utf-8 -*-
#
#  plonevote.gen_keys.py : A tool to generate new private/public key pair.
#
#  Part of the PloneVote cryptographic library (PloneVoteCryptoLib)
#
#  Originally written by: Lazaro Clapp
#
# ============================================================================
# LICENSE (MIT License - http://www.opensource.org/licenses/mit-license):
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# ============================================================================

from __future__ import absolute_import
from __future__ import print_function
import sys
import getopt

from plonevotecryptolib.EGCryptoSystem import EGCryptoSystem, EGStub
from plonevotecryptolib.PVCExceptions import *

def print_usage():
	"""
	Prints the tool's usage message
	"""
	print("""USAGE:
		  
		  plonevote.gen_keys.py --cryptosys=cryptosystem.pvcryptosys --private=private_key.pvprivkey --public=public_key.pvpubkey
		  
		  plonevote.gen_keys.py (--help|-h)
		  
		  Arguments can be given in any order. All arguments are mandatory.
		  	
		  	--cryptosys=cryptosystem.pvcryptosys : The PloneVote cryptosystem to use for generating the key pair.
		  	
		  	--private=private_key.pvprivkey  : The file in which to store the private key.
		  	
		  	--public=public_key.pvpubkey  : The file in which to store the public key.
		  	
		  	--help|-h : Shows this message
		  """)
	
def run_tool(cryptosystem_filename, privkey_filename, pubkey_filename):
	"""
	Runs the plonevote.gen_keys tool and generates a new private and public key.
	"""
	# Load the cryptosystem
	try:
		cs_stub = EGStub.from_file(cryptosystem_filename)
	except InvalidPloneVoteCryptoFileError as e:
		print("Invalid cryptosystem file (%s): %s" % \
			(cryptosystem_filename, e.msg))
		sys.exit(2)
	
	if(not cs_stub.is_secure()):
		print("The security (bit size) of the cryptosystem described by %s " \
			  "is lower than the minimum allowed by the current " \
			  "PloneVoteCryptoLib configuration.")
		sys.exit(2)
	
	try:
		cryptosystem = cs_stub.to_cryptosystem()
	except ParameterError as e:
		print("Invalid cryptosystem file (%s): %s" % \
			(cryptosystem_filename, e.msg))
		sys.exit(2)
	
	# Generate the key pair
	key_pair = cryptosystem.new_key_pair()
	
	# Save the keys
	key_pair.private_key.to_file(privkey_filename)
	key_pair.public_key.to_file(pubkey_filename)
		

def main():
	"""
	Parses command line options and runs the tool
	"""
    # parse command line options
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'n', ['cryptosys=', 'private=', 'public='])
	except getopt.error as msg:
		print(msg)
		print("for help use --help")
		sys.exit(2)
	
	# process options
	cryptosystem_filename = privkey_filename = pubkey_filename = None
	for o, a in opts:
		if o in ("-h", "--help"):
			print_usage()
			sys.exit(0)
		elif o == "--cryptosys":
			cryptosystem_filename = a
		elif o == "--private":
			privkey_filename = a
		elif o == "--public":
			pubkey_filename = a
		else:
			print("ERROR: Invalid argument: %d=%d\n" % (o, a))
			print_usage()
			sys.exit(2)
	
	# All arguments are mandatory (so that the user must explicitly tell the 
	# tool where to store the keys, avoiding confusion between the private and 
	# public keys)
	for option in [cryptosystem_filename, privkey_filename, pubkey_filename]:
		if(option == None):
			print_usage()
			sys.exit(2)			
    
    # Run cryptosystem generation
	run_tool(cryptosystem_filename, privkey_filename, pubkey_filename)

if __name__ == "__main__":
    main()
