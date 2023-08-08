import openai


OPENAI_API_KEY='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'

openai.api_key=OPENAI_API_KEY

company_sector = "Automotive"
user_request = "I want to hire a team for electric vehicle R&D with a budget of $2M for the next 3 years."

PROMPT=f"""
Given a company in the {company_sector} sector and the constraint '{user_request}',
provide a list of employee suggestions including department, role, yearly salary, bonus, and start date.
Include the people who are vital to run a organisation in that sector.

The output should always be in the format of a json. Return nothing else in the response.
The output can take the following format:

{{
    "sector": "Healthcare",
    "request": "I want to spend 70% of my $1M budget on payroll for the next 2 years",
    "suggestions": [
        {{
            "department": "R&D",
            "role": "Medical Researcher",
            "yearly_salary": "$80,000",
            "bonus": "$5,000",
            "start_date": "2023-09-01"
        }},
        {{
            "department": "G&A",
            "role": "Hospital Administrator",
            "yearly_salary": "$70,000",
            "bonus": "$4,000",
            "start_date": "2023-10-01"
        }},
        // Other suggestions here
    ]
}}

"""


messages = [{"role": "system", "content": PROMPT},{"role": "user", "content": user_request}]



response =openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  max_tokens=300,
  messages=messages


)
compeletions = response.choices[0]['message']['content']
print(compeletions)