import flet as ft

def main(page: ft.Page):
    page.title = "Simple Notepad"
    page.padding = 20

    word_count_text = ft.Text("Words: 0")
    char_count_text = ft.Text("Characters: 0")

    def update_counts(value: str):
        char_count_text.value = f"Characters: {len(value)}"

        words = value.strip().split()
        word_count_text.value = f"Words: {len(words)}"

    def on_text_change(e: ft.ControlEvent):
        update_counts(e.control.value)
        page.update()

    def clear_text(e: ft.ControlEvent):
        text_box.value = ""
        update_counts("")
        page.update()

    text_box = ft.TextField(
        label="Type here...",
        multiline=True,
        min_lines=1,
        max_lines=20,
        expand=True,
        on_change=on_text_change,
    )

    clear_button = ft.ElevatedButton("Clear", on_click=clear_text)

    page.add(
        text_box,
        ft.Row([word_count_text, char_count_text, clear_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
    )

ft.app(target=main)