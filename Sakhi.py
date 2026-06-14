antigravity-backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application startup & routing
│   ├── config.py               # Settings and configuration management (Pydantic Settings)
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── api.py           # V1 router registration
│   │   │   └── endpoints/
│   │   │       ├── __init__.py
│   │   │       └── sos.py       # SOS trigger controller
│   │   └── deps.py             # FastAPI dependency injections (DB sessions, mock clients)
│   ├── core/
│   │   ├── __init__.py
│   │   └── location.py         # Haversine distance calculation algorithm
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py             # SQLAlchemy Base class
│   │   ├── models.py           # SQL Database models (User, AlertHistory)
│   │   └── session.py          # Async engine and database session generator
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── sos.py              # Pydantic validation schemas (SOSPayload, SOSResponse)
│   └── services/
│       ├── __init__.py
│       ├── firebase.py         # Mocked Firebase Admin SDK service
│       └── twilio.py           # Mocked Twilio SMS service
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # Pytest fixtures and mock database overrides
│   └── test_sos.py             # Integration and unit tests for the SOS endpoint
├── requirements.txt            # Project dependencies
└── README.md                   # Setup and usage guide