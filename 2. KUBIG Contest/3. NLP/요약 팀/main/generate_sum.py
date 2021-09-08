
from transformers import (
    PreTrainedTokenizerFast,
    BartForConditionalGeneration)
import re, os
import pdb


class TextSummarize:
    def __init__(self, model_name):
        '''initialize fine-tuned model (should be located in ../model'''
        self.tokenizer = PreTrainedTokenizerFast.from_pretrained("hyunwoongko/kobart")
        model_dir = os.path.dirname(os.path.dirname(__file__))
        self.model = BartForConditionalGeneration.from_pretrained(os.path.join(model_dir,f"model/{model_name}"))
        self.model.config.__dict__['max_length'] = 200
    def generate_summary(self, org_input, model, tokenizer):
        '''generate by fine-tuned kobart model'''
        tokenizer = self.tokenizer
        model = self.model

        inputs = tokenizer(
            org_input,
            padding="max_length",
            truncation=True,
            max_length=600,
            return_tensors="pt",
        )
        input_ids = inputs.input_ids.to(model.device)
        attention_mask = inputs.attention_mask.to(model.device)
        outputs = model.generate(input_ids, attention_mask=attention_mask)
        output_str = tokenizer.decode(outputs[0], skip_special_tokens=True)
        # pdb.set_trace()
        return outputs, output_str

    def gen(self, org_input):
        '''returns final output'''
        org_input = re.sub('\n', ' ', org_input)
        summaries_after_tuning = self.generate_summary(org_input, self.model, self.tokenizer)[1]

        return summaries_after_tuning



if __name__ == '__main__':
    g = TextSummarize()
    org_input = input("Put any article: ")
    print(g.gen(org_input))
