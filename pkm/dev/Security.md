---
title:  Security
created: Tuesday 5th March 2024 12:32
aliases: 
tags: 
---

| Tool                                               | Description                                                              |
| -------------------------------------------------- | ------------------------------------------------------------------------ |
| [Falco](https://github.com/falcosecurity/falco)    | Cloud native runtime security tool for Linux OS                          |
| [ffuf](https://github.com/ffuf/ffuf)               | Fast web fuzzer written in Go                                            |
| [massdns](https://github.com/blechschmidt/massdns) | A high-performance DNS stub resolver for bulk lookups and reconnaissance |
| [gobuster](https://github.com/OJ/gobuster)         | Directory/File, DNS and VHost busting tool written in Go                 |
# TLS

**TLS** is a cryptographic protocol that provides end-to-end security of data sent between applications over the Internet. It is mostly familiar to users through its use in secure web browsing, and in particular the padlock icon that appears in web browsers when a secure session is established. However, it can and indeed should also be used for other applications such as e-mail, file transfers, video/audioconferencing, instant messaging and voice-over-IP, as well as Internet services such as DNS and NTP.

## SSL certificate

SSL can only be implemented by websites that have an [SSL certificate](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/) (technically a "TLS certificate"). An SSL certificate is like an ID card or a badge that proves someone is who they say they are. SSL certificates are stored and displayed on the Web by a website's or application's server. [[OpenSSL]] provides an implementation for those protocols and is often used as the reference implementation for any new feature.

One of the most important pieces of information in an SSL certificate is the website's public key. The **public key** makes encryption and authentication possible. A user's device views the public key and uses it to establish secure encryption keys with the web server. Meanwhile the web server also has a private key that is kept secret; the private key decrypts data encrypted with the public key.

**Certificate authorities** (CA) are responsible for issuing SSL certificates.

