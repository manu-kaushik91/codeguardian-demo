# CodeGuardian AI Hackathon Edition

Multi-agent AI code review platform.

Architecture:
GitHub -> FastAPI -> Agents -> Risk Summary

Deploy:
1. docker build -t codeguardian .
2. docker run -p 8000:8000 codeguardian
