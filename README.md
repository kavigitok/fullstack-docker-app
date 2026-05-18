# Fullstack Docker App

A containerized full-stack demo application built with Flask, MySQL, Docker, Docker Compose, and GitHub Actions.

## Tech Stack

- Python Flask
- MySQL 8.0
- Docker
- Docker Compose
- GitHub Actions

## Architecture

Browser → Flask Backend → MySQL Database

## Project Structure

```text
.
├── backend
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
└── .github/workflows/docker-build.yml
