# health-monitor



### Build infrastructure

1. `cd infrastructure`
2. `python3 -m venv venv`
3. `source venv/bin/activate`
4. `python3 build.py --email some@email.com`


### Destroing infrastructure

1. `python3 destroy.py`




### MISC 
#### Generating CSR
```
openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:2048
openssl req -new -key private.pem -out csr.pem -sha256
```