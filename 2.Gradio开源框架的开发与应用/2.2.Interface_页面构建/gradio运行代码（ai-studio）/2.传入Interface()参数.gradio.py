import gradio as gr

def greet(name):
  return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="textbox", outputs="textbox",
          title='测试', description='测试页面')

if __name__ == "__main__":
  demo.launch()