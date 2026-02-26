def build_prompt(topic: str):
    return f"""
You are a structured response generator for downstream software.

STRICT RULES:
- Return ONLY valid JSON
- No extra text
- No markdown
- No explanations outside JSON

Required JSON format:
{{
  "topic": "{topic}",
  "definition": "<one clear sentence>",
  "key_points": ["point1", "point2", "point3"]
}}

Generate response now.
"""