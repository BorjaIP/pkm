# Personal Knowledge Management (PKM)

This repository contains my personal PKM (Personal Knowledge Management) system. A PKM is a method of organizing, storing, and retrieving knowledge to enhance learning and productivity. For more information, you can explore the following resources:
- [What is a PKM?](https://en.wikipedia.org/wiki/Personal_knowledge_management)
- [Zettelkasten Method](https://zettelkasten.de/posts/overview/): A note-taking and knowledge management method that emphasizes connections between ideas.

## Focus Areas
This PKM is primarily focused on:
- **Tech Stack**: Notes and resources related to programming, tools, and frameworks.
- **Computer Science**: Concepts, algorithms, and systems.
- **Miscellanea**: Other topics of interest.

## Quartz
This PKM uses [Quartz](https://quartz.jzhao.xyz/) to generate a markdown-based content website. Quartz provides a clean and efficient way to publish and navigate through markdown notes.

## Development Setup

To serve the Quartz website locally with live updates, use the following command:

```bash
# Dev Setup
npx quartz build --serve --watch --concurrency 10
```

## Building Docker

To build and edit the PKM locally using Docker:

1. Build the Docker container:

```bash
docker build -t quartz .
```

2. Run the container:

```bash
docker run --rm --name quartz -p 8080:8080 quartz:latest
```

3. Access the Quartz website at http://localhost:8080.

## Editing with DevContainer

This repository includes a DevContainer configuration to simplify the development environment setup. To use it:

1. Open the repository in Visual Studio Code.
2. Install the Dev Containers extension if not already installed.
3. Reopen the folder in the DevContainer:
   - Select Dev Containers: Reopen in Container.
4. Once the container is built and running, you can edit the PKM files directly in the containerized environment.
5. Use the integrated terminal to run commands like npx quartz build or docker run as needed.
