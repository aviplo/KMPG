def user_prompt_qa(user_info: dict) -> str:
    return f"""
You are responding to a user who is asking about their healthcare services, based on their HMO and insurance membership tier.

User Information:
{user_info}

Please answer in a clear and helpful tone, using the appropriate language based on the user's input. The response should reflect the services and rules that apply to the user's HMO and membership tier only.
"""