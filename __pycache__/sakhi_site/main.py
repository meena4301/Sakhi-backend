import sys
import os
import math
import logging
from typing import List
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel, Field, field_validator

# విండోస్ పాత్ సమస్యలు రాకుండా ఉండటానికి సేఫ్టీ గార్డ్
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

logging.basicConfig(level=logging.INFO)

# --- ఇక్కడ మీ ప్రాజెక్ట్ పేరు "Sakhi" అని పక్కాగా మార్చాం ---
app = FastAPI(
    title="Sakhi Women Safety API",
    description="Backend API for Sakhi Women Safety Application (SOS Trigger & Alerts)",
    version="1.0.0"
)

# --- 1. DATA VALIDATION (SCHEMAS) ---
class SOSRequest(BaseModel):
    user_id: str
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    emergency_contact: str

    @field_validator('emergency_contact')
    @classmethod
    def validate_phone(cls, v: str) -> str:
        if not v.startswith('+') or len(v) < 10:
            raise ValueError('Phone number must start with +')
        return v

class SOSResponse(BaseModel):
    status: str
    message: str
    nearby_users_alerted: List[str]

# --- 2. MATHS LOGIC (HAVERSINE) ---
def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6371.0  # Earth radius in KM
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = (math.sin(delta_phi / 2) ** 2 +
         math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2)
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

# --- 3. MOCK SERVICES ---
async def mock_firebase_push(tokens: List[str]):
    logging.info(f"[FCM] Sending alerts to tokens: {tokens}")

async def mock_twilio_sms(to_number: str, msg: str):
    logging.info(f"[Twilio] SMS sent to {to_number}: {msg}")

# --- 4. MAIN API ENDPOINT ---
@app.post("/api/v1/sos/trigger", response_model=SOSResponse)
async def trigger_sos(payload: SOSRequest, background_tasks: BackgroundTasks):
    try:
        # Dummy Active Female Users (Testing Kosam)
        mock_users = [
            {"id": "user_sita", "lat": payload.latitude + 0.005, "lon": payload.longitude + 0.005, "token": "token1"},
            {"id": "user_geetha", "lat": payload.latitude + 0.5, "lon": payload.longitude + 0.5, "token": "token2"}
        ]

        nearby_users = []
        tokens_to_alert = []

        for user in mock_users:
            dist = haversine_distance(payload.latitude, payload.longitude, user["lat"], user["lon"])
            if dist <= 2.0:  # 2 Kilometers లోపు ఉంటే
                nearby_users.append(user["id"])
                tokens_to_alert.append(user["token"])

        # Background tasks running
        if tokens_to_alert:
            background_tasks.add_task(mock_firebase_push, tokens=tokens_to_alert)

        sms_msg = f"EMERGENCY! User {payload.user_id} needs help at Lat: {payload.latitude}, Lon: {payload.longitude}"
        background_tasks.add_task(mock_twilio_sms, to_number=payload.emergency_contact, msg=sms_msg)

        return SOSResponse(
            status="Success",
            message="SOS triggered successfully!",
            nearby_users_alerted=nearby_users
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# --- 5. AUTOMATIC RUNNER ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)