


from fastapi import FastAPI, UploadFile, File
import joblib
from preprocessing.parse_resume import extract_text_from_pdf

app = FastAPI()
model = joblib.load("../models/ats_model.pkl")

@app.post("/check-resume/")
async def check_resume(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file.file)
    score = model.predict([text])[0]
    return {"ATS Score": score}
