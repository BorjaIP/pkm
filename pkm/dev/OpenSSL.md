---
title:  OpenSSL
created: Monday 1st May 2023 17:01
aliases: 
tags: ssl
---
| Tool                                                                 | Description                                             |
| -------------------------------------------------------------------- | ------------------------------------------------------- |
| [EJBCA](https://www.ejbca.org/)      | Open-source public key infrastructure (PKI)       |
| [KeyStore Explorer](https://keystore-explorer.org/index.html)| Replacement for the Java command-line utilities keytool |

## Self sign certificate

- Create new self-signed certificate.

```bash
openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem
```

- Verify CA

```bash
openssl x509 -noout -text -in ca/public/name.crt 
#output
 X509v3 Basic Constraints: critical
                CA:TRUE
```

- Verify certificate

```bash
openssl verify -CAfile ca/public/name.crt k8s/ca-cert.pem
```

- Display certificate text

```bash
openssl x509 -in /etc/ssl/certs/name.crt -text 
```

- Display CSR information

```bash
openssl req -noout -text -in <name>.req
```

- Convert crt  --> pem

```bash
openssl x509 -in k8s/ca-key.crt -out k8s/ca-key.pem -outform PEM
```

- Extract CSR from certificate

```bash
openssl x509 -x509toreq -in name.crt -signkey name.key -out name.csr
```

## Create certificates

RootCA
 - Root Private key
 - Root Certificate
 - CSR (Certificate Signing Request) --> .req o .csr

1. Create folder

```bash
mkdir ca/<name>
```

2. Create Key

```bash
openssl genrsa -out ca/<name>.key 2048
```

3. Create CSR

```bash
openssl req -new -key ca/<name>.key -out ca/<name>.req
```

```bash
openssl req -new -key ca/<name>.key -out ca/<name>.req -config ca/<name>.cnf
```

4. Verify Sign with the key

```bash
openssl req -verify -in ca/<name>.req -text -noout
```

5. Sign CSR with the CA (this automatically add new line into .txt database)

```bash
openssl ca -config ca/node.cnf -out ca/issued/name.crt -infiles ca/<name>.req
```

```bash
openssl ca -config ca/node.cnf -out ca/issued/name.crt -extensions v3_req -infiles ca/<name>.req
```

6. Verify the certificate

```bash
openssl x509 -noout -text -in ca/issued/name.crt
```

7. Verify the connection

```bash
openssl s_client -connect <name>:443 -CAfile /etc/ssl/certs/<ca-name>.crt
echo | openssl s_client -connect redhat.com:443 2>/dev/null | openssl x509 -noout -ext subjectAltName
```

### Intermediate CA

1. Create intermediate CA

```bash
openssl genrsa -out intermediate/private/intermediate.key 4096
```

2. Modify permissions

```bash
chmod 400 intermediate/private/intermediate.key
```

3. Create CSR (from cnf)

```bash
openssl req -config intermediate/intermediate.cnf -new -sha256 -key intermediate/private/intermediate.key -out intermediate/certificates/intermediate.csr
```

4. Sign CSR with the CA (this automatically add new line into .txt database)

```bash
openssl ca -config node.cnf -extensions v3_intermediate_ca v3_req -notext -md sha256 -in intermediate/certificates/intermediate.csr -out intermediate/certificates/intermediate.crt
```

5. Modify permissions

```bash
chmod 444 intermediate/public/intermediate.crt
```

6. Verify intermediate CA

```bash
openssl x509 -noout -text -in intermediate/certificates/intermediate.crt
openssl verify -CAfile public/<ca-name>.crt intermediate/public/intermediate.crt
```

## Keytool

- Convert p12 --> jks

```bash
keytool -importkeystore -srckeystore certificate.p12 -srcstoretype pkcs12 -destkeystore cert.jks
```

- List certificates inside jks

```bash
keytool -list -keystore generic.jks -v
```

- List CA

```bash
keytool -list -keystore $JAVA_HOME/lib/security/cacerts -storepass changeit
```

## P12

- Convert crt --> .p12

```bash
openssl pkcs12 -export -clcerts -inkey client.key -in client.crt -out client.p12 -name "MyKey"
```

- See content of a .p12

```bash
openssl pkcs12 -info -nodes -in yourfilename.p12 -passin pass:password
```

- List .p12

```bash
keytool -list -v -keystore test.p12 -storepass password -storetype PKCS12
```

- List jks

```bash
keytool -v -list -keystore test.jks -storepass password
```

- Extract certs

```bash
openssl pkcs12 -in path.p12 -out newfile.crt.pem -clcerts -nokeys
```

- Extract keys

```bash
openssl pkcs12 -in path.p12 -out newfile.key.pem -nocerts -nodes
```

## CNF

- [Openssl.cnf example](https://github.com/openssl/openssl/blob/master/apps/openssl.cnf)

User `critical` for force to in this case load the custom CA.

```conf
[v3_req]
subjectAltName                  = critical, @alt_names
basicConstraints                = critical, CA:FALSE
keyUsage                        = critical, digitalSignature, keyEncipherment, keyAgreement
extendedKeyUsage                = critical, serverAuth, clientAuth
subjectKeyIdentifier            = critical, hash
authorityKeyIdentifier          = critical, keyid, issuer
```