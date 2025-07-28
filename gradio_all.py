import gradio as gr

from llm_module import query_strava

# Create simple interface
def create_simple_interface():
    with gr.Blocks(title="Strava Assistant") as demo:
        gr.Markdown("# 🏃‍♂️ Strava Activity Assistant")
        gr.Markdown("Ask questions about your Strava activities!")
        
        with gr.Row():
            with gr.Column():
                query_input = gr.Textbox(
                    label="Your Question",
                    placeholder="e.g., How far did I run yesterday?",
                    lines=2
                )
                submit_btn = gr.Button("Ask", variant="primary")
                
            with gr.Column():
                # Quick examples
                gr.Markdown("### Quick Examples:")
                example_queries = [
                    "How far did I run today?",
                    "Describe my session on Saturday", 
                    "What was my longest run this week?",
                    "How many activities this month?"
                ]
                
                for query in example_queries:
                    btn = gr.Button(query, size="sm")
                    btn.click(lambda q=query: q, outputs=query_input)
        
        response_output = gr.Textbox(
            label="Response",
            lines=10,
            max_lines=20
        )
        
        submit_btn.click(
            fn=query_strava,
            inputs=query_input,
            outputs=response_output
        )
        
        query_input.submit(
            fn=query_strava,
            inputs=query_input,
            outputs=response_output
        )
    
    return demo

if __name__ == "__main__":
    demo = create_simple_interface()
    demo.launch(
        server_port=7860,
        share=False,
        inbrowser=True
    )