---
title:  PET
created: Thursday 27th July 2023 16:39
aliases: 
tags: pet
---
Privacy-enhancing technologies are technologies that embody fundamental data protection principles by minimizing personal data use, maximizing data security, and empowering individuals. PETs allow online users to protect the privacy of their personally identifiable information, which is often provided to and handled by services or applications

| Tool                                                   | Description                                                                   |
| ------------------------------------------------------ | ----------------------------------------------------------------------------- |
| [SecretFlow](https://github.com/secretflow/secretflow) | A unified framework for privacy-preserving data analysis and machine learning |

# Data Encryption

[Data encryption](https://www.mimecast.com/content/data-encryption/) is the process of converting information into a secret code (or cipher) to hide its meaning. Using a specialized encryption algorithm, companies can encode their data so it becomes indecipherable to anyone but the intended recipient, who relies on another encryption algorithm on their end to decode the information.

## Data in Transit

Data in transit’s data **that is moving from one location to another**. This includes information traveling via email, collaboration platforms like Microsoft Teams, instant messengers like WhatsApp, and virtually any public communications channel. **Certificates TLS, security frameworks.**
## Data at Rest

Data at rest refers to **inactive data, meaning it’s not moving between devices or networks**. Because this information tends to be stored or archived, it’s less vulnerable than data in transit. That said, any information companies keep close to their chests is also seen as more valuable by hackers, making it a target for external attacks. **Encryption DDBB, firewalls, security software.**
## Data in Use

Data is in use when **it’s accessed or consumed by an employee or corporate application**. Whether it’s being read, processed or modified, data is at its most vulnerable in this state because it’s directly accessible to an individual, making it susceptible to attack or human error – both of which can have significant consequences. **PETs technologies, strong passwords, authentication and permission for data access.**

# Cryptographic algorithms

## HE

**Homomorphic Encryption:** [Homomorphic encryption](https://research.aimultiple.com/homomorphic-encryption/) is an encryption method that enables computational operations on encrypted data. It generates an encrypted result which, when decrypted, matches the result of the operations as if they had been performed on unencrypted data (i.e. [plaintext](https://en.wikipedia.org/wiki/Plaintext)). This enables encrypted data to be transfered, analyzed and returned to the data owner who can decrypt the information and view the results on the original data. Therefore, companies can share sensitive data with third parties for analysis purposes. It is also useful in applications that hold encrypted data in cloud storage. Some common types of homomorphic encryption are:

- **Partial homomorphic encryption:** can perform one type of operation on encrypted data, such as only additions or only multiplications but not both.
- **Somewhat homomorphic encryption:** can perform more than one type of operation (e.g. addition, multiplication) but enables a limited number of operations.
- **Fully homomorphic encryption:** can perform more than one type of operation and there is no restriction on the number of operations performed.

## SMPC

**Secure multi-party computation (SMPC):** [Secure multi-party computation](https://research.aimultiple.com/secure-multi-party-computation/) is a subfield of homomorphic encryption with one difference: users are able to compute values from multiple encrypted data sources. Therefore, machine learning models can be applied to encrypted data since SMPC is used for a larger volume of data.

- [MPSPDZ](https://github.com/data61/MP-SPDZ)
## DP

**Differential privacy:** [Differential privacy](https://research.aimultiple.com/differential-privacy/) protects from sharing any information about individuals. This cryptographic algorithm adds a “[statistical noise](https://whatis.techtarget.com/definition/statistical-noise)” layer to the dataset which enables to describe patterns of groups within the dataset while maintaining the privacy of individuals.
## ZKP

 **Zero-knowledge proofs (ZKP):** [Zero-knowledge proofs](https://research.aimultiple.com/zero-knowledge-proofs/) uses a set of cryptographic algorithms that allow information to be validated without revealing data that proves it.

# Data masking techniques

Some privacy enhancing technologies are also [data masking techniques](https://research.aimultiple.com/data-masking/) that are used by businesses to protect sensitive information in their data sets.

- **Obfuscation:** This one is a general term for data masking that contains multiple methods to replace sensitive information by adding distracting or misleading data to a log or profile.
- **Pseudonymization:** Identifier fields (fields that contain information specific to an individual) are replaced with fictitious data such as characters or other data. Pseudonymization is [frequently used by businesses to comply with GDPR.](https://research.aimultiple.com/data-masking/#how-does-gdpr-promote-data-masking)
- **Data minimisation:** Collecting minimum amount of personal data that enables the business to provide the elements of a service.
- **Communication anonymizers:** Anonymizers replace online identity (IP address, email address) with disposal/one-time untraceable identity.

# Artificial Intelligence (AI) & ML algorithms



- **Synthetic data generation:** [Synthetic data](https://research.aimultiple.com/synthetic-data/) is an artificially created data by using different algorithms including ML algorithms. If you are interested in privacy-enhancing technologies because you need to transform your data into a testing environment where third-party users have access, [generating synthetic data](https://research.aimultiple.com/synthetic-data-generation/) that has the same statistical characteristics is a better option.
- **Federated learning:** This is a machine learning technique that trains an algorithm across multiple [decentralized edge devices](https://research.aimultiple.com/edge-analytics/) or servers holding local data samples, without exchanging them. With the decentralization of servers, users can also achieve data minimization by reducing the amount of data that must be retained on a centralized server or in cloud storage.

---
# References

[1]: [Privacy Enhancing Technologies & Benefits](https://research.aimultiple.com/privacy-enhancing-technologies/)
