from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from config import settings

Base = declarative_base()
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Dependency that provides a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    projects = relationship('Project', back_populates='user', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'created_at': self.created_at.isoformat(),
        }


class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    project_name = Column(String(255), nullable=False)
    prompt = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='projects')
    generated_websites = relationship(
        'GeneratedWebsite', back_populates='project', cascade='all, delete-orphan'
    )

    def to_dict(self, include_websites=False):
        data = {
            'id': self.id,
            'user_id': self.user_id,
            'project_name': self.project_name,
            'prompt': self.prompt,
            'created_at': self.created_at.isoformat(),
        }
        if include_websites:
            data['generated_websites'] = [w.to_dict() for w in self.generated_websites]
        return data


class GeneratedWebsite(Base):
    __tablename__ = 'generated_websites'

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    html_code = Column(Text)
    css_code = Column(Text)
    js_code = Column(Text)
    metadata_ = Column('metadata', JSON, default={})
    created_at = Column(DateTime, default=datetime.utcnow)

    project = relationship('Project', back_populates='generated_websites')

    def to_dict(self):
        return {
            'id': self.id,
            'project_id': self.project_id,
            'html_code': self.html_code,
            'css_code': self.css_code,
            'js_code': self.js_code,
            'metadata': self.metadata_,
            'created_at': self.created_at.isoformat(),
        }


class Template(Base):
    __tablename__ = 'templates'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    category = Column(String(100), nullable=False)
    html_template = Column(Text)
    css_template = Column(Text)
    js_template = Column(Text)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'html_template': self.html_template,
            'css_template': self.css_template,
            'js_template': self.js_template,
        }
