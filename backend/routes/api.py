from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Optional

from models import get_db, Project, GeneratedWebsite, Template
from services.llm_service import llm_service
from services.code_parser import combine_code

router = APIRouter()


# ── Request / Response Schemas ────────────────────────────────────────────────

class GenerateRequest(BaseModel):
    prompt: str
    project_name: Optional[str] = None
    template_id: Optional[int] = None


# ── Generate Website ──────────────────────────────────────────────────────────

@router.post('/generate', status_code=201)
def generate_website(body: GenerateRequest, db: Session = Depends(get_db)):
    """Accept a prompt and return generated HTML/CSS/JS."""
    project_name = body.project_name or body.prompt[:60]

    # Optionally use a base template
    template_data = None
    if body.template_id:
        template = db.query(Template).get(body.template_id)
        if template:
            template_data = template.to_dict()

    # Generate code with LLM
    result = llm_service.generate_website(body.prompt, template=template_data)

    # Persist to database
    project = Project(project_name=project_name, prompt=body.prompt)
    db.add(project)
    db.flush()

    website = GeneratedWebsite(
        project_id=project.id,
        html_code=result['html'],
        css_code=result['css'],
        js_code=result['js'],
        metadata_={'prompt': body.prompt, 'template_id': body.template_id},
    )
    db.add(website)
    db.commit()
    db.refresh(project)
    db.refresh(website)

    preview_html = combine_code(result['html'], result['css'], result['js'])

    return {
        'project': project.to_dict(),
        'website': website.to_dict(),
        'preview_html': preview_html,
    }


# ── Projects ──────────────────────────────────────────────────────────────────

@router.get('/projects')
def list_projects(db: Session = Depends(get_db)):
    """List all projects, newest first."""
    projects = db.query(Project).order_by(Project.created_at.desc()).all()
    return [p.to_dict() for p in projects]


@router.get('/projects/{project_id}')
def get_project(project_id: int, db: Session = Depends(get_db)):
    """Get a single project with its generated websites."""
    project = db.query(Project).get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project.to_dict(include_websites=True)


@router.delete('/projects/{project_id}')
def delete_project(project_id: int, db: Session = Depends(get_db)):
    """Delete a project and its generated websites."""
    project = db.query(Project).get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(project)
    db.commit()
    return {'message': 'Project deleted.'}


# ── Templates ─────────────────────────────────────────────────────────────────

@router.get('/templates')
def list_templates(category: Optional[str] = Query(None), db: Session = Depends(get_db)):
    """List all templates, optionally filtered by category."""
    query = db.query(Template)
    if category:
        query = query.filter(Template.category == category)
    templates = query.order_by(Template.category, Template.name).all()
    return [t.to_dict() for t in templates]


@router.get('/templates/{template_id}')
def get_template(template_id: int, db: Session = Depends(get_db)):
    """Get a single template."""
    template = db.query(Template).get(template_id)
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    return template.to_dict()
