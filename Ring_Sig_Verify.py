import os, hashlib, random, Crypto.PublicKey.RSA
import sys
from functools import reduce
import string

class ring:
    def __init__(self, k, L=1024):
        self.k = k
        self.l = L
        self.n = len(list(k))
        self.q = 1 << (L - 1)

    def verify(self, m, X):
        self.permut(m)
        def _f(i):
            return self.g(X[i+1], self.k[i].e, self.k[i].n)
        y = list(map(_f, list(range(len(X)-1))))
        def _g(x, i):
            return self.E(x^y[i])
        r = reduce(_g, list(range(self.n)), X[0])
        return r == X[0]

    def permut(self, m):
        self.p = int(hashlib.sha1(m.encode()).hexdigest(),16)
   #     sha1(s.encode(encoding)).hexdigest()

    def E(self, x): 
        msg = '%s%s' % (x, self.p)
        return  int(hashlib.sha1(msg.encode()).hexdigest(),16)

    def g(self, x, e, n):
        q, r = divmod(x, n)
        if ((q + 1) * n) <= ((1 << self.l) - 1):
            rslt = q * n + pow(r, e, n)
        else:
            rslt = x
        return rslt

size = 4

E_ID = open("/Users/sonipriyapaul/Downloads/E_ID.txt","r")
Signed = open("/Users/sonipriyapaul/Downloads/Signed.txt","r")

data = E_ID.read()
signature = Signed.read()

#signature.translate(str.maketrans('', '', string.punctuation))
signature = signature.replace('[','')
signature = signature.replace(']','')
signature = signature.replace(',','')
signature = signature.replace(' ','')

signature = int(float(signature))


def _rn(_):
  return Crypto.PublicKey.RSA.generate(1024, os.urandom)

key = list(map(_rn, list(range(size))))
r = ring(key)

for i in range(size):
    if (i==1):
        print("Ok")
      #print(("Signature is", s1))
        #print(("Signature verified:",r.verify(data,int(float(signature)))))
        


E_ID.close()
Signed.close()
