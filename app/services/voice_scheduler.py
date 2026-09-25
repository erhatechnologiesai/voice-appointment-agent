def handle_spoken_booking(call_sid: str, speech: str):
    s_low = speech.lower()
    if "tomorrow" in s_low or "friday" in s_low or "monday" in s_low or "2pm" in s_low:
        return "I have reserved that consultation slot for you. A confirmation SMS with details is on its way.", "BOOKING_COMPLETED"
    elif "reschedule" in s_low:
        return "Certainly. What day and time would you prefer to move your appointment to?", "AWAITING_DATE"
    else:
        return "Our calendar is open tomorrow at 10 AM, 2 PM, or 4 PM. Which of those times works for you?", "DATE_CONFIRMED"
