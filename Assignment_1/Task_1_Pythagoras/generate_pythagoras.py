import os
from google import genai

# Set up the Gemini API client
gemini_client = genai.Client()

# Formulate the prompt based on the assignment instructions
generation_prompt = """
Please write a fully functional Python script using the Manim Community library to animate a visual proof of the Pythagorean Theorem (a^2 + b^2 = c^2).

Specific instructions:
- Draw a right-angled triangle and label its edges as 'a', 'b', and 'c'.
- Animate the creation of filled/shaded squares attached to each of these three edges.
- Show the mathematical formula a^2 + b^2 = c^2 clearly on the screen.
- Match the colors of the side labels to their corresponding squares for clarity.
- Include self.play() and self.wait() statements so the animation paces well and is easy to follow.

Output ONLY the raw Python code within a standard markdown code block. Do not add any conversational text before or after the code.
"""

print("Requesting Manim code from Gemini API for Task 1...")

# Call the API
response = gemini_client.models.generate_content(
    model='gemini-2.5-flash',
    contents=generation_prompt,
)

save_path = "task1_pythagoras/pythagoras.py"
api_result = response.text

# Extract the raw code from the markdown formatting
if "```python" in api_result:
    final_code = api_result.split("```python")[1].split("```")[0].strip()
elif "```" in api_result:
    final_code = api_result.split("```")[1].split("```")[0].strip()
else:
    final_code = api_result.strip()

# Write the extracted code to the target file
with open(save_path, "w", encoding="utf-8") as file:
    file.write(final_code)

print(f"Done! The generated scene has been saved to {save_path}")
