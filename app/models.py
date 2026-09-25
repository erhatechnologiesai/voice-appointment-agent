from pydantic import BaseModel
from typing import Optional

class SpokenAppointmentIntent(BaseModel):
    call_sid: str
    user_speech: str

class VoiceAppointmentAction(BaseModel):
    call_sid: str
    system_response: str
    booking_status: str # AWAITING_DATE, DATE_CONFIRMED, BOOKING_COMPLETED
