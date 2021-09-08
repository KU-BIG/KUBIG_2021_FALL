from prepare_data import PrepareData
from metrics import compute_metrics

from transformers import (
    PreTrainedTokenizerFast,
    BartForConditionalGeneration,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer,
    DataCollatorForSeq2Seq,
)
import argparse


## train 코드 
class Train:
    def __init__(self):
        self.model = BartForConditionalGeneration.from_pretrained("hyunwoongko/kobart")
        self.model.config.__dict__['max_length'] = 64
        print('modified model config max_len 20 -> 64...')
        self.tokenizer = PreTrainedTokenizerFast.from_pretrained("hyunwoongko/kobart")

        p = PrepareData(self.tokenizer)
        self.train_data = p.train_data
        self.validation_data = p.validation_data

    def initialize_trainers(self, do_train=False, do_eval=False):
        training_args = Seq2SeqTrainingArguments(
            output_dir="result",
            num_train_epochs=3,  
            do_train=do_train,
            do_eval=do_eval,
            per_device_train_batch_size=8, 
            per_device_eval_batch_size=1,
            # learning_rate=3e-05,
            warmup_steps=500,
            weight_decay=0.1,
            label_smoothing_factor=0.1,
            predict_with_generate=True,
            logging_dir="logs",
            logging_steps=50,
            save_total_limit=3,
        )

        data_collator = DataCollatorForSeq2Seq(self.tokenizer, model=self.model)

        self.trainer = Seq2SeqTrainer(
            model=self.model,
            args=training_args,
            data_collator=data_collator,
            train_dataset=self.train_data,
            eval_dataset=self.validation_data,
            tokenizer=self.tokenizer,
            compute_metrics=compute_metrics,
        )
    

    def train(self):
        self.initialize_trainers(do_train=True)
        self.trainer.train()


    def eval(self):
        self.initialize_trainers(do_eval=True)
        self.trainer.evaluate()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fine-tuning Kobart model. Choose to train or evaluate the model.")
    parser.add_argument('--mode', type=str, required=True, help="Enter 'train' or 'eval'.")
    args = parser.parse_args()

    t = Train()
    if args.mode == 'train':
        print('Fine-tuning Kobart model ...')
        t.train()
    elif args.mode == 'eval':
        print('Evaluating fine-tuned model ...')
        t.eval()