from fastapi import FastAPI
from app.config import settings
from app.models import SpokenAppointmentIntent, VoiceAppointmentAction
from app.services.voice_scheduler import handle_spoken_booking

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/voice-appointment", response_model=VoiceAppointmentAction)
def voice_appointment(intent: SpokenAppointmentIntent):
    resp, status = handle_spoken_booking(intent.call_sid, intent.user_speech)
    return VoiceAppointmentAction(
        call_sid=intent.call_sid,
        system_response=resp,
        booking_status=status
    )
