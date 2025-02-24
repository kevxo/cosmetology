from fastapi import FastAPI, Request
import httpx

app = FastAPI()

# Backend service URLs
USER_SERVICE_URL = "http://user-service:80001"
APPOINTMENT_SERVICE_URL = "http://appointment-service:8002"
PAYMENT_SERVICE_URL = "http://payment-service:8003"
NOTIFICATION_SERVICE_URL = "http://notification-service:8004"

async def forward_request(service_url: str, request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=f"{service_url}{request.url.path}",
            headers=dict(request.headers),
            content=await request.body()
        )

    return response.json()


# user service routes
@app.api_route("/users/{full_path:path}", methods=["GET", "POST","PUT", "DELETE"])
async def user_proxy(request: Request, full_path: str):
    return await forward_request(USER_SERVICE_URL, request)

# appointment service routes
@app.api_route("/appointments/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def appointment_proxy(request: Request, full_path: str):
    return await forward_request(APPOINTMENT_SERVICE_URL, request)

# payment service routes
@app.api_route("/payments/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def payment_proxy(request: Request, full_path: str):
    return await forward_request(PAYMENT_SERVICE_URL, request)

# notification service routes
@app.api_route("/notifications/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def notification_service(request: Request, full_path: str):
    return await forward_request(NOTIFICATION_SERVICE_URL, request)
