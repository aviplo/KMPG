


def build_info_collection_prompt(user_info: dict) -> str:
    return f"""
            Current user information collected so far: {user_info}
            Please continue the conversation to collect any missing required information or help the user complete their registration.
        """