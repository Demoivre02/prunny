def generate_summary_prompt(article: str) -> str:
    prompt = f"""
    Please provide a concise and informative summary of the following news article. The summary should:
    1. Capture the main points and key information
    2. Be no longer than 3-4 sentences
    3. Maintain a neutral tone
    4. Exclude any personal opinions or interpretations

    Article:
    {article}

    Summary:
    """
    return prompt


article = """
In a groundbreaking development, scientists at the University of Cambridge have successfully created a living, self-replicating robot using stem cells derived from frog embryos. These tiny machines, dubbed "xenobots," are less than a millimeter wide and can move, work together in groups, and even heal themselves. The researchers believe that these biodegradable, living robots could have numerous applications in medicine, environmental cleanup, and other fields. However, the creation of these xenobots also raises ethical questions about the boundaries between living organisms and machines, prompting calls for further discussion on the implications of such technology.
"""

summary_prompt = generate_summary_prompt(article)
print(summary_prompt)