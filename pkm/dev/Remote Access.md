---
title:  Remote Access
created: Saturday 25th January 2025 12:21
aliases: 
tags: 
---
**Remote access** is a networked computing methodology enabling users to access computer systems, applications, or data from a geographically distant location through secure, authenticated communication channels. It involves connecting to a network infrastructure via encrypted protocols, allowing seamless interaction with resources regardless of physical proximity.

Key Technical Components:

- Authentication mechanisms
- Secure communication tunnels
- Network access control
- Encrypted data transmission
- Device and user verification protocols

| Tool                                           | Description                                        |
| ---------------------------------------------- | -------------------------------------------------- |
| [KasmVNC](https://github.com/kasmtech/KasmVNC) | Modern VNC Server and client, web based and secure |
# Transmission protocols

## TCP (Transmission Control Protocol)

- Connection-oriented protocol
- Ensures reliable, ordered data delivery
- Performs error checking and retransmission
- Establishes guaranteed packet transmission

## UDP (User Datagram Protocol)

- Connectionless protocol
- Faster, lightweight data transmission
- No guaranteed delivery
- Minimal error checking
- Ideal for real-time applications

## HTTPS (Secure HTTP)

- Encrypts data during transmission
- Uses SSL/TLS for security
- Prevents data interception
- Authenticates website identity

## IP (Internet Protocol)

- Responsible for addressing and routing
- Defines packet structure
- Manages data packet fragmentation
- Enables cross-network communication

## SMTP (Simple Mail Transfer Protocol)

- Email transmission protocol
- Manages email routing
- Defines message transfer rules
- Supports global email communication

## FTP (File Transfer Protocol)

- Standard network protocol for file transfer
- Enables file upload/download
- Supports authentication
- Separate control and data connections

## SSH (Secure Shell)

- Encrypted network protocol
- Secure remote system access
- Supports secure file transfers
- Provides command-line interface

# Protocols for Remote Access

There are several key protocols used for remote access:
## 1. Virtual Private Network (VPN)

- **Purpose**: Creates a secure, encrypted tunnel between a remote device and the corporate network
- **Types**:
    - **IPsec VPN**: Provides security at the IP layer
    - **Point-to-Point Tunneling Protocol (PPTP):**  PPTP has fallen out of favor due to identified security vulnerabilities. It's recommended to opt for more modern and secure alternatives
    - **Remote Access Services (RAS):** A RAS setup empowers users to securely connect to a corporate network from remote locations, either through traditional dial-up connections or via a VPN
    - **SSL/TLS VPN**: Uses web browsers for secure access
    - **OpenVPN**: Open-source solution with strong encryption
## 2. Remote Desktop Protocol (RDP)

- **Developed by Microsoft**
- Allows users to connect to another computer over a network
- Provides full graphical interface of the remote system
- Commonly used in Windows environments for remote administration and access
## 3. Secure Shell (SSH)

- Cryptographic network protocol for secure data communication
- Primarily used for command-line access to remote systems
- Provides strong encryption and authentication
- Widely used in Unix/Linux environments
## 4. Terminal Services/Remote Desktop Protocol (RDP)

- Microsoft's comprehensive remote access solution (a proprietary)
- Allows multiple users to access Windows applications and desktops simultaneously
- Supports various client devices and platforms
## 5. Virtual Network Computing (VNC)

- Platform-independent remote desktop sharing system
- Allows viewing and controlling another computer's screen
- Open-source and supports multiple operating systems
## 6. WebDAV (Web Distributed Authoring and Versioning)

- Extension of HTTP for collaborative document editing
- Allows users to edit and manage files on remote web servers
- Often used for file sharing and collaborative work
## 7. Citrix Remote Access Solutions

- Provides advanced remote access technologies
- Includes virtual desktop infrastructure (VDI)
- Supports complex enterprise remote access requirements
