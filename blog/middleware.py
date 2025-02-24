from django.shortcuts import redirect
from django.utils.timezone import now
from django.urls import reverse
from datetime import datetime, timedelta

SESSION_TIMEOUT_SECONDS = 3600

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity_str = request.session.get("last_activity")

            if last_activity_str:
                last_activity = datetime.fromisoformat(last_activity_str).replace(tzinfo=now().tzinfo)
                idle_time = (now() - last_activity)

                if idle_time > timedelta(seconds=SESSION_TIMEOUT_SECONDS):
                    request.session.flush()
                    return redirect(f"{reverse('admin_login')}?next={request.path}")

            request.session["last_activity"] = now().isoformat()

        response = self.get_response(request)
        return response
