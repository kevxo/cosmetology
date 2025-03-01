# Backend service URLs
USER_SERVICE_URL = "http://user-service:80001"
APPOINTMENT_SERVICE_URL = "http://appointment-service:8002"
PAYMENT_SERVICE_URL = "http://payment-service:8003"
NOTIFICATION_SERVICE_URL = "http://notification-service:8004"

SERVICES_MAPPER = {
    'users': USER_SERVICE_URL,
    'appointments': APPOINTMENT_SERVICE_URL,
    'payments': PAYMENT_SERVICE_URL,
    'notifications': NOTIFICATION_SERVICE_URL
}
