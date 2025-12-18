import gradio as gr

def divide(numerator, denominator):
  if denominator == 0:
    raise gr.Error("Cannot divide by zero!")

demo = gr.Interface(divide, ["number", "number"], "number")
demo.launch()