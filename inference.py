from BertNer import Ner

model = Ner("out_base/")

output = model.predict("I want to go to Paris with Steve.")

print(output)
'''
    [
        {
            "confidence": 0.9981840252876282,
            "tag": "B-PER",
            "word": "Steve"
        },
        {
            "confidence": 0.9998939037322998,
            "tag": "O",
            "word": "went"
        },
        {
            "confidence": 0.999891996383667,
            "tag": "O",
            "word": "to"
        },
        {
            "confidence": 0.9991968274116516,
            "tag": "B-LOC",
            "word": "Paris"
        }
    ]
'''