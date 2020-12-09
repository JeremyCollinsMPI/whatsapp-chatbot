from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np

tokenizer = AutoTokenizer.from_pretrained("ipuneetrathore/bert-base-cased-finetuned-finBERT")
model = AutoModelForSequenceClassification.from_pretrained("ipuneetrathore/bert-base-cased-finetuned-finBERT")

review_text = """A tinyurl link takes users to a scamming site promising that users can earn thousands of dollars by becoming a Google ( NASDAQ : GOOG ) Cash advertiser ."""
review_text = """Britain's economy shrank by 20% in the three months to June as it battled with the coronavirus pandemic, the biggest fall of any large advanced economy."""
review_text = """The world's second-biggest economy saw growth of 4.9% between July and September, compared to the same quarter last year."""
MAX_LEN = 160
class_names = ['negative', 'neutral', 'positive']

encoded_new = tokenizer.encode_plus(
                        review_text,                      # Sentence to encode.
                        add_special_tokens = True,        # Add '[CLS]' and '[SEP]'
                        max_length = MAX_LEN,             # Pad & truncate all sentences.
                        pad_to_max_length = True,
                        return_attention_mask = True,     # Construct attn. masks.
                        return_tensors = 'pt',            # Return pytorch tensors.
                   )

# Add the encoded sentence to the list.    
input_idst = (encoded_new['input_ids'])
attention_maskst = (encoded_new['attention_mask'])

# Convert the lists into tensors.
input_idst = torch.cat([input_idst], dim=0)
attention_maskst = torch.cat([attention_maskst], dim=0)


new_test_output = model(input_idst, token_type_ids=None, 
                      attention_mask=attention_maskst)

logits = new_test_output[0]
predicted = logits.detach().numpy()

# Store predictions
flat_predictions = np.concatenate(predicted, axis=0)

# For each sample, pick the label (0 or 1) with the higher score.
new_predictions = np.argmax(flat_predictions).flatten()

print(class_names[new_predictions[0]])