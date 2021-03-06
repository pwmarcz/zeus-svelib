# -*- coding: utf-8 -*-
#
# ============================================================================
# About this file:
# ============================================================================
#
#  ThresholdEncryptionCommitment.py : 
#  Represents a trustee's commitment towards a particular threshold encryption 
#  scheme.
#
#  The commitments of all trustees can be verified collaborativelly and used to 
#  set-up a threshold encryption scheme.
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

class ThresholdEncryptionCommitment:
	"""
	Represents a trustee's commitment towards a particular threshold encryption 
	scheme.
	
	Each trustee must create a commitment and share it with all other trustees 
	(can be done publicly). The following attributes describe the structure 
	of a commitment. For information about how commitments are created and used 
	to set-up a threshold encryption scheme, please look into the  
	ThresholdEncryptionSetUp class and its documentation.
	
	Attributes:
		cryptosystem::EGCryptoSystem --The cryptosystem used by this commitment.
							Only commitments based on the same cryptosystem are 
							compatible with one another for generating the same 
							threshold encryption scheme.
		num_trustees::int	-- Total number of trustees in the threshold scheme.
							   (the n in "k of n"-decryption)
		threshold::int	-- Minimum number of trustees required to decrypt 
						   threshold  encrypted messages. 
						   (the k in "k of n"-decryption)
		public_coefficients::long[] -- generator^{c_{i}} for each c_{i} 
							coefficient of the secret polynomial generated by 
							the trustee. Public coefficients are used to check 
							the distributed partial private keys and to generate
							 the threshold public key.
		encrypted_partial_private_keys::Ciphertext[]	--
							The partial private keys generated by the current 
							trustee for each other trustee (P_{i}(j), where i 
							is the current trustee, P_{i} their secret 
							polynomial, and j the trustee to whom the partial 
							private key is addressed).
							Each key is encrypted with the 1-to-1 (non 
							threshold) public key of the addressed trustee.
	"""
	
	def __init__(self, cryptosystem, num_trustees, threshold, 
				 public_coefficients, encrypted_partial_private_keys):
		"""
		Creates a new ThresholdEncryptionCommitment.
		
		Arguments:
			(see class attributes)
		"""
		self.cryptosystem = cryptosystem
		self.num_trustees = num_trustees
		self.threshold = threshold
		self.public_coefficients = public_coefficients
		self.encrypted_partial_private_keys = encrypted_partial_private_keys
