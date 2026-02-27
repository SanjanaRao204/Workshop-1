class Evaluator:
    def __init__(self):
        pass

    def evaluate(self, query, response):
        score = 0

        # 1️⃣ Length Check (30 marks)
        if len(response) > 150:
            score += 30
        elif len(response) > 80:
            score += 20
        else:
            score += 10

        # 2️⃣ Relevance Check (40 marks)
        query_words = query.lower().split()
        match_count = sum(word in response.lower() for word in query_words)

        if match_count >= 3:
            score += 40
        elif match_count >= 1:
            score += 25
        else:
            score += 10

        # 3️⃣ Basic Quality Check (30 marks)
        if "error" not in response.lower():
            score += 30

        # Final score capped at 100
        final_score = min(score, 100)

        return {
            "score_out_of_100": final_score
        }