import json
from ai_logic import get_bot_response

with open('test_questions.json', 'r', encoding='utf-8') as f:
    test_set = json.load(f)

total = len(test_set)
correct = 0

for item in test_set:
    user_q = item['question']
    expected = item['expected_answer']
    bot_ans = get_bot_response(user_q)
    print(f"Q: {user_q}\nBot: {bot_ans}\nExpected: {expected}\n")
    if bot_ans.strip() == expected.strip():
        correct += 1

accuracy = correct / total * 100 if total > 0 else 0
print(f"Accuracy: {accuracy:.2f}% ({correct}/{total})") 