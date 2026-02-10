from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class LlamaWebGenerator:
    def __init__(self):
        self.model_name = "meta-llama/Llama-2-7b-chat-hf"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            torch_dtype=torch.float16,
            device_map="auto",
            load_in_8bit=True  # For memory optimization
        )
    
    def generate_code(self, prompt, component_type):
        system_prompt = f"""You are an expert web developer. Generate clean, 
        semantic HTML, modern CSS, and vanilla JavaScript for a {component_type}.
        
        User Request: {prompt}
        
        Generate ONLY the code without explanations. Use this format:
        HTML:
        [html code]
        
        CSS:
        [css code]
        
        JS:
        [javascript code if needed]
        """
        
        inputs = self.tokenizer(system_prompt, return_tensors="pt").to("cuda")
        outputs = self.model.generate(
            **inputs,
            max_length=2048,
            temperature=0.7,
            top_p=0.9,
            do_sample=True
        )
        
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
