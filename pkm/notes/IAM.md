---
title:  AIM
created: Tuesday 20th February 2024 19:09
aliases: 
tags: 
---
Identity and Access Management (IAM) provides fine-grained access control across all of AWS. With IAM, you can control access to services and resources under specific conditions. Use IAM policies to manage permissions for your workforce and systems to ensure [least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege). 
### Tips

- The root account is the email address you used to sign up for AWS. The **root account** has **full administrative access** to AWS. For this reason, it is important to secure this account.
- Always create an **MFA** for good security.
- Create an **admin** group and add users to the group.
- If for some reason you are stuck in a scenario where you have policies mapped against you that have both of the effect’s for the same resource, the **Deny will always win**.
- The least privilege model is a common security suggest to **only grant the access level required to perform the necessary function, and no more**.
- **IAM is Universal**: it does not apply to regions at this time.
- **The Root Account**: this is the account created when you first set up your AWS account and it has complete admin access. Secure it as soon as possible and **do not** use it to log in day to day.
- **New Users**: no permissions when first created.
- **Access key ID and secret key are not the same as username and pass.**
- You only get to **view these one** (Access and secret key).
- **Always set up password rotations**.
- **IAM Federation**: you can combine your existing user with AWS. (LDAP)
- **Identity Federation**: uses SAML standard, which is Active Directory.
### Usage
#### Resources

**Resources** are the entities that you create in AWS. This can include thing’s like an S3 bucket, an S3 Object, or a DynamoDB tables. All resources in AWS are represented by something called an **ARN** or **Amazon Resource Name**. You’ve probably seen one of these identifiers before, they look a little like this: `arn:aws:s3:::test-website-awssimplified`.
#### Actions

**Actions** are the operations that users attempt to perform on resources. For example, if I created a lambda function, I may want to update its configuration. In order to do that, I need to use an API called `lambda:UpdateFunctionConfiguration`.
#### Policy / Policy Document

The heart of AWS IAM is the **Policy**. IAM policies refer specific JSON documents that define user permissions to access a resource. In other words, authorization to perform an **Action** is determined by whether or not the user has the appropriate **Policy Document** with associated permissions.
### Control

#### Groups

IAM **groups** are simply a collection of AWS Users. They are an important organizational toolkit to help you assign similar permissions to a collection of users at once. Using groups, you can associate users added to the group with a default IAM policy. Check out the documentation [here](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html).
#### Roles

**Roles** are similar to users in the sense that we can attach IAM policies to them. However, unlike Users, Roles are meant to **grant short term access to resources**. In other words, if I want to grant short term access to a user to provide a certain job function, say as an administrator, I may grant them the ability to **assume** a specific role. In doing so, the user will have all permissions defined under the assumed rule’s policy document. Roles can be used by many different users and at once if necessary.

Roles can be assumed by both users and other AWS services. For instance, when creating a Lambda function, we need to specify a **Role** that the Lambda function will use. If our function needs to access DynamoDB for example, I will need to add DynamoDB specific **Actions** to the role’s policy document.

#### Trust Relationships

**Trust Relationships** are not so much a core concept of IAM, but they are a source of problems that many developers run into which is why I think they’re worth discussing.

**Trust Relationships** allow us to create **Roles** that enable users from a DIFFERENT AWS account to temporarily gain access to it. For instance, consider an example like we have one account with a DynamoDB table, and a user from a different account wanting to get access to it.

- [[Enable an IAM User or IAM Role to access an EKS cluster]]
- [[Cross-Account Access in the AWS Management Console]]