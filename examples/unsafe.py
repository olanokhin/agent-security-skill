import os
import subprocess

from openai import OpenAI


client = OpenAI()


def summarize_document(user_input: str):
    prompt = f"You are a helpful assistant. Summarize this document: {user_input}"
    return client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
    )


def answer_from_rag(query: str, retrieved_chunk: str, user_id: str):
    prompt = f"""
    Answer the user's question using this internal document.

    Document:
    {retrieved_chunk}

    Question:
    {query}
    """
    return client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )


def run_agent_tool(tool_name: str, tool_args: str):
    if tool_name == "shell":
        return subprocess.check_output(tool_args, shell=True).decode("utf-8")

    if tool_name == "delete_file":
        os.remove(tool_args)
        return "deleted"

    raise ValueError("unknown tool")


def install_suggested_package(package_name_from_llm: str):
    return subprocess.check_call(["pip", "install", package_name_from_llm])
