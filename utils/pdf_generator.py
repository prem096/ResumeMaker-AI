import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from textwrap import wrap

def generate_chart(chart_id, matched, missing):
    """
    Generate a bar chart image showing matched vs missing skills.
    """
    labels = ['Matched Skills', 'Missing Skills']
    values = [len(matched), len(missing)]

    plt.figure(figsize=(5, 3))
    plt.bar(labels, values, color=['#28a745', '#dc3545'])
    plt.title("\n".join(wrap(f'Skill Alignment - {chart_id}', 50)), pad=10)

    safe_chart_name = chart_id.replace('.pdf', '').replace(' ', '_')
    chart_path = os.path.join("static", "charts", f"{safe_chart_name}_chart.png")
    os.makedirs(os.path.dirname(chart_path), exist_ok=True)

    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()
    return chart_path

def generate_pdf_summary(resume_name, jd_name, score, matched, missing, extra, suggestions, role=None, output_dir="summaries"):
    """
    Generate a PDF summary report including alignment chart and skill breakdown.
    """
    # Sanitize filenames
    resume_safe = str(resume_name).replace('.pdf', '').replace(' ', '_')
    jd_safe = str(jd_name).replace('.pdf', '').replace(' ', '_')
    chart_id = f"{resume_safe}_vs_{jd_safe}"

    # Create chart
    chart_path = generate_chart(chart_id, matched or [], missing or [])

    # Render HTML
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("pdf_template.html")
    html_content = template.render(
        resume_name=resume_name,
        jd_name=jd_name,
        score=round(score * 100, 2),
        matched=matched or [],
        missing=missing or [],
        extra=extra or [],
        suggestions=suggestions or [],
        role=role,
        chart_path=chart_path
    )

    # Write PDF
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{chart_id}_summary.pdf")
    HTML(string=html_content, base_url='.').write_pdf(output_path)
    return output_path
