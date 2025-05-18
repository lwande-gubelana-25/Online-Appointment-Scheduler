# Project Roadmap

This document outlines the future direction and planned features for the Online Appointment Scheduler.

---

## Completed

- User registration and login
- Book, cancel, and reschedule appointments
- Role-based user access (admin, user)
- Unit tests with Pytest
- CI/CD pipeline using GitHub Actions

---

## In Progress

- Admin dashboard for managing users and appointments
- In-memory repository layer using DI
- RESTful API with FastAPI
- Appointment status tracking (pending, confirmed, cancelled)

---

## Future Plans

- [ ] Integrate Redis caching to improve appointment lookup speed
- [ ] Add email/SMS notifications using Twilio or SMTP
- [ ] Dockerize the application for deployment
- [ ] OpenAPI documentation export (JSON/YAML)
- [ ] Multi-language support (English, isiZulu, Afrikaans, etc.)
- [ ] Allow recurring appointments (weekly/monthly)
- [ ] OAuth 2.0 / Google login support
- [ ] Analytics dashboard (number of appointments/booked per day)
