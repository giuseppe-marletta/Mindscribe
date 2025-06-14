from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.agents.organizer import organize_text
from app.agents.editor import edit_text
from app.utils.io import save_to_file
from app.utils.logger import log_interaction

router = APIRouter()

class TextInput(BaseModel):
    content: str
    style: Optional[str] = None

class EditRequest(BaseModel):
    content: str
    instruction: str

class ExportRequest(BaseModel):
    content: str
    format: str  # "markdown" o "pdf"

@router.post("/organize")
async def organize_endpoint(input_data: TextInput):
    try:
        organized_text = await organize_text(input_data.content)
        log_interaction("organize", input_data.content, organized_text)
        return {"organized_text": organized_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/edit")
async def edit_endpoint(edit_request: EditRequest):
    try:
        edited_text = await edit_text(edit_request.content, edit_request.instruction)
        log_interaction("edit", edit_request.content, edited_text, edit_request.instruction)
        return {"edited_text": edited_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/export")
async def export_endpoint(export_request: ExportRequest):
    try:
        file_path = await save_to_file(export_request.content, export_request.format)
        return {"file_path": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 