# Entry point of the agentic resume enhancer

from resume_parser import parse_resume
from critique_agent import critique_resume
from enhancement_agent import enhance_resume
from rag_module import tailor_to_job
from app_ui import launch_app

if __name__ == '__main__':
    launch_app()
