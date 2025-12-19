import gradio as gr

with gr.Blocks() as demo:
    question_num = gr.Number(
        label="评估问题数",
        value=2,
        minimum=1,
        precision=0
    )

    questions_state = gr.State([])

    @gr.render(inputs=[question_num, questions_state])
    def render_questions(num, questions):
        num = int(num)

        # 保证 state 长度和 num 一致
        if len(questions) < num:
            questions.extend([""] * (num - len(questions)))
        else:
            questions[:] = questions[:num]

        boxes = []
        for i in range(num):
            boxes.append(
                gr.Textbox(
                    label=f"评估问题 {i + 1}",
                    value=questions[i],
                    placeholder=f"请输入第 {i + 1} 个评估问题",
                ).change(
                    fn=lambda v, idx=i: update_question(v, idx),
                    inputs=None,
                    outputs=questions_state
                )
            )
        return boxes

    def update_question(value, index):
        qs = questions_state.value
        qs[index] = value
        return qs

    submit = gr.Button("提交问题")
    output = gr.JSON()

    submit.click(
        fn=lambda qs: qs,
        inputs=questions_state,
        outputs=output
    )

demo.launch()
