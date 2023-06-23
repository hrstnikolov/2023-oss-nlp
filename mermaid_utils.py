def generate_mermaid_code(input_text):
    steps = input_text.splitlines()
    processed_steps = []

    for step in steps:
        if step.startswith(" "):  # Sub-step
            processed_steps.append(step.strip())
        else:  # Main step
            if processed_steps:
                processed_steps[-1] = {processed_steps[-1]: processed_steps[-1]}
            processed_steps.append(step.strip())

    mermaid_code = "```mermaid\n"
    mermaid_code += "graph TD\n"

    # Generate nodes
    for i, step in enumerate(processed_steps, start=1):
        if isinstance(step, dict):  # Sub-step
            for sub_step in step.values():
                mermaid_code += f"    {i}({sub_step})\n"
        else:  # Main step
            mermaid_code += f"    {i}({step})\n"

    # Generate connections
    mermaid_code += f"    {1}"
    for i in range(2, len(processed_steps) + 1):
        mermaid_code += f" --> {i}"
    mermaid_code += "\n"

    # Generate subgraph
    if any(isinstance(step, dict) for step in processed_steps):
        mermaid_code += "\n    subgraph preprocess\n"
        for i, step in enumerate(processed_steps, start=1):
            if isinstance(step, dict):
                for sub_step in step.values():
                    mermaid_code += f"        {i}\n"
        mermaid_code += "    end\n"

    mermaid_code += "```"
    return mermaid_code


# Example usage
input_text = """
download
    find in web
develop
preprocess
    clean
    filter
umap
    embedding
"""

output_mermaid_code = generate_mermaid_code(input_text)
print(output_mermaid_code)
