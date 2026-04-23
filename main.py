from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from detector import detect_ingredients
from recipe_gen import generate_recipes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "FridgeVision is running!"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg", "image/png", "image/webp"]:
        raise HTTPException(status_code=400, detail="Upload JPEG or PNG only")

    image_bytes = await file.read()
    ingredients = detect_ingredients(image_bytes)
    recipes = generate_recipes(ingredients)

    return JSONResponse({
        "ingredients": ingredients,
        "recipes": recipes,
        "count": len(ingredients)
    })
```

---

## ▶️ RUN BACKEND NOW

After creating all 4 files, run this in terminal (with venv active):
```
uvicorn main:app --reload --port 8000
```

✅ Open browser → `http://localhost:8000` → must see `{"message":"FridgeVision is running!"}`

---

## 🖥️ SETUP FRONTEND FIRST

Open a **NEW second terminal** (click + in terminal panel) and run:
```
cd Desktop\fridgevision\frontend
npm create vite@latest . -- --template react
npm install
npm install axios