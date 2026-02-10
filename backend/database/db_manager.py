from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import sys

# Add parent directory to path to import models
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import Project, GeneratedWebsite, SessionLocal

class DatabaseManager:
    def __init__(self):
        # Use existing SessionLocal from models.py which uses environment variables
        self.session = SessionLocal()
    
    def save_project(self, prompt, code):
        """
        Save parsing results to database.
        code is expected to be a dict with 'html', 'css', 'js'.
        """
        try:
            # Create Project entry
            project = Project(
                project_name="Generated Project", # Placeholder name or extract from prompt
                prompt=prompt,
                user_id=None # Assuming no auth for now
            )
            self.session.add(project)
            self.session.commit()
            
            # Create GeneratedWebsite entry
            website = GeneratedWebsite(
                project_id=project.id,
                html_code=code.get('html_code', ''),
                css_code=code.get('css_code', ''),
                js_code=code.get('js_code', ''),
                metadata_=code.get('metadata', {})
            )
            self.session.add(website)
            self.session.commit()
            
            return project.id
        except Exception as e:
            self.session.rollback()
            raise e
    
    def get_project(self, project_id):
        """Retrieve project by ID."""
        project = self.session.query(Project).filter(Project.id == project_id).first()
        if project:
            return project.to_dict(include_websites=True)
        return None
    
    def __del__(self):
        self.session.close()
