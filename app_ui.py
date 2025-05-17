# Gradio app for interacting with the agent
import gradio as gr
from resume_parser import parse_resume
from critique_agent import critique_resume
from enhancement_agent import enhance_resume
from rag_module import tailor_to_job


def process_resume(file, job_desc):
    parsed = parse_resume(file.name)
    full_text = str(parsed)
    critique = critique_resume(full_text)
    improved = enhance_resume(full_text)
    tailored = tailor_to_job(job_desc, improved)
    return critique, improved, tailored

def launch_app():
    iface = gr.Interface(
        fn=process_resume,
        inputs=[gr.File(label="Upload Resume"), gr.Textbox(label="Job Description")],
        outputs=["text", "text", "text"],
        title="AI Resume Critique & Enhancement Agent"
    )
    iface.launch()
