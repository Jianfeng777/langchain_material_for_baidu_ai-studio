import gradio as gr

def greet(name):
  return "Hello " + name + "!"

demo = gr.Interface(fn=greet, 
                    inputs=gr.Textbox(value='ljf',info='请写入你的名称'), 
                    outputs=gr.Textbox(), 
                    title='测试', 
                    description='测试页面')

if __name__ == "__main__":
  demo.launch()