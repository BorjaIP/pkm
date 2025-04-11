---
title:  Vault
created: Saturday 29th April 2023 16:43
aliases: 
tags: ssl
---

- [Build your own certificate authority (CA)](https://developer.hashicorp.com/vault/tutorials/secrets-management/pki-engine)

Manage Secrets & Protect Sensitive Data with Vault

RootCA->Intermediate1->vault_intermediate

```bash
# The private key needs to be changed from pkcs8 to pkcs1 
# For Vault create the Root CA in pem format
openssl rsa -in pkcs8.key -out pkcs1.key -outform pem

# Delete encryptation for CA in Vault
openssl rsa -in ssl.key.encrypted -out ssl.key.decrypted

# Create pem with public and private keys
cat name.crt nameca.key.decrypted > <ca-name>.pem
```
