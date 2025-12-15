import gradio as gr

with gr.Blocks() as demo:
  text_count = gr.State(1)

  add_btn = gr.Button("Add Box")
  add_btn.click(lambda x: x + 1, text_count, text_count)

  @gr.render(inputs=text_count)
  def render_count(count):
    gr.Markdown(f"### 当前组件数：{count}")
    for i in range(count):
      gr.Textbox(label=f"Box {i + 1}", key = f"textbox-{i}")

demo.launch()