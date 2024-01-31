from fastapi import FastAPI,Request,HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from config.database import shutdown
from routes import music_routes,user_routes,auth_routes
import uvicorn
import time
import os
from helper.FirebaseAuth import Verify_Token
app=FastAPI(
    description="This is the backend for HPMP",
    title="HPMP Backend",
    docs_url="/"
)


    
app.include_router(music_routes.HPMP_api_router)
app.include_router(user_routes.user_router)
app.include_router(auth_routes.auth_router)

origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event("shutdown")
async def shutdown_event():
    shutdown()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    try:
        token=request.headers["Authorization"]
        user=Verify_Token(token)
        if user["status"]=="ok":
            headers = dict(request.scope['headers'])
            headers[b"user"]=user
            request.scope['headers'] = [(k, v) for k, v in headers.items()]
        else:
            return JSONResponse(status_code=401,content={"reason":"Not Authorized"})
    except KeyError:
        if os.environ.get("ENV_NAME")!="dev":
            return JSONResponse(status_code=401,content={"reason":"Not Authorized"})
        else:
            pass
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

if __name__=="__main__":
    uvicorn.run("main:app",reload=True)