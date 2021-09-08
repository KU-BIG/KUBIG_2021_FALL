import datasets

class PrepareData:
    def __init__(self, tokenizer):
        '''create train data and validation data'''
        print('Preparing data ...')
        data = datasets.load_dataset("knews_dataset.py", split="train")
        train_data_txt, validation_data_txt = data.train_test_split(test_size=0.1).values()

        # tokenization
        encoder_max_length = 600
        decoder_max_length = 64

        train_data = train_data_txt.map(
        lambda batch: self.batch_tokenize_preprocess(
            batch, tokenizer, encoder_max_length, decoder_max_length
        ),
        batched=True,
        remove_columns=train_data_txt.column_names,
        )

        validation_data = validation_data_txt.map(
        lambda batch: self.batch_tokenize_preprocess(
            batch, tokenizer, encoder_max_length, decoder_max_length
        ),
        batched=True,
        remove_columns=validation_data_txt.column_names,
        )

        self.train_data = train_data
        self.validation_data = validation_data


    def batch_tokenize_preprocess(self, batch, tokenizer, max_source_length, max_target_length):
        source, target = batch["article_original"], batch["abstractive"]
        source_tokenized = tokenizer(
            source, padding="max_length", truncation=True, max_length=max_source_length
        )
        target_tokenized = tokenizer(
            target, padding="max_length", truncation=True, max_length=max_target_length
        )
        batch = {k: v for k, v in source_tokenized.items()}
        # Ignore padding in the loss
        batch["labels"] = [
            [-100 if token == tokenizer.pad_token_id else token for token in l]
            for l in target_tokenized["input_ids"]
        ]
        return batch
