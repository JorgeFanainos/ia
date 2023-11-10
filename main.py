import openai  # pip install openai
import typer  # pip install "typer[all]"
import speech_recognition as sr
from rich import print  # pip install rich
from rich.table import Table

"""
Webs de interés:
- Módulo OpenAI: https://github.com/openai/openai-python
- Documentación API ChatGPT: https://platform.openai.com/docs/api-reference/chat
- Typer: https://typer.tiangolo.com
- Rich: https://rich.readthedocs.io/en/stable/
"""


def main():

    openai.api_key = "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"

    print("💬 [bold green]ChatGPT API en Python[/bold green]")

    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Crear una nueva conversación")

    print(table)

    # Contexto del asistente
    context = {"role": "system",
               "content": "Eres un asistente muy útil."}
    messages = [context]

    while True:

        content = __prompt()

        if content == "new":
            print("🆕 Nueva conversación creada")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")


def __prompt() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
    # read the audio data from the default microphone
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
    # convert speech to text
        text = r.recognize_google(audio_data, language="es-ES")
        print(text)
        prompt = text
    if prompt == "exit":
        exit = typer.confirm("✋ ¿Estás seguro?")
        if exit:
            print("👋 ¡Hasta luego!")
            raise typer.Abort()

        return __prompt()

    return prompt


if __name__ == "__main__":
    typer.run(main)