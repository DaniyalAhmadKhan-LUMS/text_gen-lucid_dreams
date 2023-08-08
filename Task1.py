import openai

openai.api_key = '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'

company_sector = "Tech"
partial_title = "Soft"

PROMPT=f"""
Your job is provide suggestion for the employee roles given the company sector and partial title.

The output should always be in the format of a json. Return nothing else in the response.
The output can take the following format:

{{
    "sector": "TECH",
    "request": "Soft",
    "suggestion":
        {{
            "Employee role": "Software Engineer",
        }}
    "sector": "TECH",
    "request": "Soft",
    "suggestion":
        {{
            "Employee role": "Software Tester",
        }}
        // any other suggestions here
}}

"""
message = f"""
Given a company in the {company_sector} sector, what are the likely job titles starting with '{partial_title}'?
"""

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": PROMPT},
    {"role": "user", "content": message}
    ],
    max_tokens=100,
    temperature=0.2
)

completions = response.choices[0]['message']['content']  # Assuming the model returns a comma-separated list
print(completions)

