from fastapi import FastAPI, Request, Depends, HTTPException
from authentication.auth import verify_token
from constants import SERVICES_MAPPER
import httpx

app = FastAPI()

@app.api_route("/{service}/{full_path:path}", methods=["GET", "POST","PUT", "DELETE"])
async def proxy(request: Request, service: str, full_path: str, user=Depends(verify_token)):
    if service not in SERVICES_MAPPER:
        raise HTTPException(status_code=404, detail="Service not found")

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=f"{SERVICES_MAPPER[service]}{full_path}",
            headers=dict(request.headers),
            content=await request.body()
        )

    return response.json()
